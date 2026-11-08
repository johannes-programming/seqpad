from __future__ import annotations

__all__: list[str] = ["main", "parse_args", "run", "seqpad", "test"]

import sys

from seqpad.core import main, parse_args, run, seqpad
from seqpad.tests import test

if __name__ == "__main__":
    sys.exit(main())
