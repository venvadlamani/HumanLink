"""`appengine_config` gets loaded when starting a new application instance."""

import common
import sys
import os.path


# Add `lib` subdirectory to `sys.path`, so our `main` module can load
# third-party libraries.
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib'))

# Add libraries that were added by `pip` to `sys.path`.
sys.path.append(os.path.join(os.path.dirname(__file__), 'lib/pip'))


# Workaround the SSL issue on dev_appserver.
if common.is_localhost():
    import imp
    import chunk
    from google.appengine.tools.devappserver2.python import sandbox

    sandbox._WHITE_LIST_C_MODULES += ['_ssl', '_socket']
    psocket = os.path.join(os.path.dirname(chunk.__file__), 'socket.py')
    imp.load_source('socket', psocket)
