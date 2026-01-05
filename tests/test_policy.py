"""Tests for policy module."""

from pureplot.policy import get_catppuccin_colors, get_color_cycle, get_default_style


def test_get_catppuccin_colors() -> None:
    """Test Catppuccin color dictionary."""
    colors = get_catppuccin_colors()

    # Check essential colors exist
    assert "mauve" in colors
    assert "blue" in colors
    assert "green" in colors
    assert "text" in colors
    assert "base" in colors

    # Check hex format
    for color_name, hex_value in colors.items():
        assert hex_value.startswith("#")
        assert len(hex_value) == 7  # #RRGGBB


def test_get_color_cycle_default() -> None:
    """Test default color cycle."""
    cycle = get_color_cycle()

    assert len(cycle) == 8
    for color in cycle:
        assert color.startswith("#")


def test_get_color_cycle_custom_count() -> None:
    """Test color cycle with custom count."""
    cycle = get_color_cycle(n_colors=3)

    assert len(cycle) == 3


def test_get_default_style() -> None:
    """Test default style dictionary."""
    style = get_default_style()

    # Check key settings exist
    assert "figure.facecolor" in style
    assert "axes.facecolor" in style
    assert "text.color" in style
    assert "figure.figsize" in style

    # Check types
    assert isinstance(style["figure.figsize"], tuple)
    assert isinstance(style["figure.dpi"], int)
    assert isinstance(style["axes.grid"], bool)


def test_color_cycle_consistency() -> None:
    """Test that color cycle is deterministic."""
    cycle1 = get_color_cycle(5)
    cycle2 = get_color_cycle(5)

    assert cycle1 == cycle2
