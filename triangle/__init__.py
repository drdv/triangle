"""Module interface."""
try:
    from ._version import __version__
except ModuleNotFoundError:
    __version__ = "unknown (package not installed)"

from triangle.problem import TriangleProblem
