# primitives/interface.py

from collections.abc import Callable
from typing import Any

import numpy as np
from matplotlib.axes import Axes
from numpy.typing import ArrayLike

from .result import PlotResult
from .utils import make_figure_and_axes, validate_xy

DrawResult = tuple[Any, str]  # (handle, color_used)


def plot_template(
    draw_fn: Callable[
        [Axes, np.ndarray, np.ndarray, dict[str, Any], list[str]],
        DrawResult,
    ],
    *,
    x: ArrayLike,
    y: ArrayLike,
    title: str | None,
    xlabel: str | None,
    ylabel: str | None,
    figsize: tuple[float, float] | None,
    **draw_kwargs: Any,
) -> PlotResult:
    """
    Canonical plotting lifecycle.

    Responsibilities:
    - validate inputs
    - create figure / axes
    - query style policy
    - delegate drawing
    - apply common styling
    - return PlotResult

    Forbidden:
    - rcParams mutation
    - backend switching
    """

    x_arr, y_arr = validate_xy(x, y)
    fig, ax, style, colors = make_figure_and_axes(figsize=figsize)

    handle, color_used = draw_fn(
        ax,
        x_arr,
        y_arr,
        style,
        colors,
        **draw_kwargs,
    )

    if title:
        ax.set_title(
            title,
            color=style["text.color"],
            fontsize=style["font.size"] + 2,
        )
    if xlabel:
        ax.set_xlabel(
            xlabel,
            color=style["axes.labelcolor"],
            fontsize=style["font.size"],
        )
    if ylabel:
        ax.set_ylabel(
            ylabel,
            color=style["axes.labelcolor"],
            fontsize=style["font.size"],
        )

    for spine in ax.spines.values():
        spine.set_edgecolor(style["axes.edgecolor"])
        spine.set_linewidth(style["axes.linewidth"])

    ax.tick_params(
        colors=style["xtick.color"],
        labelsize=style["xtick.labelsize"],
    )

    fig.tight_layout()

    # Center plot by mirroring left margin to right
    # This balances y-axis/label space for report layouts
    pos = ax.get_position()
    left_margin = pos.x0
    right_margin = 1.0 - pos.x1
    if left_margin > right_margin:
        # Add space on right to match left
        extra = left_margin - right_margin
        ax.set_position([pos.x0, pos.y0, pos.width - extra, pos.height])

    return PlotResult(
        fig=fig,
        ax=ax,
        handles=(handle,),
        metadata={
            "n_points": len(x_arr),
            "x_range": (float(x_arr.min()), float(x_arr.max())),
            "y_range": (float(y_arr.min()), float(y_arr.max())),
            "color_used": color_used,
        },
    )
