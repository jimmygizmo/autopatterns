#! /usr/bin/env python
"""Commander.

Usage:
  commander-do.py blue <target>
  commander-do.py green <target>
  commander-do.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt


def blue(target):
    print(f"Performing Blue command on target: {target}")


def green(target):
    print(f"Performing Green command on target: {target}")


if __name__ == '__main__':
    arguments = docopt(__doc__)

    # if an argument called blue was passed, execute the blue logic.
    if arguments["blue"]:
        blue(arguments["<target>"])
    elif arguments["green"]:
        green(arguments["<target>"])

