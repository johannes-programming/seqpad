from __future__ import annotations

__all__: list[str] = ["main", "parse_args", "run", "seqpad"]

import argparse
import logging
from collections import abc
from importlib import metadata
from typing import TypeVar

from seqpad.typing.SizedAndSupportsAdd import SizedAndSupportsAdd

Seq = TypeVar("Seq", bound=SizedAndSupportsAdd[str])


def main(args: abc.Iterable[str] | None = None) -> int:
    space: argparse.Namespace
    try:
        space = parse_args(args)
    except SystemExit as exit:
        if isinstance(exit.code, int):
            return exit.code
        else:
            return int(bool(exit.code))
    try:
        run(space.seq)
    except Exception as exc:
        logging.exception(exc)
        return 1
    return 0


def parse_args(args: abc.Iterable[str] | None = None) -> argparse.Namespace:
    parser: argparse.ArgumentParser
    version: str
    parser = argparse.ArgumentParser(
        add_help=False,
        fromfile_prefix_chars="@",
        prog="seqpad",
    )
    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="show this help message and exit",
    )
    version = "%(prog)s, version " + metadata.version("seqpad")
    parser.add_argument("-V", "--version", action="version", version=version)
    parser.add_argument("seq", nargs="?")
    return parser.parse_args(args)


def run(seq: str | None = None) -> None:
    if seq is not None:
        print(seqpad(seq))


def seqpad(seq: Seq) -> Seq:
    while len(seq) % 3 != 0:
        seq = seq + "N"
    return seq
