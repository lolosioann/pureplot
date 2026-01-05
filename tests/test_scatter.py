"""Tests for scatter primitive."""

import numpy as np
import pytest
from matplotlib.axes import Axes
from matplotlib.figure import Figure

from pureplot import PlotResult, scatter


def test_scatter_basic() -> None:
    """Test basic scatter plot creation."""
    x = np.array([1, 2, 3, 4, 5])
    y = np.array([2, 4, 6, 8, 10])

    result = scatter(x, y)

    assert isinstance(result, PlotResult)
    assert isinstance(result.fig, Figure)
    assert isinstance(result.ax, Axes)
    assert len(result.handles) == 1
    assert result.metadata["n_points"] == 5


def test_scatter_with_labels() -> None:
    """Test scatter plot with title and axis labels."""
    x = np.array([1, 2, 3])
    y = np.array([1, 4, 9])

    result = scatter(x, y, title="Test Plot", xlabel="X", ylabel="Y")

    assert result.ax.get_title() == "Test Plot"
    assert result.ax.get_xlabel() == "X"
    assert result.ax.get_ylabel() == "Y"


def test_scatter_custom_color() -> None:
    """Test scatter plot with custom color."""
    x = np.array([1, 2, 3])
    y = np.array([1, 2, 3])

    result = scatter(x, y, color="#FF0000")

    assert result.metadata["color_used"] == "#FF0000"


def test_scatter_custom_size() -> None:
    """Test scatter plot with custom marker size."""
    x = np.array([1, 2, 3])
    y = np.array([1, 2, 3])

    result = scatter(x, y, size=100)

    # No assertion error means it ran successfully
    assert result is not None


def test_scatter_shape_mismatch() -> None:
    """Test that mismatched x and y shapes raise ValueError."""
    x = np.array([1, 2, 3])
    y = np.array([1, 2])

    with pytest.raises(ValueError, match="must have same shape"):
        scatter(x, y)


def test_scatter_metadata() -> None:
    """Test metadata contains expected information."""
    x = np.array([0, 1, 2, 3, 4])
    y = np.array([0, 2, 4, 6, 8])

    result = scatter(x, y)

    assert "n_points" in result.metadata
    assert "x_range" in result.metadata
    assert "y_range" in result.metadata
    assert "color_used" in result.metadata

    assert result.metadata["x_range"] == (0.0, 4.0)
    assert result.metadata["y_range"] == (0.0, 8.0)


def test_scatter_deterministic() -> None:
    """Test that scatter produces deterministic results."""
    x = np.array([1, 2, 3])
    y = np.array([4, 5, 6])

    result1 = scatter(x, y, title="Test")
    result2 = scatter(x, y, title="Test")

    # Same data and params should produce same metadata
    assert result1.metadata == result2.metadata


def test_scatter_with_lists() -> None:
    """Test scatter accepts Python lists."""
    x = [1, 2, 3]
    y = [1, 4, 9]

    result = scatter(x, y)

    assert result.metadata["n_points"] == 3


def test_plot_result_immutable() -> None:
    """Test that PlotResult is frozen/immutable."""
    x = np.array([1, 2, 3])
    y = np.array([1, 2, 3])

    result = scatter(x, y)

    with pytest.raises(AttributeError):
        result.metadata = {}  # type: ignore
