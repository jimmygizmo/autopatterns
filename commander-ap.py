#! /usr/bin/env python
import argparse

# TODO: This code is not quite correct. Argparse lib has changed since example.

# When a single root parser is defined, the below code works. It is when
# the commented-out subparser green/blue code is used that there is an error.
#     args.func(args)
#     ^^^^^^^^^
# AttributeError: 'Namespace' object has no attribute 'func'


def blue(function_args):
    print(f"Performing Blue command on target: {function_args.target}")


def green(function_args):
    print(f"Performing Green command on target: {function_args.target}")


parser = argparse.ArgumentParser()


# subparsers = parser.add_subparsers()

# blue_parser = subparsers.add_parser("blue")
# blue_parser.add_argument("target")
# blue_parser.set_defaults(func=blue)
#
# green_parser = subparsers.add_parser("green")
# green_parser.add_argument("target")
# green_parser.set_defaults(func=green)


# Option -v, --verbose
parser.add_argument("-v", "--verbose",
                    help="Verbose output.",
                    action="store_true",
                    )


# Required final argument, target of command: target
parser.add_argument("target",
                    help="The target of the specified command, a file path.",
                    )


# Conflicting options, such as a --quiet and a --verbose can be mutually-exclusive,
# by adding a special group to add these arguments too, like this:
# group = parser.add_mutually_exclusive_group()
# group.add_argument("-v", "--verbose", action="store_true")
# group.add_argument("-q", "--quiet", action="store_true")


# Help is always included: -h, --help
# Help can be global or if put after a command, you get command-specific help.


if __name__ == '__main__':
    args = parser.parse_args()
    # The following disabled line goes with the disabled subparser code (above).
    # args.func(args)
    if args.verbose:
        print("Output will be verbose.")
    print(args.target)

