# primitives/line.py

from typing import Any

import numpy as np
from matplotlib.axes import Axes
from matplotlib.lines import Line2D
from numpy.typing import ArrayLike

from .interface import DrawResult, plot_template
from .result import PlotResult


def _draw_line(
    ax: Axes,
    x: np.ndarray,
    y: np.ndarray,
    style: dict[str, Any],
    colors: list[str],
    *,
    color: str | None,
    linewidth: float,
    alpha: float,
    **kwargs: Any,
) -> DrawResult:
    """Draw line plot on axes."""
    plot_color = color if color is not None else colors[0]

    handle: Line2D = ax.plot(
        x,
        y,
        color=plot_color,
        linewidth=linewidth,
        alpha=alpha,
        **kwargs,
    )[0]

    return handle, plot_color


def line(
    x: ArrayLike,
    y: ArrayLike,
    *,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    color: str | None = None,
    linewidth: float = 2.0,
    alpha: float = 1.0,
    figsize: tuple[float, float] | None = None,
    **kwargs: Any,
) -> PlotResult:
    """Create a line plot."""
    return plot_template(
        _draw_line,
        x=x,
        y=y,
        title=title,
        xlabel=xlabel,
        ylabel=ylabel,
        figsize=figsize,
        color=color,
        linewidth=linewidth,
        alpha=alpha,
        **kwargs,
    )
