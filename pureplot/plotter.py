"""
Singleton class for plotting graphs using matplotlib.

Responsibilities:
- Holds current policy snapshot
- Exposes read only views to primitives
- Owns Context manager factories

- No drawing
- No figure creation
- No data manipulation
"""

from __future__ import annotations

from typing import Optional

from .context import PlotContext
from .policy import PolicySnapshot

__PLOTTER: Optional["Plotter"] = None


class Plotter:
    """
    Singleton access point for plotting configuration.

    Responsibilities:
    - Expose read-only policy snapshots
    - Provide Context manager factories

    Forbidden:
    - Drawing
    - Figure / Axes creation
    - Global mutation
    """

    def __init__(self) -> None:
        self._policy = PolicySnapshot.capture()

    # ---- read-only policy access ----

    @property
    def policy(self) -> PolicySnapshot:
        """
        Immutable snapshot of current plotting policy.
        """
        return self._policy

    # ---- context factories ----

    def context(self, **overrides) -> PlotContext:
        """
        Create a mutation context with temporary overrides.

        No drawing allowed inside this class.
        """
        return PlotContext(overrides)


def get_plotter() -> Plotter:
    global __PLOTTER
    if __PLOTTER is None:
        __PLOTTER = Plotter()
    return __PLOTTER
