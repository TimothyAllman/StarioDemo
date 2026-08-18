import os

from piccolo.conf.apps import AppRegistry
from piccolo.engine.sqlite import SQLiteEngine

from stariodemo.WebsiteFeatureWidgetPkg import piccolo_app

SQLITE_DB_PATH = os.getenv("LITESTREAM_DB_PATH", "no ENV_VAR found")

DB = SQLiteEngine(
    path=SQLITE_DB_PATH,
    timeout=60,
)


APP_REGISTRY = AppRegistry(
    apps=[
        # "stariodemo.DatabasePiccoloFunctionsPkg.piccolo_app",
        piccolo_app.__name__
    ]
)
