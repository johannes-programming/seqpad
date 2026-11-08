from __future__ import annotations

__all__: list[str] = []

import sys

import seqpad.tests

sys.exit(1 - seqpad.tests.test().wasSuccessful())
