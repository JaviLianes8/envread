"""Allow ``python -m envread`` as an alias for the ``envread`` command."""

import sys

from ._cli import main

sys.exit(main())
