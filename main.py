"""
Stario Chat - Application Entry Point

This file bootstraps the application:
1. Configures tracing (RichTracer for dev, JsonTracer for production)
2. Creates database (in-memory for dev, file-based for production)
3. Registers routes with dependencies injected via closures
4. Starts the server

Run with: uv run main.py
      or: python main.py
"""

import asyncio
import os
from pathlib import Path

from stario import JsonTracer
from stario import Relay
from stario import RichTracer
from stario import Stario

from piccolo_conf import SQLITE_DB_PATH
from stariodemo.DataStructsPkg.UrlsModule import ABC_ADD_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import ABC_CALCULATION_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import ABC_LIST_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import API_ABC_CALCULATION_URL
from stariodemo.DataStructsPkg.UrlsModule import API_CALCULATION_URL
from stariodemo.DataStructsPkg.UrlsModule import API_USER_CREATE_URL
from stariodemo.DataStructsPkg.UrlsModule import API_WIDGET_ADD_URL
from stariodemo.DataStructsPkg.UrlsModule import API_WIDGET_LIST_URL
from stariodemo.DataStructsPkg.UrlsModule import API_WIDGET_SEED_URL
from stariodemo.DataStructsPkg.UrlsModule import CHAT_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import GIVE_ME_JSON_URL
from stariodemo.DataStructsPkg.UrlsModule import GIVE_ME_TEXT_URL
from stariodemo.DataStructsPkg.UrlsModule import HOME_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import SEND_URL
from stariodemo.DataStructsPkg.UrlsModule import SUBSCRIBE_URL
from stariodemo.DataStructsPkg.UrlsModule import TYPING_URL
from stariodemo.DataStructsPkg.UrlsModule import XYZ_ADD_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import XYZ_LIST_PAGE_URL
from stariodemo.HandlersPkg.AbcAddPageEndpointModule import AbcAddPageEndpoint
from stariodemo.HandlersPkg.AbcCalculationEndpointModule import AbcCalculationEndpoint
from stariodemo.HandlersPkg.AbcCalculationPageEndpointModule import AbcCalculationPageEndpoint
from stariodemo.HandlersPkg.AbcListPageEndpointModule import AbcListPageEndpoint
from stariodemo.HandlersPkg.ApiCalculationEndpointModule import ApiCalculationEndpoint
from stariodemo.HandlersPkg.ChatPageEndpointModule import ChatPageEndpoint
from stariodemo.HandlersPkg.GiveMeJsonEndpointModule import GiveMeJsonEndpoint
from stariodemo.HandlersPkg.GiveMeTextEndpointModule import GiveMeTextEndpoint
from stariodemo.HandlersPkg.HomePageEndpointModule import HomePageEndpoint
from stariodemo.HandlersPkg.SendMessageModule import send_message
from stariodemo.HandlersPkg.SubscribeModule import subscribe
from stariodemo.HandlersPkg.TypingModule import typing

# from stariodemo.HandlersPkg.WidgetAddEndpointModule import WidgetAddEndpoint
from stariodemo.HandlersPkg.WidgetAddEndpointModule import WidgetAddEndpoint
from stariodemo.HandlersPkg.WidgetListEndpointModule import WidgetListEndpoint
from stariodemo.HandlersPkg.WidgetSeedEndpointModule import WidgetSeedEndpoint
from stariodemo.HandlersPkg.XyzAddPageEndpointModule import XyzAddPageEndpoint
from stariodemo.HandlersPkg.XyzListPageEndpointModule import XyzListPageEndpoint
from stariodemo.PiccoloPkg import PiccoloChatDb
from stariodemo.PiccoloPkg.InitPiccoloDbModule import InitPiccoloDb


async def main():
    # Determine environment
    is_dev = True  # "--local" in sys.argv or sys.stdout.isatty()

    if is_dev:
        tracer = RichTracer()
        host = "127.0.0.1"
        port = 8000
        workers = 1
    else:
        tracer = JsonTracer()
        host = "0.0.0.0"
        port = 8000
        workers = 4

    # remove any prior db
    print("deleting db....")
    if os.path.exists(SQLITE_DB_PATH):
        os.remove(SQLITE_DB_PATH)

    # Create database - in-memory for dev, file-based for prod
    print("creating db...")
    # db = create_database(is_dev=False)
    await InitPiccoloDb()
    db = PiccoloChatDb()
    print("db created successfully")

    # Relay for pub/sub between SSE connections
    relay: Relay[str] = Relay()

    try:
        with tracer:
            app = Stario(tracer)

            # Static files - note: path is relative to this file's location
            app.assets("/static", Path(__file__).parent / "static")

            # Routes - closures inject db/relay where needed
            app.get(HOME_PAGE_URL, HomePageEndpoint())

            app.get(ABC_ADD_PAGE_URL, AbcAddPageEndpoint())
            app.get(ABC_LIST_PAGE_URL, AbcListPageEndpoint())
            app.get(ABC_CALCULATION_PAGE_URL, AbcCalculationPageEndpoint())

            app.get(XYZ_ADD_PAGE_URL, XyzAddPageEndpoint())
            app.get(XYZ_LIST_PAGE_URL, XyzListPageEndpoint())

            app.get(CHAT_PAGE_URL, ChatPageEndpoint())
            app.get(SUBSCRIBE_URL, subscribe(db, relay))
            app.post(SEND_URL, send_message(db, relay))
            app.post(TYPING_URL, typing(db, relay))

            app.get(API_CALCULATION_URL, ApiCalculationEndpoint())
            app.get(API_USER_CREATE_URL, ApiCalculationEndpoint())
            app.get(API_ABC_CALCULATION_URL, AbcCalculationEndpoint())

            app.get(API_WIDGET_ADD_URL, WidgetAddEndpoint())
            app.get(API_WIDGET_LIST_URL, WidgetListEndpoint())
            app.get(API_WIDGET_SEED_URL, WidgetSeedEndpoint())

            app.get(GIVE_ME_TEXT_URL, GiveMeTextEndpoint())
            app.get(GIVE_ME_JSON_URL, GiveMeJsonEndpoint())

            await app.serve(host=host, port=port, workers=workers)
    finally:
        print("ending...")
        x = 0
        # await close_db()


if __name__ == "__main__":
    asyncio.run(main())
