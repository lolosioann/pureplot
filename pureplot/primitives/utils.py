from __future__ import annotations

from typing import Any

import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from numpy.typing import ArrayLike

from ..policy import create_figure, get_color_cycle, get_default_style


def validate_xy(x: ArrayLike, y: ArrayLike) -> tuple[np.ndarray, np.ndarray]:
    """Validate and convert x/y inputs to numpy arrays."""
    x_arr = np.asarray(x)
    y_arr = np.asarray(y)

    if x_arr.shape != y_arr.shape:
        raise ValueError(
            f"x and y must have same shape: {x_arr.shape} != {y_arr.shape}"
        )

    if x_arr.ndim != 1:
        raise ValueError("x and y must be 1D arrays")

    return x_arr, y_arr


def make_figure_and_axes(
    *,
    figsize: tuple[float, float] | None,
) -> tuple[Figure, Axes, dict[str, Any], list[str]]:
    """Create figure and axes with policy-applied styling."""
    style = get_default_style()
    colors = list(get_color_cycle(12))

    fig = create_figure(figsize=figsize)
    ax = fig.add_subplot(111)
    ax.set_facecolor(style["axes.facecolor"])

    if style["axes.grid"]:
        ax.grid(
            True,
            color=style["grid.color"],
            linestyle=style["grid.linestyle"],
            linewidth=style["grid.linewidth"],
            alpha=style["grid.alpha"],
        )
        ax.set_axisbelow(style["axes.axisbelow"])

    return fig, ax, style, colors
