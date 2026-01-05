"""pureplot - Pure, opinionated matplotlib wrapper with Catppuccin aesthetics."""

from .policy import get_catppuccin_colors, get_color_cycle, get_default_style
from .primitives import PlotResult, scatter

__version__ = "0.1.0"
__all__ = [
    "scatter",
    "PlotResult",
    "get_catppuccin_colors",
    "get_color_cycle",
    "get_default_style",
]
