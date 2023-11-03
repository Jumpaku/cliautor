package data

import (
	"cliautor/name"
	"fmt"
)

type Command struct {
	Name        name.Path
	Description string
	Options     []Option
	Arguments   []Argument
	Subcommands []Subcommand
}

func (d Command) NameLiteral() string {
	return fmt.Sprintf("%q", d.Name.Join(" ", "", ""))
}

func (d Command) CLIStructName() string {
	return d.Name.Map(name.Title).Join("", "CLI_", "")
}

func (d Command) CLIInputStructName() string {
	return d.Name.Map(name.Title).Join("", "CLI_", "_Input")
}

func (d Command) CLIFuncMethodChain() string {
	return d.Name.Map(func(s string) string {
		return "Sub_" + name.Title(s)
	}).Join(".", "", ".Func")
}

func (d Command) DescriptionLiteral() string {
	return fmt.Sprintf("%q", d.Description)
}
