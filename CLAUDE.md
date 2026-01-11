# Pureplot - Project Context

## Overview

Pure, opinionated matplotlib wrapper with Catppuccin aesthetics. Emphasizes functional programming principles: no hidden state, deterministic rendering, explicit outputs.

## Architecture

```
pureplot/
├── __init__.py          # Public API exports
├── configure.py         # One-time global configuration
├── context.py           # PlotContext - ONLY mutation point
├── plotter.py           # Singleton for policy access (future use)
├── policy.py            # PolicySnapshot, colors, styles, figure creation
└── primitives/
    ├── __init__.py      # Exports: PlotResult, scatter
    ├── interface.py     # plot_template - canonical plotting lifecycle
    ├── scatter.py       # Scatter primitive
    ├── line.py          # Line primitive (not yet exported)
    ├── result.py        # PlotResult frozen dataclass
    └── utils.py         # Validation, figure/axes setup
```

## Design Principles

1. **Pure plotting** - Referential transparency with respect to policy
2. **No hidden state** - Each plot is self-contained
3. **Deterministic rendering** - Same inputs = same outputs
4. **Explicit outputs** - PlotResult contains fig, ax, handles, metadata
5. **Mutation isolated** - Only PlotContext can mutate matplotlib globals

## Module Responsibilities

### policy.py
- `PolicySnapshot` - Immutable snapshot of matplotlib rcParams
- `get_catppuccin_colors()` - Full Mocha palette (26 colors)
- `get_color_cycle(n)` - Vibrant colors for data visualization
- `get_default_style()` - rcParams defaults for Catppuccin theme
- `apply_policy(options)` - Merge options with defaults, apply to rcParams
- `create_figure(figsize)` - Figure creation with policy styling
- `restore_policy(snapshot)` - Restore from snapshot

### context.py
- `PlotContext` - Context manager for temporary policy overrides
- ONLY place where mutation is allowed
- Captures state on enter, restores on exit (even on error)

### configure.py
- `configure(**options)` - One-time global setup before any plotting
- Enforces single-call constraint

### primitives/interface.py
- `plot_template(draw_fn, ...)` - Canonical plotting lifecycle:
  1. Validate inputs
  2. Create figure/axes via policy
  3. Delegate drawing to primitive
  4. Apply common styling (title, labels, spines)
  5. Return PlotResult

### primitives/scatter.py, line.py
- `scatter(x, y, ...)` / `line(x, y, ...)` - User-facing functions
- `_draw_scatter()` / `_draw_line()` - Internal drawing, returns (handle, color_used)

### primitives/result.py
- `PlotResult` - Frozen dataclass: fig, ax, handles, metadata
- metadata includes: n_points, x_range, y_range, color_used

## Patterns Used

| Pattern | Implementation | Purpose |
|---------|---------------|---------|
| Singleton | `Plotter` via `get_plotter()` | Single policy access point |
| Immutable Snapshot | `PolicySnapshot` | Capture/restore matplotlib state |
| Context Manager | `PlotContext` | Temporary overrides with auto-restore |
| Strategy | `plot_template()` + draw functions | Reusable plotting lifecycle |
| Factory | `create_figure()` | Consistent figure creation |
| Frozen Dataclass | `PlotResult` | Immutable results |

## Development Guidelines

### Testing
- Run: `uv run pytest`
- Test files: `tests/test_*.py`
- Tests verify: shape validation, labels, colors, metadata, determinism

### Type Hints
- Mandatory for all functions/methods
- Use `from __future__ import annotations` for forward refs

### Forbidden Patterns
- `plt.gca()` - Creates hidden state
- Global `rcParams` access outside policy layer
- Mutation outside `PlotContext`

### Adding New Primitives
1. Create `primitives/newprim.py`
2. Implement `_draw_newprim(ax, x, y, style, colors, **kwargs) -> DrawResult`
3. Implement `newprim(x, y, ...) -> PlotResult` using `plot_template`
4. Export from `primitives/__init__.py`
5. Add tests in `tests/test_newprim.py`

## Color Palette (Catppuccin Latte - Light Mode)

Vibrant cycle order: mauve, blue, green, peach, pink, teal, yellow, red, sapphire, lavender, flamingo, sky

Background colors: base (#eff1f5), mantle (#e6e9ef), crust (#dce0e8)
Text colors: text (#4c4f69), subtext0, subtext1
UI colors: surface0/1/2, overlay0/1/2

## Plot Centering

Plots are automatically centered for report layouts. After `tight_layout()`, the right margin is adjusted to match the left margin (which includes y-axis tick labels and axis label space). This ensures the plot area is visually centered in the figure.

## Current Status

### Implemented
- Scatter plot with full styling
- Line plot (internal, not exported)
- Policy system (colors, styles, snapshots)
- PlotContext for temporary overrides
- One-time configuration

### Planned (v0.2+)
- Additional primitives: bar, histogram, heatmap, subplot_grid
- Decorators: @validate_data, @auto_labels, @publication_ready
- Enhanced contexts: theme_context, backend_context

### Out of Scope
- 3D plotting
- Geographic/map plots
- Network graphs
