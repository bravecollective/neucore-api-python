
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.application_api import ApplicationApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from neucore_api.api.application_api import ApplicationApi
from neucore_api.api.application___characters_api import ApplicationCharactersApi
from neucore_api.api.application___esi_api import ApplicationESIApi
from neucore_api.api.application___groups_api import ApplicationGroupsApi
from neucore_api.api.application___tracking_api import ApplicationTrackingApi
