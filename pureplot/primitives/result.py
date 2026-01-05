"""Plot result dataclass for returning structured outputs."""

from dataclasses import dataclass
from typing import Any

from matplotlib.axes import Axes
from matplotlib.figure import Figure


@dataclass(frozen=True)
class PlotResult:
    """Immutable result from a plotting function.

    Attributes:
        fig: Matplotlib Figure object
        ax: Matplotlib Axes object
        handles: Artist objects created by the plot (lines, scatter points, etc)
        metadata: Additional plot-specific information
    """

    fig: Figure
    ax: Axes
    handles: tuple[Any, ...]
    metadata: dict[str, Any]
