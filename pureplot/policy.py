"""Policy module - pure functions for plot configuration."""

from collections.abc import Sequence
from dataclasses import dataclass
from typing import Any

import matplotlib as mpl
import matplotlib.pyplot as plt
from catppuccin import PALETTE
from matplotlib.figure import Figure

# -----------------------------------------------------------------------------
# PolicySnapshot
# -----------------------------------------------------------------------------


@dataclass(frozen=True)
class PolicySnapshot:
    """Immutable snapshot of matplotlib rcParams."""

    rcparams: dict[str, Any]

    @staticmethod
    def capture() -> "PolicySnapshot":
        return PolicySnapshot(rcparams=dict(mpl.rcParams))


def restore_policy(snapshot: PolicySnapshot) -> None:
    """Restore matplotlib rcParams from a snapshot."""
    mpl.rcParams.update(snapshot.rcparams)


# -----------------------------------------------------------------------------
# Color Policy
# -----------------------------------------------------------------------------


def get_catppuccin_colors() -> dict[str, str]:
    """Get Catppuccin Latte color palette (light mode).

    Returns:
        Dictionary mapping color names to hex values.
    """
    latte = PALETTE.latte
    return {
        "rosewater": latte.colors.rosewater.hex,
        "flamingo": latte.colors.flamingo.hex,
        "pink": latte.colors.pink.hex,
        "mauve": latte.colors.mauve.hex,
        "red": latte.colors.red.hex,
        "maroon": latte.colors.maroon.hex,
        "peach": latte.colors.peach.hex,
        "yellow": latte.colors.yellow.hex,
        "green": latte.colors.green.hex,
        "teal": latte.colors.teal.hex,
        "sky": latte.colors.sky.hex,
        "sapphire": latte.colors.sapphire.hex,
        "blue": latte.colors.blue.hex,
        "lavender": latte.colors.lavender.hex,
        "text": latte.colors.text.hex,
        "subtext1": latte.colors.subtext1.hex,
        "subtext0": latte.colors.subtext0.hex,
        "overlay2": latte.colors.overlay2.hex,
        "overlay1": latte.colors.overlay1.hex,
        "overlay0": latte.colors.overlay0.hex,
        "surface2": latte.colors.surface2.hex,
        "surface1": latte.colors.surface1.hex,
        "surface0": latte.colors.surface0.hex,
        "base": latte.colors.base.hex,
        "mantle": latte.colors.mantle.hex,
        "crust": latte.colors.crust.hex,
    }


def get_color_cycle(n_colors: int = 8) -> Sequence[str]:
    """Get color cycle for multi-series plots.

    Args:
        n_colors: Number of colors to return (default: 8).

    Returns:
        List of hex color codes.
    """
    colors = get_catppuccin_colors()
    cycle = [
        colors["mauve"],
        colors["blue"],
        colors["green"],
        colors["peach"],
        colors["pink"],
        colors["teal"],
        colors["yellow"],
        colors["red"],
        colors["sapphire"],
        colors["lavender"],
        colors["flamingo"],
        colors["sky"],
    ]
    return cycle[:n_colors]


# -----------------------------------------------------------------------------
# Style Policy
# -----------------------------------------------------------------------------


def get_default_style() -> dict[str, Any]:
    """Get default matplotlib rcParams overrides.

    Returns:
        Dictionary of matplotlib rcParams settings.
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


def apply_policy(options: dict[str, Any] | None = None) -> None:
    """Apply policy to matplotlib rcParams.

    Merges provided options with defaults.

    Args:
        options: Optional dict of rcParams overrides.
    """
    defaults = get_default_style()
    if options:
        defaults.update(options)
    mpl.rcParams.update(defaults)


# -----------------------------------------------------------------------------
# Figure Creation
# -----------------------------------------------------------------------------


def create_figure(
    figsize: tuple[float, float] | None = None,
) -> Figure:
    """Create a figure with policy-applied styling.

    Args:
        figsize: Optional figure size (width, height) in inches.

    Returns:
        Configured matplotlib Figure.
    """
    style = get_default_style()
    fig_size = figsize or style["figure.figsize"]
    fig = plt.figure(figsize=fig_size, dpi=style["figure.dpi"])
    fig.patch.set_facecolor(style["figure.facecolor"])
    return fig
