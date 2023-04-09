#! /usr/bin/env python
import click


@click.group()
def entry():
    pass


@entry.command()
@click.argument('target')  # add the name argument
def blue(**kwargs):
    print(f"Performing Blue command on target: {kwargs['target']}")


@entry.command()
@click.argument('target')  # add the name argument
def green(**kwargs):
    print(f"Performing Green command on target: {kwargs['target']}")


if __name__ == '__main__':
    entry()


# Out of the box, click does not support -h, only --help.

