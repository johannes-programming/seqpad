from typing import *

import click
import preparse

__all__ = ["seqpad", "main"]


def seqpad(seq: Any) -> Any:
    while len(seq) % 3 != 0:
        seq += "N"
    return seq


@preparse.PreParser().click()
@click.command(add_help_option=False)
@click.help_option("-h", "--help")
@click.version_option(None, "-V", "--version")
@click.argument("seq", type=str, required=False)
def main(seq: Optional[str]) -> None:
    "This program pads the given seq to a length that is a multiple of three."
    if seq is not None:
        click.echo(seqpad(seq))
