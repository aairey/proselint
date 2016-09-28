"""Tests for misc.suddenly check."""
from __future__ import absolute_import

from .check import Check

from proselint.checks.misc import suddenly as chk


class TestCheck(Check):
    """The test class for misc.suddenly."""

    __test__ = True

    @property
    def this_check(self):
        """Bolierplate."""
        return chk

    def test_smoke(self):
        """Basic smoke test for misc.suddenly."""
        assert self.passes("""Smoke phrase with nothing flagged.""")
        assert not self.passes("""Suddenly, it all made sense.""")
