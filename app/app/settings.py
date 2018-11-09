import os

IS_PRODUCTION = os.environ.get('IS_PRODUCTION')

if IS_PRODUCTION:
    from .configs.production.settings import *
else:
    from .configs.development.settings import *
