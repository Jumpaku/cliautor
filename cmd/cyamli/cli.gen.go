// Code generated by cyamli v0.0.13, DO NOT EDIT.
package main

import (
	"fmt"
	"strconv"
	"strings"
)

type Func[Input any] func(subcommand []string, input Input, inputErr error) (err error)

type CLI struct {
	Golang CLI_Golang

	Python3 CLI_Python3

	FUNC Func[CLI_Input]
}

func (CLI) DESC_Simple() string {
	return "cyamli (v0.0.13):\nA command line tool to generate CLI for your app from YAML-based schema.\n\nUsage:\n    $ cyamli [<option>]...\n\nOptions:\n    -help, -version\n\nSubcommands:\n    golang, python3\n\n"
}
func (CLI) DESC_Detail() string {
	return "cyamli (v0.0.13):\nA command line tool to generate CLI for your app from YAML-based schema.\n\nUsage:\n    $ cyamli [<option>]...\n\n\nOptions:\n    -help[=<boolean>], -h[=<boolean>]  (default=false):\n        shows description of this app\n\n    -version[=<boolean>], -v[=<boolean>]  (default=false):\n        shows version of this app\n\n\nSubcommands:\n    golang:\n        generates CLI for your app written in Go.\n\n    python3:\n        generates CLI for your app written in Python3.\n\n"
}

type CLI_Input struct {
	Opt_Help bool

	Opt_Version bool
}

func resolve_CLI_Input(input *CLI_Input, restArgs []string) error {
	*input = CLI_Input{

		Opt_Help: false,

		Opt_Version: false,
	}

	var arguments []string
	for idx, arg := range restArgs {
		if arg == "--" {
			arguments = append(arguments, restArgs[idx+1:]...)
			break
		}
		if !strings.HasPrefix(arg, "-") {
			arguments = append(arguments, arg)
			continue
		}
		optName, lit, cut := strings.Cut(arg, "=")
		consumeVariables(optName, lit, cut)

		switch optName {
		default:
			return fmt.Errorf("unknown option %q", optName)

		case "-help", "-h":
			if !cut {
				lit = "true"

			}
			if err := parseValue(&input.Opt_Help, lit); err != nil {
				return fmt.Errorf("value %q is not assignable to option %q", lit, optName)
			}

		case "-version", "-v":
			if !cut {
				lit = "true"

			}
			if err := parseValue(&input.Opt_Version, lit); err != nil {
				return fmt.Errorf("value %q is not assignable to option %q", lit, optName)
			}

		}
	}

	return nil
}

type CLI_Golang struct {
	FUNC Func[CLI_Golang_Input]
}

func (CLI_Golang) DESC_Simple() string {
	return "generates CLI for your app written in Go.\n\nUsage:\n    $ <program> golang [<option>]...\n\nOptions:\n    -help, -out-path, -package, -schema-path\n\n"
}
func (CLI_Golang) DESC_Detail() string {
	return "generates CLI for your app written in Go.\n\nUsage:\n    $ <program> golang [<option>]...\n\n\nOptions:\n    -help[=<boolean>], -h[=<boolean>]  (default=false):\n        shows description of golang subcommand\n\n    -out-path=<string>  (default=\"\"):\n        if specified then creates a file at the path and writes generated code, otherwise outputs to stdout.\n\n    -package=<string>  (default=\"main\"):\n        package name where the generated file will be placed.\n\n    -schema-path=<string>  (default=\"\"):\n        if specified then reads schema file from the path, otherwise reads from stdin.\n\n"
}

type CLI_Golang_Input struct {
	Opt_Help bool

	Opt_OutPath string

	Opt_Package string

	Opt_SchemaPath string
}

func resolve_CLI_Golang_Input(input *CLI_Golang_Input, restArgs []string) error {
	*input = CLI_Golang_Input{

		Opt_Help: false,

		Opt_OutPath: "",

		Opt_Package: "main",

		Opt_SchemaPath: "",
	}

	var arguments []string
	for idx, arg := range restArgs {
		if arg == "--" {
			arguments = append(arguments, restArgs[idx+1:]...)
			break
		}
		if !strings.HasPrefix(arg, "-") {
			arguments = append(arguments, arg)
			continue
		}
		optName, lit, cut := strings.Cut(arg, "=")
		consumeVariables(optName, lit, cut)

		switch optName {
		default:
			return fmt.Errorf("unknown option %q", optName)

		case "-help", "-h":
			if !cut {
				lit = "true"

			}
			if err := parseValue(&input.Opt_Help, lit); err != nil {
				return fmt.Errorf("value %q is not assignable to option %q", lit, optName)
			}

		case "-out-path":
			if !cut {
				return fmt.Errorf("value is not specified to option %q", optName)

			}
			if err := parseValue(&input.Opt_OutPath, lit); err != nil {
				return fmt.Errorf("value %q is not assignable to option %q", lit, optName)
			}

		case "-package":
			if !cut {
				return fmt.Errorf("value is not specified to option %q", optName)

			}
			if err := parseValue(&input.Opt_Package, lit); err != nil {
				return fmt.Errorf("value %q is not assignable to option %q", lit, optName)
			}

		case "-schema-path":
			if !cut {
				return fmt.Errorf("value is not specified to option %q", optName)

			}
			if err := parseValue(&input.Opt_SchemaPath, lit); err != nil {
				return fmt.Errorf("value %q is not assignable to option %q", lit, optName)
			}

		}
	}

	return nil
}

type CLI_Python3 struct {
	FUNC Func[CLI_Python3_Input]
}

func (CLI_Python3) DESC_Simple() string {
	return "generates CLI for your app written in Python3.\n\nUsage:\n    $ <program> python3 [<option>]...\n\nOptions:\n    -help, -out-path, -schema-path\n\n"
}
func (CLI_Python3) DESC_Detail() string {
	return "generates CLI for your app written in Python3.\n\nUsage:\n    $ <program> python3 [<option>]...\n\n\nOptions:\n    -help[=<boolean>], -h[=<boolean>]  (default=false):\n        shows description of python3 subcommand\n\n    -out-path=<string>  (default=\"\"):\n        if specified then creates a file at the path and writes generated code, otherwise outputs to stdout.\n\n    -schema-path=<string>  (default=\"\"):\n        if specified then reads schema file from the path, otherwise reads from stdin.\n\n"
}

type CLI_Python3_Input struct {
	Opt_Help bool

	Opt_OutPath string

	Opt_SchemaPath string
}

func resolve_CLI_Python3_Input(input *CLI_Python3_Input, restArgs []string) error {
	*input = CLI_Python3_Input{

		Opt_Help: false,

		Opt_OutPath: "",

		Opt_SchemaPath: "",
	}

	var arguments []string
	for idx, arg := range restArgs {
		if arg == "--" {
			arguments = append(arguments, restArgs[idx+1:]...)
			break
		}
		if !strings.HasPrefix(arg, "-") {
			arguments = append(arguments, arg)
			continue
		}
		optName, lit, cut := strings.Cut(arg, "=")
		consumeVariables(optName, lit, cut)

		switch optName {
		default:
			return fmt.Errorf("unknown option %q", optName)

		case "-help", "-h":
			if !cut {
				lit = "true"

			}
			if err := parseValue(&input.Opt_Help, lit); err != nil {
				return fmt.Errorf("value %q is not assignable to option %q", lit, optName)
			}

		case "-out-path":
			if !cut {
				return fmt.Errorf("value is not specified to option %q", optName)

			}
			if err := parseValue(&input.Opt_OutPath, lit); err != nil {
				return fmt.Errorf("value %q is not assignable to option %q", lit, optName)
			}

		case "-schema-path":
			if !cut {
				return fmt.Errorf("value is not specified to option %q", optName)

			}
			if err := parseValue(&input.Opt_SchemaPath, lit); err != nil {
				return fmt.Errorf("value %q is not assignable to option %q", lit, optName)
			}

		}
	}

	return nil
}

func NewCLI() CLI {
	return CLI{}
}

func Run(cli CLI, args []string) error {
	subcommandPath, restArgs := resolveSubcommand(args)
	switch strings.Join(subcommandPath, " ") {

	case "":
		funcMethod := cli.FUNC
		if funcMethod == nil {
			return fmt.Errorf("%q is unsupported: cli.FUNC not assigned", "")
		}
		var input CLI_Input
		err := resolve_CLI_Input(&input, restArgs)
		return funcMethod(subcommandPath, input, err)

	case "golang":
		funcMethod := cli.Golang.FUNC
		if funcMethod == nil {
			return fmt.Errorf("%q is unsupported: cli.Golang.FUNC not assigned", "golang")
		}
		var input CLI_Golang_Input
		err := resolve_CLI_Golang_Input(&input, restArgs)
		return funcMethod(subcommandPath, input, err)

	case "python3":
		funcMethod := cli.Python3.FUNC
		if funcMethod == nil {
			return fmt.Errorf("%q is unsupported: cli.Python3.FUNC not assigned", "python3")
		}
		var input CLI_Python3_Input
		err := resolve_CLI_Python3_Input(&input, restArgs)
		return funcMethod(subcommandPath, input, err)

	}
	return nil
}

func resolveSubcommand(args []string) (subcommandPath []string, restArgs []string) {
	if len(args) == 0 {
		panic("command line arguments are too few")
	}
	subcommandSet := map[string]bool{
		"":       true,
		"golang": true, "python3": true,
	}

	for _, arg := range args[1:] {
		if arg == "--" {
			break
		}
		pathLiteral := strings.Join(append(append([]string{}, subcommandPath...), arg), " ")
		if !subcommandSet[pathLiteral] {
			break
		}
		subcommandPath = append(subcommandPath, arg)
	}

	return subcommandPath, args[1+len(subcommandPath):]
}

func parseValue(dstPtr any, strValue ...string) error {
	switch dstPtr := dstPtr.(type) {
	case *[]bool:
		val := make([]bool, len(strValue))
		for idx, str := range strValue {
			if err := parseValue(&val[idx], str); err != nil {
				return fmt.Errorf("fail to parse %#v as []bool: %w", str, err)
			}
		}
		*dstPtr = val
	case *[]float64:
		val := make([]float64, len(strValue))
		for idx, str := range strValue {
			if err := parseValue(&val[idx], str); err != nil {
				return fmt.Errorf("fail to parse %#v as []float64: %w", str, err)
			}
		}
		*dstPtr = val
	case *[]int64:
		val := make([]int64, len(strValue))
		for idx, str := range strValue {
			if err := parseValue(&val[idx], str); err != nil {
				return fmt.Errorf("fail to parse %#v as []int64: %w", str, err)
			}
		}
		*dstPtr = val
	case *[]string:
		val := make([]string, len(strValue))
		for idx, str := range strValue {
			if err := parseValue(&val[idx], str); err != nil {
				return fmt.Errorf("fail to parse %#v as []string: %w", str, err)
			}
		}
		*dstPtr = val
	case *bool:
		val, err := strconv.ParseBool(strValue[0])
		if err != nil {
			return fmt.Errorf("fail to parse %q as bool: %w", strValue[0], err)
		}
		*dstPtr = val
	case *float64:
		val, err := strconv.ParseFloat(strValue[0], 64)
		if err != nil {
			return fmt.Errorf("fail to parse %q as float64: %w", strValue[0], err)
		}
		*dstPtr = val
	case *int64:
		val, err := strconv.ParseInt(strValue[0], 0, 64)
		if err != nil {
			return fmt.Errorf("fail to parse %q as int64: %w", strValue[0], err)
		}
		*dstPtr = val
	case *string:
		*dstPtr = strValue[0]
	}

	return nil
}

func consumeVariables(...any) {}
