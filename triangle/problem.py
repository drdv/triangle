"""Triangle problem."""
import matplotlib.pyplot as plt
import numpy as np


class Point:
    """Point with (x,y) coordinates."""

    def __init__(self, x, y):
        self.x, self.y = x, y

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
            Unknown angle (in degrees).

        """
        z = np.sin(self.a1) / np.sin(self.b1) * np.sin(self.b2) / np.sin(self.a2)
        v = np.pi - (self.a1 + self.a2 + self.b1 + self.b2)
        c1 = z * np.sin(v)
        c2 = z * np.cos(v)

        gamma_2 = np.arctan2(c1, 1 + c2)
        x = np.pi - (self.b2 + gamma_2)

        return x * 180 / np.pi

    @staticmethod
    def deg2rad(deg):
        """Convert degrees to radians."""
        return deg * np.pi / 180

    def plot(self, ax=None, solve=False, annotate=False, savefig=None):
        """Plot problem.

        Parameters
        -----------
        ax : :obj:`AxesSubplot`
            Axix where to plot.
        solve : :obj:`bool`
            Show solution or not.
        annotate : :obj:`bool`
            Add annotation (for default case only).
        savefig : :obj:`str` or ``None``
            Name of figure to save.

        """
        if ax is None:
            _, ax = plt.subplots()

        A, B, C, M = self._get_points()
        ax.plot([A.x, B.x, C.x, 0], [A.y, B.y, C.y, 0])
        ax.plot(A.x, A.y, "bs")
        ax.plot(B.x, B.y, "bs")
        ax.plot(C.x, C.y, "bs")
        ax.plot(M.x, M.y, "rs")
        ax.plot([A.x, M.x, B.x], [A.y, M.y, B.y], "r--")
        ax.plot([M.x, C.x], [M.y, C.y], "r--")

        if annotate:
            self._annotate(ax)

        if solve:
            ax.text(C.x, 1.05 * C.y, f"$x: {self.solve():0.1f}$")

        ax.axis("off")
        if savefig is not None:
            plt.savefig(savefig)

    def _get_points(self):
        a = self.a1 + self.a2
        b = self.b1 + self.b2
        v = np.pi - (a + b)

        AB = 1  # arbitrary
        AC = AB * np.sin(b) / np.sin(v)
        AM = AB * np.sin(self.b1) / np.sin(np.pi - (self.a1 + self.b1))

        A = Point(0, 0)
        B = Point(AB, 0)
        C = Point(AC * np.cos(a), AC * np.sin(a))
        M = Point(AM * np.cos(self.a1), AM * np.sin(self.a1))

        return A, B, C, M

    def _annotate(self, ax):
        """Annotate figure for default angles only.

        Warning
        --------
        default angles: a1=10, a2=30, b1=20, b2=20.

        """
        fontsize = 16

        # vertices
        ax.text(-0.05, -0.03, "$A$", fontsize=fontsize)
        ax.text(1.02, -0.03, "$B$", fontsize=fontsize)
        ax.text(0.5, 0.44, "$C$", fontsize=fontsize)
        ax.text(0.61, 0.118, "$M$", fontsize=fontsize)

        # angles
        ax.text(0.17, 0.008, "$\\alpha_1$", fontsize=fontsize)
        ax.text(0.08, 0.04, "$\\alpha_2$", fontsize=fontsize)
        ax.text(0.83, 0.015, "$\\beta_1$", fontsize=fontsize)
        ax.text(0.83, 0.08, "$\\beta_2$", fontsize=fontsize)
        ax.text(0.46, 0.37, "$\\gamma_1$", fontsize=fontsize)
        ax.text(0.56, 0.32, "$\\gamma_2$", fontsize=fontsize)

        # lengths of line segments
        ax.text(0.35, 0.08, "$s_1$", fontsize=fontsize)
        ax.text(0.71, 0.07, "$s_2$", fontsize=fontsize)
        ax.text(0.53, 0.25, "$s_3$", fontsize=fontsize)

        # unknown angle
        ax.text(0.7, 0.125, "$x$", fontsize=fontsize)
