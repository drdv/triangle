"""Triangle problem."""
import matplotlib.pyplot as plt
import numpy as np


class Point:
    """Point with (x,y) coordinates."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class TriangleProblem:
    """Defines the triangle problem."""

    def __init__(self, a1=10, a2=30, b1=20, b2=20):
        """Initialize problem instance.

        Parameters
        -----------
        a1 : :obj:`float`
            Angle ``alpha_1`` in degrees.
        a2 : :obj:`float`
            Angle ``alpha_2`` in degrees.
        b1 : :obj:`float`
            Angle ``beta_1`` in degrees.
        b2 : :obj:`float`
            Angle ``beta_2`` in degrees.

        """
        self.a1, self.a2 = self.deg2rad(a1), self.deg2rad(a2)
        self.b1, self.b2 = self.deg2rad(b1), self.deg2rad(b2)

    def solve(self):
        """Solve problem.

        Returns
        --------
        :obj:`float`
            Angle ``x`` in degrees.

        """
        z = np.sin(self.a1) / np.sin(self.b1) * np.sin(self.b2) / np.sin(self.a2)
        v = np.pi - (self.a1 + self.a2 + self.b1 + self.b2)
        c1 = z * np.sin(v)
        c2 = z * np.cos(v)

        gamma2 = np.arctan2(c1, 1 + c2)
        x = np.pi - (self.b2 + gamma2)

        return x * 180 / np.pi

    @staticmethod
    def deg2rad(deg):
        """Convert degrees to radians."""
        return deg * np.pi / 180

    def plot(self, verbose=False, savefig=None):
        """Plot problem.

        Parameters
        -----------
        verbose : :obj:`bool`
            Add verbose annotation.
        savefig : :obj:`str` or ``None``
            Name of figure to save.

        """
        AB = 1  # can be chosen arbitrarily (for the visualization)
        v = np.pi - (self.a1 + self.a2 + self.b1 + self.b2)
        AC = AB * np.sin(self.b1 + self.b2) / np.sin(v)
        C = Point(np.cos(self.a1 + self.a2) * AC, np.sin(self.a1 + self.a2) * AC)

        # the intersection point in the interior
        AM = AB * np.sin(self.b1) / np.sin(np.pi - (self.a1 + self.b1))
        M = Point(np.cos(self.a1) * AM, np.sin(self.a1) * AM)

        plt.plot([0, AB, C.x, 0], [0, 0, C.y, 0])
        plt.plot([0], [0], "bs")
        plt.plot([AB], [0], "bs")
        plt.plot([C.x], [C.y], "bs")

        plt.plot(M.x, M.y, "rs")
        plt.plot([0, M.x, AB], [0, M.y, 0], "r--")
        plt.plot([M.x, C.x], [M.y, C.y], "r--")

        self._annotate(C, M, verbose=verbose)
        plt.axis("off")
        if savefig is not None:
            plt.savefig(savefig)

    def _annotate(self, C, M, verbose=False, fontsize=16):
        """Annotate figure."""
        # vertices
        plt.text(-0.05, -0.03, "$A$", fontsize=fontsize)
        plt.text(1.02, -0.03, "$B$", fontsize=fontsize)
        plt.text(C.x, C.y + 0.02, "$C$", fontsize=fontsize)
        plt.text(M.x - 0.065, M.y, "$M$", fontsize=fontsize)

        if verbose:
            # angles
            plt.text(0.17, 0.008, "$\\alpha_1$", fontsize=fontsize)
            plt.text(0.08, 0.04, "$\\alpha_2$", fontsize=fontsize)
            plt.text(0.83, 0.015, "$\\beta_1$", fontsize=fontsize)
            plt.text(0.83, 0.08, "$\\beta_2$", fontsize=fontsize)
            plt.text(0.46, 0.37, "$\\gamma_1$", fontsize=fontsize)
            plt.text(0.56, 0.32, "$\\gamma_2$", fontsize=fontsize)

            # lengths of line segments
            plt.text(0.35, 0.08, "$s_1$", fontsize=fontsize)
            plt.text(0.71, 0.07, "$s_2$", fontsize=fontsize)
            plt.text(0.53, 0.25, "$s_3$", fontsize=fontsize)

            # unknown angle
            plt.text(0.7, 0.125, "$x$", fontsize=fontsize)
