from __future__ import annotations

__all__: list[str] = ["main", "seqpad", "test"]

from seqpad.core import main, seqpad
from seqpad.tests import test

if __name__ == "__main__":
    main()
