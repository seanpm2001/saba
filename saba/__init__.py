# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""
Bridge between Sherpa and Astropy modeling.
"""

# Affiliated packages may add whatever they like to this file, but
# should keep this content at the top.
# ----------------------------------------------------------------------------
from ._astropy_init import *
# ----------------------------------------------------------------------------

# For egg_info test builds to pass, put package imports here.
if not _ASTROPY_SETUP_:
    from .main import SherpaFitter, SherpaMCMC, Stat, OptMethod, EstMethod
    from . import util
    from . import datasets
    from . import stat_methods
