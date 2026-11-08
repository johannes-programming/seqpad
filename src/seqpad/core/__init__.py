from __future__ import annotations

__all__: list[str] = ["main", "seqpad"]

from typing import Any

import click
import preparse


@preparse.PreParser().click()
@click.command(add_help_option=False)
@click.help_option("-h", "--help")
@click.version_option(None, "-V", "--version")
@click.argument("seq", type=str, required=False)
def main(seq: str | None) -> None:
    "This program pads the given seq to a length that is a multiple of three."
    if seq is not None:
        click.echo(seqpad(seq))


def seqpad(seq: Any) -> Any:
    while len(seq) % 3 != 0:
        seq += "N"
    return seq
