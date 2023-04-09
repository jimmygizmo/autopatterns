#! /usr/bin/env python
import argparse

# TODO: This code is not quite correct. Argparse lib has changed since example.

# When a single root parser is defined, the below code works. It is when
# the commented-out subparser green/blue code is used that there is an error.
#     args.func(args)
#     ^^^^^^^^^
# AttributeError: 'Namespace' object has no attribute 'func'


def blue(args):
    print(f"Performing Blue command on target: {args.target}")


def green(args):
    print(f"Performing Green command on target: {args.target}")


parser = argparse.ArgumentParser()
# subparsers = parser.add_subparsers()

# blue_parser = subparsers.add_parser("blue")
# blue_parser.add_argument("target")
# blue_parser.set_defaults(func=blue)
#
# green_parser = subparsers.add_parser("green")
# green_parser.add_argument("target")
# green_parser.set_defaults(func=green)

parser.add_argument("target")


if __name__ == '__main__':
    args = parser.parse_args()
    # args.func(args)
    print(args.target)

