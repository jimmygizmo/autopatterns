#! /usr/bin/env python
import click


@click.group()
def entry():
    pass


@entry.command()
def blue(**kwargs):
    pass


@entry.command()
def green(**kwargs):
    pass


if __name__ == '__main__':
    entry()

