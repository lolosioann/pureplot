"""Basic line plot example"""

import numpy as np

from pureplot import line

# Generate sample data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a basic line plot
result = line(x, y, title="Basic Line Plot", xlabel="X-axis", ylabel="Y-axis")

# To display the plot, you would typically use:
# result.show()
# However, since this is a code snippet, we will not execute it here.

result.fig.savefig("basic_line_plot.png")  # Save the figure as a PNG file
