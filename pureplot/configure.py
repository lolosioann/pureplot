# pureplot/configure.py

from .policy import apply_policy

_CONFIGURED = False


def configure(**options) -> None:
    """
    One-time global configuration.

    Must be called before any plotting primitive.
    """
    global _CONFIGURED

    if _CONFIGURED:
        raise RuntimeError(
            "pureplot.configure() may only be called once, "
            "before any plots are created."
        )

    apply_policy(options)
    _CONFIGURED = True
