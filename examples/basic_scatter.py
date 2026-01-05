"""Basic scatter plot example."""

import numpy as np

from pureplot import scatter

# Generate random data
np.random.seed(42)
x = np.random.randn(100)
y = 2 * x + np.random.randn(100) * 0.5

# Create scatter plot
result = scatter(
    x,
    y,
    title="Scatter Plot with Linear Trend",
    xlabel="X values",
    ylabel="Y values",
    alpha=0.6,
    size=80,
)

# Save the plot
result.fig.savefig("scatter_example.png")
print(f"Plot saved! {result.metadata['n_points']} points plotted.")
print(f"X range: {result.metadata['x_range']}")
print(f"Y range: {result.metadata['y_range']}")
