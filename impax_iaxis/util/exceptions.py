"""
This module provides errors/exceptions and warnings of general use.

Exceptions that are specific to a given package should **not** be here,
but rather in the particular package.

This code is based on that provided by SunPy see
    licenses/SUNPY.rst
"""

import warnings

__all__ = [
    "iAXISWarning",
    "iAXISUserWarning",
    "iAXISDeprecationWarning",
    "iAXISPendingDeprecationWarning",
    "warn_user",
    "warn_deprecated",
]


class iAXISWarning(Warning):
    """
    The base warning class from which all IMPAX IAXIS warnings should inherit.

    Any warning inheriting from this class is handled by the IMPAX IAXIS
    logger. This warning should not be issued in normal code. Use
    "iAXISUserWarning" instead or a specific sub-class.
    """


class iAXISUserWarning(UserWarning, iAXISWarning):
    """
    The primary warning class for IMPAX IAXIS.

    Use this if you do not need a specific type of warning.
    """


class iAXISDeprecationWarning(FutureWarning, iAXISWarning):
    """
    A warning class to indicate a deprecated feature.
    """


class iAXISPendingDeprecationWarning(PendingDeprecationWarning, iAXISWarning):
    """
    A warning class to indicate a soon-to-be deprecated feature.
    """


def warn_user(msg, stacklevel=1):
    """
    Raise a `iAXISUserWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, iAXISUserWarning, stacklevel + 1)


def warn_deprecated(msg, stacklevel=1):
    """
    Raise a `iAXISDeprecationWarning`.

    Parameters
    ----------
    msg : str
        Warning message.
    stacklevel : int
        This is interpreted relative to the call to this function,
        e.g. ``stacklevel=1`` (the default) sets the stack level in the
        code that calls this function.
    """
    warnings.warn(msg, iAXISDeprecationWarning, stacklevel + 1)
