from __future__ import annotations

__all__: list[str] = ["main", "test"]

import sys

from seqpad.tests import test


def main() -> int:
    return int(not seqpad.tests.test().wasSuccessful())


if __name__ == "__main__":
    main()
