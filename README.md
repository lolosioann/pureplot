# pureplot

Pure, opinionated matplotlib wrapper with Catppuccin aesthetics.

**Design principles:**
- Functional: no hidden state, each plot is self-contained
- Minimal: focus on common plots with defaults i think look good
- Beautiful: Catppuccin color schemes built-in
- Typed: full type hints for IDE support


## Installation

```bash
# Using uv
uv add pureplot

# Using pip
pip install pureplot
```

## Quick Start

```python
from pureplot import scatter
import numpy as np

x = np.random.randn(100)
y = np.random.randn(100)

result = scatter(x, y, title="My Plot")
result.fig.savefig("output.png")
```

## Development

```bash
uv sync --dev
uv run pytest
```
