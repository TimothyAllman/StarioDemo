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
import sys
from pathlib import Path

from stario import JsonTracer
from stario import Relay
from stario import RichTracer
from stario import Stario

from stariodemo.DataBasePkg.db import create_database
from stariodemo.DataStructsPkg.UrlsModule import ABC_ADD_URL
from stariodemo.DataStructsPkg.UrlsModule import ABC_LIST_URL
from stariodemo.DataStructsPkg.UrlsModule import CHAT_URL
from stariodemo.DataStructsPkg.UrlsModule import HOME_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import SEND_URL
from stariodemo.DataStructsPkg.UrlsModule import SUBSCRIBE_URL
from stariodemo.DataStructsPkg.UrlsModule import TYPING_URL
from stariodemo.DataStructsPkg.UrlsModule import XYZ_ADD_URL
from stariodemo.DataStructsPkg.UrlsModule import XYZ_LIST_URL
from stariodemo.HandlersPkg.AbcAddPageEndpointModule import AbcAddPageEndpoint
from stariodemo.HandlersPkg.AbcListPageEndpointModule import AbcListPageEndpoint
from stariodemo.HandlersPkg.ChatPageEndpointModule import ChatPageEndpoint
from stariodemo.HandlersPkg.HomePageEndpointModule import HomePageEndpoint
from stariodemo.HandlersPkg.SendMessageModule import send_message
from stariodemo.HandlersPkg.SubscribeModule import subscribe
from stariodemo.HandlersPkg.TypingModule import typing
from stariodemo.HandlersPkg.XyzAddPageEndpointModule import XyzAddPageEndpoint
from stariodemo.HandlersPkg.XyzListPageEndpointModule import XyzListPageEndpoint


async def main():
    # Determine environment
    is_dev = "--local" in sys.argv or sys.stdout.isatty()

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

    # Create database - in-memory for dev, file-based for prod
    db = create_database(is_dev=is_dev)

    # Relay for pub/sub between SSE connections
    relay: Relay[str] = Relay()

    with tracer:
        app = Stario(tracer)

        # Static files - note: path is relative to this file's location
        app.assets("/static", Path(__file__).parent / "static")

        # Routes - closures inject db/relay where needed
        app.get(HOME_PAGE_URL, HomePageEndpoint(None))
        app.get(CHAT_URL, ChatPageEndpoint(None))
        app.get(ABC_ADD_URL, AbcAddPageEndpoint(None))
        app.get(ABC_LIST_URL, AbcListPageEndpoint(None))
        app.get(XYZ_ADD_URL, XyzAddPageEndpoint(None))
        app.get(XYZ_LIST_URL, XyzListPageEndpoint(None))
        app.get(SUBSCRIBE_URL, subscribe(db, relay))
        app.post(SEND_URL, send_message(db, relay))
        app.post(TYPING_URL, typing(db, relay))

        await app.serve(host=host, port=port, workers=workers)


if __name__ == "__main__":
    asyncio.run(main())
