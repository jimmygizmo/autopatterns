#! /usr/bin/env python
"""Commander.

Usage:
  commander.py blue
  commander.py green
  commander.py -h | --help

Options:
  -h --help     Show this screen.
"""
from docopt import docopt


if __name__ == '__main__':
    arguments = docopt(__doc__)

