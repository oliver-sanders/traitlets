from warnings import warn

from . import traitlets
from ._version import __version__, version_info
from .traitlets import *
from .utils.bunch import Bunch
from .utils.decorators import signature_has_traits
from .utils.importstring import import_item


class Sentinel(traitlets.Sentinel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        warn(
            """
            Sentinel is not a public part of the traitlets API.
            It was published by mistake, and may be removed in the future.
            """,
            DeprecationWarning,
            stacklevel=2,
        )
