General guidelines:
- Do not impordt matplotlib.pyplot in policy/
- lint against plt.gca()
- centralize rcParams access

Pure plotting in this library means:
- Referential transparency with respect to policy
- No hidden state
- Deterministic rendering
- Explicit outputs
- Mutation isolated to context managers
