# `cliautor`

A command line tool to generate command line interfaces for your command line tools from YAML-based schema.

## Highlights

- defines a CLI schema in YAML.
- provides a typed CLI code generator.

## CLI schema

The CLI schema definition is provided as `cli-schema-definition.ts`.

## CLI code generator

`cliautor` generates a typed code for handling command line arguments from a YAML file written according to the CLI schema definition.

Supported programming language is only Go currently.

### Installation

The CLI code generator `cliautor` can be installed as follows:

```sh
go install "github.com/Jumpaku/cliautor/cmd/cliautor"
```

### Usage

1. Generating the CLI type.
2. Overwriting the CLI object.
3. Executing program.

#### Generating the CLI type

Prepare the CLI schema for your application, for example:

```yaml
name: greet
description: this is an example program
options:
  -help:
    short: -h
    description: Show help information.
    type: boolean
subcommands:
  hello:
    description: Prints "Hello, <target name>! My name is <greeter>!"
    options:
      -target-name:
        short: -t
        description: The name of the person to be said hello.
    arguments:
      - name: greeter
        description: The name of the person who says hello.
```

Run `cliautor` as follows:

```sh
cliautor golang < path/to/cli-schema.yaml > path/to/generated/code.go
```

The above generates a Go code which includes:

```go
type CLI 
type CLI_Input 
type CLI_Hello 
type CLI_Hello_Input

func NewCLI() CLI
func Run(cli CLI, args []string) error
```

#### Overwriting the CLI object

To define the behavior of your program, you can utilize the generated types and functions as follows:

```go
func main() {
	// Create the CLI object
	cli := NewCLI()
	// Overwrite behaviors
	cli.Func = showHelp
	cli.Sub_Hello.Func = sayHello
	// Run with command line arguments
	if err := Run(cli, os.Args); err != nil {
		panic(err)
	}
}
```

Example implementations for `showHelp` and `sayHello` are as follows:

```go
func showHelp(subcommand []string, input CLI_Input) (err error) {
	if input.Opt_Help {
		fmt.Println("This is an example program.")
	} else {
		fmt.Println("Do nothing.")
	}
	return nil
}
func sayHello(subcommand []string, input CLI_Hello_Input) (err error) {
	hello := "Hello"
	if input.Opt_TargetName != "" {
		hello += ", " + input.Opt_TargetName
	}
	hello += "! My name is " + input.Arg_Greeter + "!"
	fmt.Println(hello)
	return nil
}
```

#### Executing program

Execute the `main` function as follows

```sh
go run main.go -h
# => This is an example program.
go run main.go hello Alice
# => Hello! My name is Alice!
go run main.go hello -target-name=Bob Alice
# => Hello, Bob! My name is Alice!
```

## Details specifications

### handling command line arguments

```
<program> <subcommand> [<option>|<argument>]... [-- [<argument>]...]
```

- `<program>` is the path to your executable file.
- `<subcommand>` is a sequence of tokens, which represents a path in the command tree illustrated in your CLI schema.
    - `<subcommand>` may be empty.
- `<option>` represents an option, which is a token in form of `<option_name>[=<option_value>]`.
    - `<option_name>` must match regular expression `^(-[a-z][a-z0-9]*)+$` (or `^-[a-z]$` in short version).
    - `<option_value>` must be a string that can be parsed as a value of the type of the option.
    - `=<option_value>` can be omitted if the type of the option is boolean.
- `<argument>` represents an argument, which must be a string that can be parsed as a value of the type of the argument.
    - Tokens after `--` are handled as arguments even if prefixed by `-`.

