from piccolo.conf.apps import AppRegistry
from piccolo.engine.sqlite import SQLiteEngine

SQLITE_DB_PATH = "piccolochat.db"
DB = SQLiteEngine(
    path=SQLITE_DB_PATH,
    timeout=60,
)
APP_REGISTRY = AppRegistry(
    apps=[
        "stariodemo.PiccoloPkg.piccolo_app",
    ]
)
