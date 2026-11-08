from __future__ import annotations

__all__: list[str] = ["test"]

import unittest


def test() -> unittest.TextTestResult:
    loader: unittest.TestLoader
    runner: unittest.TextTestRunner
    tests: unittest.TestSuite
    loader = unittest.TestLoader()
    tests = loader.discover(start_dir="seqpad.tests")
    runner = unittest.TextTestRunner()
    return runner.run(tests)
