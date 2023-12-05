
# Code generated by cyamli v0.0.10, DO NOT EDIT.
from dataclasses import dataclass
from typing import TypeAlias
import typing
FuncTypeInput = typing.TypeVar('FuncTypeInput')
FuncType: TypeAlias = typing.Callable[[None,FuncTypeInput,Exception],None]

@dataclass
class CLI_Sub3Subd_Input:
    arg_arg_v: tuple[str,...] = tuple[str,...]()

class CLI_Sub3Subd:
    FUNC: FuncType[CLI_Sub3Subd_Input] = None
def resolve_CLI_Sub3Subd_Input(rest_args: list[str])->CLI_Sub3Subd_Input:
    input = CLI_Sub3Subd_Input()
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
    if len(arguments) <= 0 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[str,...], arguments[0:])
    return input

@dataclass
class CLI_Sub3Subc_Input:
    arg_arg_v: tuple[float,...] = tuple[float,...]()

class CLI_Sub3Subc:
    FUNC: FuncType[CLI_Sub3Subc_Input] = None
def resolve_CLI_Sub3Subc_Input(rest_args: list[str])->CLI_Sub3Subc_Input:
    input = CLI_Sub3Subc_Input()
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
    if len(arguments) <= 0 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[float,...], arguments[0:])
    return input

@dataclass
class CLI_Sub3Subb_Input:
    arg_arg_v: tuple[int,...] = tuple[int,...]()

class CLI_Sub3Subb:
    FUNC: FuncType[CLI_Sub3Subb_Input] = None
def resolve_CLI_Sub3Subb_Input(rest_args: list[str])->CLI_Sub3Subb_Input:
    input = CLI_Sub3Subb_Input()
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
    if len(arguments) <= 0 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[int,...], arguments[0:])
    return input

@dataclass
class CLI_Sub3Suba_Input:
    arg_arg_v: tuple[bool,...] = tuple[bool,...]()

class CLI_Sub3Suba:
    FUNC: FuncType[CLI_Sub3Suba_Input] = None
def resolve_CLI_Sub3Suba_Input(rest_args: list[str])->CLI_Sub3Suba_Input:
    input = CLI_Sub3Suba_Input()
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
    if len(arguments) <= 0 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[bool,...], arguments[0:])
    return input

@dataclass
class CLI_Sub3_Input:
    opt_option_a: str = "abc"
    opt_option_b: int = int(-123)
    opt_option_c: bool = True
    opt_option_d: float = float(-123.456)
    opt_option_e: str = ""
    arg_arg_a: str = str()
    arg_arg_b: int = int()
    arg_arg_c: bool = bool()
    arg_arg_d: float = float()
    arg_arg_e: str = str()
    arg_arg_v: tuple[str,...] = tuple[str,...]()

class CLI_Sub3:
    subd: CLI_Sub3Subd = CLI_Sub3Subd()
    subc: CLI_Sub3Subc = CLI_Sub3Subc()
    subb: CLI_Sub3Subb = CLI_Sub3Subb()
    suba: CLI_Sub3Suba = CLI_Sub3Suba()
    FUNC: FuncType[CLI_Sub3_Input] = None
def resolve_CLI_Sub3_Input(rest_args: list[str])->CLI_Sub3_Input:
    input = CLI_Sub3_Input()
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
            case "-option-a" | "-a":
                if not assign:
                    raise Exception("value is not specified to option "+ opt_name)
                input.opt_option_a = parse_value(str, split[1])
            case "-option-b" | "-b":
                if not assign:
                    raise Exception("value is not specified to option "+ opt_name)
                input.opt_option_b = parse_value(int, split[1])
            case "-option-c" | "-c":
                if not assign:
                    split[1] = "True"
                input.opt_option_c = parse_value(bool, split[1])
            case "-option-d" | "-d":
                if not assign:
                    raise Exception("value is not specified to option "+ opt_name)
                input.opt_option_d = parse_value(float, split[1])
            case "-option-e":
                if not assign:
                    raise Exception("value is not specified to option "+ opt_name)
                input.opt_option_e = parse_value(str, split[1])
            case _:
                raise Exception("unsupported option " + opt_name)
    if len(arguments) <= 0:
        raise Exception("too few arguments")
    input.arg_arg_a = parse_value(str, arguments[0])

    if len(arguments) <= 1:
        raise Exception("too few arguments")
    input.arg_arg_b = parse_value(int, arguments[1])

    if len(arguments) <= 2:
        raise Exception("too few arguments")
    input.arg_arg_c = parse_value(bool, arguments[2])

    if len(arguments) <= 3:
        raise Exception("too few arguments")
    input.arg_arg_d = parse_value(float, arguments[3])

    if len(arguments) <= 4:
        raise Exception("too few arguments")
    input.arg_arg_e = parse_value(str, arguments[4])

    if len(arguments) <= 5 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[str,...], arguments[5:])
    return input

@dataclass
class CLI_Sub2_Input:
    pass
class CLI_Sub2:
    FUNC: FuncType[CLI_Sub2_Input] = None
def resolve_CLI_Sub2_Input(rest_args: list[str])->CLI_Sub2_Input:
    input = CLI_Sub2_Input()
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

@dataclass
class CLI_Sub1_Input:
    pass
class CLI_Sub1:
    FUNC: FuncType[CLI_Sub1_Input] = None
def resolve_CLI_Sub1_Input(rest_args: list[str])->CLI_Sub1_Input:
    input = CLI_Sub1_Input()
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

@dataclass
class CLI_Input:
    opt_option_a: str = "abc"
    opt_option_b: int = int(-123)
    opt_option_c: bool = True
    opt_option_d: float = float(-123.456)
    opt_option_e: str = ""
    arg_arg_a: str = str()
    arg_arg_b: int = int()
    arg_arg_c: bool = bool()
    arg_arg_d: float = float()
    arg_arg_e: str = str()
    arg_arg_v: tuple[str,...] = tuple[str,...]()

class CLI:
    sub3: CLI_Sub3 = CLI_Sub3()
    sub2: CLI_Sub2 = CLI_Sub2()
    sub1: CLI_Sub1 = CLI_Sub1()
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
            case "-option-a" | "-a":
                if not assign:
                    raise Exception("value is not specified to option "+ opt_name)
                input.opt_option_a = parse_value(str, split[1])
            case "-option-b" | "-b":
                if not assign:
                    raise Exception("value is not specified to option "+ opt_name)
                input.opt_option_b = parse_value(int, split[1])
            case "-option-c" | "-c":
                if not assign:
                    split[1] = "True"
                input.opt_option_c = parse_value(bool, split[1])
            case "-option-d" | "-d":
                if not assign:
                    raise Exception("value is not specified to option "+ opt_name)
                input.opt_option_d = parse_value(float, split[1])
            case "-option-e":
                if not assign:
                    raise Exception("value is not specified to option "+ opt_name)
                input.opt_option_e = parse_value(str, split[1])
            case _:
                raise Exception("unsupported option " + opt_name)
    if len(arguments) <= 0:
        raise Exception("too few arguments")
    input.arg_arg_a = parse_value(str, arguments[0])

    if len(arguments) <= 1:
        raise Exception("too few arguments")
    input.arg_arg_b = parse_value(int, arguments[1])

    if len(arguments) <= 2:
        raise Exception("too few arguments")
    input.arg_arg_c = parse_value(bool, arguments[2])

    if len(arguments) <= 3:
        raise Exception("too few arguments")
    input.arg_arg_d = parse_value(float, arguments[3])

    if len(arguments) <= 4:
        raise Exception("too few arguments")
    input.arg_arg_e = parse_value(str, arguments[4])

    if len(arguments) <= 5 - 1:
        raise Exception("too few arguments")
    input.arg_arg_v = parse_value(tuple[str,...], arguments[5:])
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
        case "sub3 subd":
            if not cli.sub3.subd.FUNC:
                raise Exception("unsupported subcommand \"" + "sub3 subd" + "\": cli.sub3.subd.FUNC not assigned")
            ex: Exception = None
            input: CLI_Sub3Subd_Input = None
            try:
                input = resolve_CLI_Sub3Subd_Input(rest_args)
            except Exception as e:
                ex = e
            cli.sub3.subd.FUNC(input, ex)
        case "sub3 subc":
            if not cli.sub3.subc.FUNC:
                raise Exception("unsupported subcommand \"" + "sub3 subc" + "\": cli.sub3.subc.FUNC not assigned")
            ex: Exception = None
            input: CLI_Sub3Subc_Input = None
            try:
                input = resolve_CLI_Sub3Subc_Input(rest_args)
            except Exception as e:
                ex = e
            cli.sub3.subc.FUNC(input, ex)
        case "sub3 subb":
            if not cli.sub3.subb.FUNC:
                raise Exception("unsupported subcommand \"" + "sub3 subb" + "\": cli.sub3.subb.FUNC not assigned")
            ex: Exception = None
            input: CLI_Sub3Subb_Input = None
            try:
                input = resolve_CLI_Sub3Subb_Input(rest_args)
            except Exception as e:
                ex = e
            cli.sub3.subb.FUNC(input, ex)
        case "sub3 suba":
            if not cli.sub3.suba.FUNC:
                raise Exception("unsupported subcommand \"" + "sub3 suba" + "\": cli.sub3.suba.FUNC not assigned")
            ex: Exception = None
            input: CLI_Sub3Suba_Input = None
            try:
                input = resolve_CLI_Sub3Suba_Input(rest_args)
            except Exception as e:
                ex = e
            cli.sub3.suba.FUNC(input, ex)
        case "sub3":
            if not cli.sub3.FUNC:
                raise Exception("unsupported subcommand \"" + "sub3" + "\": cli.sub3.FUNC not assigned")
            ex: Exception = None
            input: CLI_Sub3_Input = None
            try:
                input = resolve_CLI_Sub3_Input(rest_args)
            except Exception as e:
                ex = e
            cli.sub3.FUNC(input, ex)
        case "sub2":
            if not cli.sub2.FUNC:
                raise Exception("unsupported subcommand \"" + "sub2" + "\": cli.sub2.FUNC not assigned")
            ex: Exception = None
            input: CLI_Sub2_Input = None
            try:
                input = resolve_CLI_Sub2_Input(rest_args)
            except Exception as e:
                ex = e
            cli.sub2.FUNC(input, ex)
        case "sub1":
            if not cli.sub1.FUNC:
                raise Exception("unsupported subcommand \"" + "sub1" + "\": cli.sub1.FUNC not assigned")
            ex: Exception = None
            input: CLI_Sub1_Input = None
            try:
                input = resolve_CLI_Sub1_Input(rest_args)
            except Exception as e:
                ex = e
            cli.sub1.FUNC(input, ex)
@dataclass
class ResolveSubcommandResult:
    subcommand: list[str]
    rest_args: list[str]
def resolve_subcommand(args: list[str])->ResolveSubcommandResult:
    if not args:
        raise Exception("command line arguments are too few")
    subcommand_set = {
        "",
        "sub3 subd","sub3 subc","sub3 subb","sub3 suba","sub3","sub2","sub1",
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
            return bool(strValues[0])
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