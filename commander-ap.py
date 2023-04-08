#! /usr/bin/env python
import argparse


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers()

green_parser = subparsers.add_parser('green')
blue_parser = subparsers.add_parser('blue')


if __name__ == '__main__':
    args = parser.parse_args()

