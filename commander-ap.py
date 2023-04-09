#! /usr/bin/env python
import argparse

# Docs, specifically on sub-commands:
# https://docs.python.org/3/library/argparse.html#other-utilities


def blue(function_args):
    print(f"Performing Blue command on target: {function_args.target_blue}")


def green(function_args):
    print(f"Performing Green command on target: {function_args.target_green}")


parser = argparse.ArgumentParser(
    prog="Commander-AP",
    description="commander-ap.py is a demonstration of the argparse module.",
)


# https://docs.python.org/3/library/argparse.html#other-utilities

subparsers = parser.add_subparsers(help="sub-command help")

# Supply the name of the command, like this:  subparser.add_parser("command_name")

parser_blue = subparsers.add_parser("blue", help="blue command help")
parser_blue.add_argument("target_blue", help="target_blue help")
parser_blue.set_defaults(func=blue)

parser_green = subparsers.add_parser("green", help="green command help")
parser_green.add_argument("target_green", help="target_green help")
parser_green.set_defaults(func=green)


# Option -v, --verbose
parser.add_argument(
    "-v", "--verbose",
    help="Verbose output.",
    action="store_true",
)


# Probably won't use this global-level target when sub-commands are defining targets.
# Required final argument, target of command: target
# parser.add_argument(
#     "target",
#     help="The target of the specified command, a file path.",
# )


# Conflicting options, such as a --quiet and a --verbose can be mutually-exclusive,
# by adding a special group to add these arguments too, like this:
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")


# Help is always included: -h, --help
# Help can be global or if put after a command, you get command-specific help.


if __name__ == '__main__':
    args = parser.parse_args()
    args.func(args)
    # if args.verbose:
    #     print("Output will be verbose.")
    # print(args.target)

