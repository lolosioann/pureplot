"""Scatter plot primitive."""

from typing import Any

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from numpy.typing import ArrayLike

from ..policy import get_color_cycle, get_default_style
from .result import PlotResult


def scatter(
    x: ArrayLike,
    y: ArrayLike,
    *,
    title: str | None = None,
    xlabel: str | None = None,
    ylabel: str | None = None,
    color: str | None = None,
    size: float | ArrayLike = 50,
    alpha: float = 0.7,
    figsize: tuple[float, float] | None = None,
    **kwargs: Any,
) -> PlotResult:
    """Create a scatter plot with Catppuccin styling.

    Pure function: creates new figure, applies policy, returns result.
    No hidden state, deterministic rendering.

    Args:
        x: X-axis data
        y: Y-axis data
        title: Plot title (optional)
        xlabel: X-axis label (optional)
        ylabel: Y-axis label (optional)
        color: Marker color (hex or name). Defaults to Catppuccin mauve
        size: Marker size(s) in points^2
        alpha: Marker transparency (0-1)
        figsize: Figure size (width, height) in inches
        **kwargs: Additional arguments passed to ax.scatter()

    Returns:
        PlotResult with fig, ax, handles, and metadata

    Examples:
        >>> import numpy as np
        >>> from pureplot import scatter
        >>> x = np.random.randn(100)
        >>> y = np.random.randn(100)
        >>> result = scatter(x, y, title="Random Data")
        >>> result.fig.savefig("scatter.png")
    """
    # Convert to numpy arrays for validation
    x_arr = np.asarray(x)
    y_arr = np.asarray(y)

    if x_arr.shape != y_arr.shape:
        raise ValueError(
            f"x and y must have same shape: {x_arr.shape} != {y_arr.shape}"
        )

    # Query policy
    style = get_default_style()
    colors = get_color_cycle(1)

    # Create figure with policy settings
    fig_size = figsize or style["figure.figsize"]
    fig: Figure = plt.figure(figsize=fig_size, dpi=style["figure.dpi"])
    fig.patch.set_facecolor(style["figure.facecolor"])

    # Create axes
    ax: Axes = fig.add_subplot(111)
    ax.set_facecolor(style["axes.facecolor"])

    # Apply grid settings
    if style["axes.grid"]:
        ax.grid(
            True,
            color=style["grid.color"],
            linestyle=style["grid.linestyle"],
            linewidth=style["grid.linewidth"],
            alpha=style["grid.alpha"],
        )
        ax.set_axisbelow(style["axes.axisbelow"])

    # Plot with policy colors
    plot_color = color if color is not None else colors[0]
    scatter_collection = ax.scatter(
        x_arr,
        y_arr,
        c=plot_color,
        s=size,
        alpha=alpha,
        **kwargs,
    )

    # Apply labels
    if title is not None:
        ax.set_title(title, color=style["text.color"], fontsize=style["font.size"] + 2)
    if xlabel is not None:
        ax.set_xlabel(
            xlabel, color=style["axes.labelcolor"], fontsize=style["font.size"]
        )
    if ylabel is not None:
        ax.set_ylabel(
            ylabel, color=style["axes.labelcolor"], fontsize=style["font.size"]
        )

    # Style spines
    for spine in ax.spines.values():
        spine.set_edgecolor(style["axes.edgecolor"])
        spine.set_linewidth(style["axes.linewidth"])

    # Style ticks
    ax.tick_params(
        colors=style["xtick.color"],
        labelsize=style["xtick.labelsize"],
    )

    # Tight layout
    fig.tight_layout()

    # Build metadata
    metadata = {
        "n_points": len(x_arr),
        "x_range": (float(x_arr.min()), float(x_arr.max())),
        "y_range": (float(y_arr.min()), float(y_arr.max())),
        "color_used": plot_color,
    }

    return PlotResult(
        fig=fig,
        ax=ax,
        handles=(scatter_collection,),
        metadata=metadata,
    )
