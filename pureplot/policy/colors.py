"""Color policies using Catppuccin palette."""

from collections.abc import Sequence

from catppuccin import PALETTE


def get_catppuccin_colors() -> dict[str, str]:
    """Get Catppuccin Mocha color palette.

    Returns:
        Dictionary mapping color names to hex values
    """
    mocha = PALETTE.mocha
    return {
        "rosewater": mocha.colors.rosewater.hex,
        "flamingo": mocha.colors.flamingo.hex,
        "pink": mocha.colors.pink.hex,
        "mauve": mocha.colors.mauve.hex,
        "red": mocha.colors.red.hex,
        "maroon": mocha.colors.maroon.hex,
        "peach": mocha.colors.peach.hex,
        "yellow": mocha.colors.yellow.hex,
        "green": mocha.colors.green.hex,
        "teal": mocha.colors.teal.hex,
        "sky": mocha.colors.sky.hex,
        "sapphire": mocha.colors.sapphire.hex,
        "blue": mocha.colors.blue.hex,
        "lavender": mocha.colors.lavender.hex,
        "text": mocha.colors.text.hex,
        "subtext1": mocha.colors.subtext1.hex,
        "subtext0": mocha.colors.subtext0.hex,
        "overlay2": mocha.colors.overlay2.hex,
        "overlay1": mocha.colors.overlay1.hex,
        "overlay0": mocha.colors.overlay0.hex,
        "surface2": mocha.colors.surface2.hex,
        "surface1": mocha.colors.surface1.hex,
        "surface0": mocha.colors.surface0.hex,
        "base": mocha.colors.base.hex,
        "mantle": mocha.colors.mantle.hex,
        "crust": mocha.colors.crust.hex,
    }


def get_color_cycle(n_colors: int = 8) -> Sequence[str]:
    """Get color cycle for multi-series plots.

    Args:
        n_colors: Number of colors to return (default: 8)

    Returns:
        List of hex color codes
    """
    colors = get_catppuccin_colors()
    # Prioritize vibrant colors for data visualization
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
