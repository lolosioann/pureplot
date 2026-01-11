from __future__ import annotations

from contextlib import AbstractContextManager

from .policy import PolicySnapshot, apply_policy, restore_policy


class PlotContext(AbstractContextManager):
    """
    Controlled mutation context for matplotlib global state.

    This is the ONLY place where mutation is allowed.
    """

    def __init__(self, overrides: dict):
        self._overrides = overrides
        self._previous_policy: PolicySnapshot | None = None

    def __enter__(self):
        # Capture current global state
        self._previous_policy = PolicySnapshot.capture()

        # Apply overrides (rcParams, fonts, backend, etc.)
        apply_policy(self._overrides)

        return self

    def __exit__(self, exc_type, exc_value, traceback):
        # Restore previous state unconditionally
        restore_policy(self._previous_policy)
        return False
