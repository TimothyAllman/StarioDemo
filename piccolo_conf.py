from piccolo.conf.apps import AppRegistry
from piccolo.engine.sqlite import SQLiteEngine

SQLITE_DB_PATH = "piccolochat.db"

DB = SQLiteEngine(
    path=SQLITE_DB_PATH,
    timeout=60,
    
)

import asyncio
from piccolo.querystring import QueryString
from piccolo_conf import DB  

async def enable_wal():
    # 1. Establish the connection pool/engine
    await DB.start_connection_pool()
    
    # 2. Wrap the PRAGMA statements in Piccolo QueryStrings
    wal_query = QueryString("PRAGMA journal_mode=WAL;")
    sync_query = QueryString("PRAGMA synchronous=NORMAL;")
    
    # 3. Execute the queries directly through the engine instance
    await DB.run_querystring(wal_query)
    await DB.run_querystring(sync_query)
    
    # 4. Clean up connection pool (if running as a standalone script)
    await DB.close_connection_pool()

APP_REGISTRY = AppRegistry(
    apps=[
        "stariodemo.PiccoloPkg.piccolo_app",
    ]
)
