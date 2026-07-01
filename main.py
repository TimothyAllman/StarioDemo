"""
Stario Demo
"""

import os

from stario import App
from stario import Relay
from stario import Span
from stario import StaticAssets

from piccolo_conf import SQLITE_DB_PATH
from piccolo_conf import enable_wal
from stariodemo.DataStructsPkg.UrlsModule import ABC_ADD_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import ABC_CALCULATION_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import ABC_LIST_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import API_ABC_CALCULATION_URL
from stariodemo.DataStructsPkg.UrlsModule import API_CALCULATION_URL
from stariodemo.DataStructsPkg.UrlsModule import CHAT_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import CHAT_SEND_URL
from stariodemo.DataStructsPkg.UrlsModule import CHAT_SUBSCRIBE_URL
from stariodemo.DataStructsPkg.UrlsModule import CHAT_TYPING_URL
from stariodemo.DataStructsPkg.UrlsModule import GIVE_ME_JSON_URL
from stariodemo.DataStructsPkg.UrlsModule import GIVE_ME_TEXT_URL
from stariodemo.DataStructsPkg.UrlsModule import HOME_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import USER_ADD_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import USER_DETAILS_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import USER_EDIT_PAGE_URL
from stariodemo.DataStructsPkg.UrlsModule import USER_LIST_PAGE_URL
from stariodemo.FromTableDatabaseFunctionsPkg import PiccoloChatDb
from stariodemo.FromTableDatabaseFunctionsPkg.InitPiccoloDbModule import InitPiccoloDb
from stariodemo.HandlersPkg.AbcAddPageEndpointModule import AbcAddPageEndpoint
from stariodemo.HandlersPkg.AbcCalculationEndpointModule import AbcCalculationEndpoint
from stariodemo.HandlersPkg.AbcCalculationPageEndpointModule import AbcCalculationPageEndpoint
from stariodemo.HandlersPkg.AbcListPageEndpointModule import AbcListPageEndpoint
from stariodemo.HandlersPkg.ApiCalculationEndpointModule import ApiCalculationEndpoint
from stariodemo.HandlersPkg.ChatPageEndpointModule import ChatPageEndpoint
from stariodemo.HandlersPkg.GiveMeJsonEndpointModule import GiveMeJsonEndpoint
from stariodemo.HandlersPkg.GiveMeTextEndpointModule import GiveMeTextEndpoint
from stariodemo.HandlersPkg.HomePageEndpointModule import HomePageEndpoint
from stariodemo.HandlersPkg.SendMessageEndpointModule import SendMessageEndpoint
from stariodemo.HandlersPkg.SubscribeEndpointModule import SubscribeEndpoint
from stariodemo.HandlersPkg.TypingEndpointModule import TypingEndpoint
from stariodemo.HandlersPkg.UserAddPageEndpointModule import UserAddPageEndpoint
from stariodemo.HandlersPkg.UserDetailsPageEndpointModule import UserDetailsPageEndpoint
from stariodemo.HandlersPkg.UserEditPageEndpointModule import UserEditPageEndpoint
from stariodemo.HandlersPkg.UserListPageEndpointModule import UserListPageEndpoint
from stariodemo.StaticAssetsPkg.StaticAssetsModule import ASSETS


async def bootstrap(
    app: App,
    span: Span,
):
    span.event("stariodemo.startup.begin")
    # config = Config.from_env()

    # remove any prior db
    span.event("stariodemo.db.deleting.old")
    if os.path.exists(SQLITE_DB_PATH):
        os.remove(SQLITE_DB_PATH)

    # Create database
    span.event("stariodemo.db.creating.new")
    await InitPiccoloDb()
    db = PiccoloChatDb()
    await enable_wal()
    span.event("stariodemo.db.created.successfully")

    # Relay for pub/sub between SSE connections
    span.event("stariodemo.relays.creating.all")
    relay = Relay()

    # span.attrs(
    #     {
    #         "stariodemo.db_path": config.db_path,
    #         "stariodemo.static_dir": str(ASSETS.directory),
    #     }
    # )

    # Static files - note: path is relative to this file's location
    with span.step("static_assets") as s:
        static = StaticAssets(ASSETS)
        s.attrs(static.stats)
    static.register(app)

    # register_lobby(app, db, relay)
    # register_room(app, db, relay)

    # Routes - closures inject db/relay where needed
    app.get(HOME_PAGE_URL, HomePageEndpoint())

    # other pages
    app.get(ABC_ADD_PAGE_URL, AbcAddPageEndpoint())
    app.get(ABC_LIST_PAGE_URL, AbcListPageEndpoint())
    app.get(ABC_CALCULATION_PAGE_URL, AbcCalculationPageEndpoint())

    app.get(CHAT_PAGE_URL, ChatPageEndpoint())
    app.get(CHAT_SUBSCRIBE_URL, SubscribeEndpoint(db, relay))
    app.post(CHAT_SEND_URL, SendMessageEndpoint(db, relay))
    app.post(CHAT_TYPING_URL, TypingEndpoint(db, relay))

    app.get(USER_ADD_PAGE_URL, UserAddPageEndpoint())
    app.get(USER_LIST_PAGE_URL, UserListPageEndpoint())
    app.get(USER_EDIT_PAGE_URL, UserEditPageEndpoint())
    app.get(USER_DETAILS_PAGE_URL, UserDetailsPageEndpoint())

    # api
    app.get(API_CALCULATION_URL, ApiCalculationEndpoint())
    app.get(API_ABC_CALCULATION_URL, AbcCalculationEndpoint())

    app.get(GIVE_ME_TEXT_URL, GiveMeTextEndpoint())
    app.get(GIVE_ME_JSON_URL, GiveMeJsonEndpoint())

    span.event("stariodemo.startup.ready")

    yield

    span.attr("stariodemo.shutting.down", True)
    span.event("stariodemo.shutdown.begin")
    span.event("stariodemo.shutdown.complete")
