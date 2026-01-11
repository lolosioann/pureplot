General guidelines:
- matplotlib.pyplot only in policy.py (for create_figure) and context.py
- lint against plt.gca() - creates hidden state
- centralize rcParams access through policy layer
- primitives must not import plt directly

Pure plotting in this library means:
- Referential transparency with respect to policy
- No hidden state
- Deterministic rendering
- Explicit outputs
- Mutation isolated to context managers
