"""`appengine_config` gets loaded when starting a new application instance."""

import sys
import os.path


# Add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

# Add libraries that were added by `pip` to `sys.path`.
sys.path.append(os.path.join(os.path.dirname(__file__),
                             'venv/lib/python2.7/site-packages'))
