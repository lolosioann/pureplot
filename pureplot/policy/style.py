"""Style policies for matplotlib configuration."""

from typing import Any

from .colors import get_catppuccin_colors


def get_default_style() -> dict[str, Any]:
    """Get default matplotlib rcParams overrides.

    Returns:
        Dictionary of matplotlib rcParams settings
    """
    colors = get_catppuccin_colors()

    return {
        # Figure
        "figure.facecolor": colors["base"],
        "figure.edgecolor": colors["base"],
        "figure.figsize": (8, 6),
        "figure.dpi": 100,
        # Axes
        "axes.facecolor": colors["base"],
        "axes.edgecolor": colors["overlay0"],
        "axes.labelcolor": colors["text"],
        "axes.linewidth": 1.2,
        "axes.grid": True,
        "axes.axisbelow": True,
        # Grid
        "grid.color": colors["surface1"],
        "grid.linestyle": "-",
        "grid.linewidth": 0.8,
        "grid.alpha": 0.3,
        # Ticks
        "xtick.color": colors["text"],
        "ytick.color": colors["text"],
        "xtick.labelsize": 10,
        "ytick.labelsize": 10,
        # Text
        "text.color": colors["text"],
        "font.size": 11,
        "font.family": "sans-serif",
        # Lines
        "lines.linewidth": 2.0,
        "lines.markersize": 6,
        # Legend
        "legend.frameon": True,
        "legend.facecolor": colors["mantle"],
        "legend.edgecolor": colors["overlay0"],
        "legend.fontsize": 10,
        # Savefig
        "savefig.facecolor": colors["base"],
        "savefig.edgecolor": colors["base"],
        "savefig.dpi": 150,
        "savefig.bbox": "tight",
    }
