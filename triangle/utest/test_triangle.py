"""Utests for :mod:`triangle`."""
import sys
import unittest
from pathlib import Path

# pylint: disable=wrong-import-position
sys.path.append(str(Path(__file__).resolve().parent / "../.."))
from triangle import TriangleProblem


class TestPlaceholder(unittest.TestCase):
    """Utests."""

    def test_placeholder(self):
        """Test default case."""
        tp = TriangleProblem()
        self.assertEqual(tp.solve(), 140)
