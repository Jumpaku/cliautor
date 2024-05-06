# Code generated by cyamli v0.0.15, DO NOT EDIT.

from dataclasses import dataclass
from typing import TypeAlias
import typing


FuncTypeInput = typing.TypeVar('FuncTypeInput')
FuncType: TypeAlias = typing.Callable[[None,FuncTypeInput,Exception],None]


@dataclass
class CLI_List_Input:
    opt_config: str = ""
    
    
    pass


class CLI_List:
    
    desc_simple: str = "list tables\n\nUsage:\n    $ <program> list [<option>]...\n\nOptions:\n    -config\n\n"
    desc_detail: str = "list tables\n\nUsage:\n    $ <program> list [<option>]...\n\n\nOptions:\n    -config=<string>, -c=<string>  (default=\"\"):\n        path to config file\n\n"
    FUNC: FuncType[CLI_List_Input] = None


def resolve_CLI_List_Input(rest_args: list[str])->CLI_List_Input:
    input = CLI_List_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        match opt_name:
        
            case "-config" | "-c":
                if not assign:
                    raise Exception("value is not specified to option "+ opt_name)
                    
                input.opt_config = parse_value(str, split[1])
        
            case _:
                raise Exception("unsupported option " + opt_name)
    
    return input


@dataclass
class CLI_Fetch_Input:
    opt_config: str = ""
    opt_verbose: bool = False
    
    arg_tables: tuple[str,...] = tuple[str,...]()
    
    pass


class CLI_Fetch:
    
    desc_simple: str = "show information of tables\n\nUsage:\n    $ <program> fetch [<option>|<argument>]... [-- [<argument>]...]\n\nOptions:\n    -config, -verbose\n\nArguments:\n    <tables>...\n\n"
    desc_detail: str = "show information of tables\n\nUsage:\n    $ <program> fetch [<option>|<argument>]... [-- [<argument>]...]\n\n\nOptions:\n    -config=<string>, -c=<string>  (default=\"\"):\n        path to config file\n\n    -verbose[=<boolean>], -v[=<boolean>]  (default=false):\n        shows detailed log\n\n\nArguments:\n    [0:] [<tables:string>]...\n        names of tables to be described\n\n"
    FUNC: FuncType[CLI_Fetch_Input] = None


def resolve_CLI_Fetch_Input(rest_args: list[str])->CLI_Fetch_Input:
    input = CLI_Fetch_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        match opt_name:
        
            case "-config" | "-c":
                if not assign:
                    raise Exception("value is not specified to option "+ opt_name)
                    
                input.opt_config = parse_value(str, split[1])
        
            case "-verbose" | "-v":
                if not assign:
                    split.append("True")
                    
                input.opt_verbose = parse_value(bool, split[1])
        
            case _:
                raise Exception("unsupported option " + opt_name)
    if len(arguments) <= 0 - 1:
        raise Exception("too few arguments")
    input.arg_tables = parse_value(tuple[str,...], *arguments[0:])
    
    return input


@dataclass
class CLI_Input:
    
    
    pass


class CLI:
    list: CLI_List = CLI_List()
    fetch: CLI_Fetch = CLI_Fetch()
    
    desc_simple: str = "demo:\ndemo app to get table information from databases\n\nUsage:\n    $ demo\n\nSubcommands:\n    fetch, list\n\n"
    desc_detail: str = "demo:\ndemo app to get table information from databases\n\nUsage:\n    $ demo\n\n\nSubcommands:\n    fetch:\n        show information of tables\n\n    list:\n        list tables\n\n"
    FUNC: FuncType[CLI_Input] = None


def resolve_CLI_Input(rest_args: list[str])->CLI_Input:
    input = CLI_Input()
    arguments = []
    for i, arg in enumerate(rest_args):
        if arg == "--":
            arguments += rest_args[i+1:]
            break
        if not arg.startswith("-"):
            arguments.append(arg)
            continue
        split = arg.split("=", 1)
        opt_name, assign = split[0], len(split) > 1
        match opt_name:
        
            case _:
                raise Exception("unsupported option " + opt_name)
    
    return input


def run(cli: CLI, args: list[str]):
    r = resolve_subcommand(args)
    subcommand_path, rest_args = r.subcommand, r.rest_args
    match " ".join(subcommand_path):
    
        case "":
            if not cli.FUNC:
                raise Exception("unsupported subcommand \"" + "" + "\": cli.FUNC not assigned")
            ex: Exception = None
            input: CLI_Input = None
            try:
                input = resolve_CLI_Input(rest_args)
            except Exception as e:
                ex = e
            cli.FUNC(input, ex)
    
    
        case "list":
            if not cli.list.FUNC:
                raise Exception("unsupported subcommand \"" + "list" + "\": cli.list.FUNC not assigned")
            ex: Exception = None
            input: CLI_List_Input = None
            try:
                input = resolve_CLI_List_Input(rest_args)
            except Exception as e:
                ex = e
            cli.list.FUNC(input, ex)
    
        case "fetch":
            if not cli.fetch.FUNC:
                raise Exception("unsupported subcommand \"" + "fetch" + "\": cli.fetch.FUNC not assigned")
            ex: Exception = None
            input: CLI_Fetch_Input = None
            try:
                input = resolve_CLI_Fetch_Input(rest_args)
            except Exception as e:
                ex = e
            cli.fetch.FUNC(input, ex)
    

@dataclass
class ResolveSubcommandResult:
    subcommand: list[str]
    rest_args: list[str]


def resolve_subcommand(args: list[str])->ResolveSubcommandResult:
    if not args:
        raise Exception("command line arguments are too few")
    
    subcommand_set = {
        "",
        "list","fetch",
    }

    subcommand_path = []
    for arg in args[1:]:
        if arg == "--":
            break
        if " ".join(subcommand_path + [arg]) not in subcommand_set:
            break
        subcommand_path.append(arg)
    
    return ResolveSubcommandResult(subcommand_path, args[1+len(subcommand_path):])


def parse_value(typ, *strValues: str) -> str | bool | float | int | tuple[str,...] | tuple[bool,...] | tuple[float,...] | tuple[int,...]:
    try: 
        if typ == str:
            return str(strValues[0])
        if typ == bool:
            if strValues[0] in {"", "0", "f", "F", "FALSE", "false", "False"}:
                return False
            if strValues[0] in {"1", "t", "T", "TRUE", "true", "True"}:
                return True
            raise Exception("could not convert string to bool: '" + strValues[0] + "'")
        if typ == float:
            return float(strValues[0])
        if typ == int:
            return int(strValues[0], base=0)
        if typ == tuple[str,...]:
            return tuple([parse_value(str, s) for s in strValues])
        if typ == tuple[bool,...]:
            return tuple([parse_value(bool, s) for s in strValues])
        if typ == tuple[float,...]:
            return tuple([parse_value(float, s) for s in strValues])
        if typ == tuple[int,...]:
            return tuple([parse_value(int, s) for s in strValues])
        raise Exception("unsupported type")
    except Exception as e:
        e.add_note('fail to parse string value as ' + typ.__name__)
        raise
