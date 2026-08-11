"""
Stario Demo
"""

from stario import App
from stario import Relay
from stario import Span
from stario import StaticAssets

from stariodemo.BasicStructsPkg.UrlsModule import ABC_ADD_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import ABC_CALCULATION_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import ABC_LIST_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import API_ABC_CALCULATION_URL
from stariodemo.BasicStructsPkg.UrlsModule import API_CALCULATION_URL
from stariodemo.BasicStructsPkg.UrlsModule import API_TOAST_ERROR_TEST_URL
from stariodemo.BasicStructsPkg.UrlsModule import API_TOAST_SUCCESS_TEST_URL
from stariodemo.BasicStructsPkg.UrlsModule import CHAT_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import CHAT_SEND_URL
from stariodemo.BasicStructsPkg.UrlsModule import CHAT_SUBSCRIBE_URL
from stariodemo.BasicStructsPkg.UrlsModule import CHAT_TYPING_URL
from stariodemo.BasicStructsPkg.UrlsModule import GIVE_ME_JSON_URL
from stariodemo.BasicStructsPkg.UrlsModule import GIVE_ME_TEXT_URL
from stariodemo.BasicStructsPkg.UrlsModule import HOME_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import PLOTLY_GRAPH_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import SUBSCRIBE_TO_TOAST_NOTIFICATIONS_URL
from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_ADD_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_DETAILS_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_EDIT_PAGE_URL
from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_LIST_API_URL
from stariodemo.BasicStructsPkg.UrlsModule import WIDGET_LIST_PAGE_URL
from stariodemo.DatabasePiccoloTablesPkg.InitPiccoloDbModule import InitPiccoloDb
from stariodemo.FromTableDatabaseFunctionsPkg import PiccoloChatDb
from stariodemo.HandlersPkg.AbcAddPageEndpointModule import AbcAddPageEndpoint
from stariodemo.HandlersPkg.AbcCalculationEndpointModule import AbcCalculationEndpoint
from stariodemo.HandlersPkg.AbcCalculationPageEndpointModule import AbcCalculationPageEndpoint
from stariodemo.HandlersPkg.AbcListPageEndpointModule import AbcListPageEndpoint
from stariodemo.HandlersPkg.ApiCalculationEndpointModule import ApiCalculationEndpoint
from stariodemo.HandlersPkg.ChatPageEndpointModule import ChatPageEndpoint
from stariodemo.HandlersPkg.GiveMeJsonEndpointModule import GiveMeJsonEndpoint
from stariodemo.HandlersPkg.GiveMeTextEndpointModule import GiveMeTextEndpoint
from stariodemo.HandlersPkg.HomePageEndpointModule import HomePageEndpoint
from stariodemo.HandlersPkg.PlotlyGraphPageEndpointModule import PlotlyGraphPageEndpoint
from stariodemo.HandlersPkg.SendMessageEndpointModule import SendMessageEndpoint
from stariodemo.HandlersPkg.SubscribeEndpointModule import SubscribeEndpoint
from stariodemo.HandlersPkg.SubscribeToastNotificationsEndpointModule import SubscribeToToastNotificationsEndpoint
from stariodemo.HandlersPkg.ToastErrorEndpointModule import ToastErrorEndpoint
from stariodemo.HandlersPkg.ToastSuccessEndpointModule import ToastSuccessEndpoint
from stariodemo.HandlersPkg.TypingEndpointModule import TypingEndpoint
from stariodemo.HandlersPkg.WidgetAddPageEndpointModule import WidgetAddPageEndpoint
from stariodemo.HandlersPkg.WidgetDetailsPageEndpointModule import WidgetDetailsPageEndpoint
from stariodemo.HandlersPkg.WidgetEditPageEndpointModule import WidgetEditPageEndpoint
from stariodemo.HandlersPkg.WidgetListApiEndpointModule import WidgetListApiEndpoint
from stariodemo.HandlersPkg.WidgetListPageEndpointModule import WidgetListPageEndpoint
from stariodemo.StaticAssetsPkg.StaticAssetsModule import ASSETS


async def bootstrap(
    app: App,
    span: Span,
):
    span.event("stariodemo.startup.begin")
    # config = Config.from_env()

    # # remove any prior db
    # span.event("stariodemo.db.deleting.old")
    # if os.path.exists(SQLITE_DB_PATH):
    #     os.remove(SQLITE_DB_PATH)

    # Create database
    span.event("stariodemo.db.creating.new")
    await InitPiccoloDb()
    db = PiccoloChatDb()
    # await enable_wal()
    span.event("stariodemo.db.created.successfully")

    # await SeedWidget()

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

    app.get(WIDGET_ADD_PAGE_URL, WidgetAddPageEndpoint())
    app.get(WIDGET_LIST_PAGE_URL, WidgetListPageEndpoint())
    app.get(WIDGET_LIST_API_URL, WidgetListApiEndpoint())
    app.get(WIDGET_EDIT_PAGE_URL, WidgetEditPageEndpoint())
    app.get(WIDGET_DETAILS_PAGE_URL, WidgetDetailsPageEndpoint())

    # api
    app.get(API_CALCULATION_URL, ApiCalculationEndpoint())
    app.get(API_ABC_CALCULATION_URL, AbcCalculationEndpoint())

    app.get(GIVE_ME_TEXT_URL, GiveMeTextEndpoint())
    app.get(GIVE_ME_JSON_URL, GiveMeJsonEndpoint())
    app.get(PLOTLY_GRAPH_PAGE_URL, PlotlyGraphPageEndpoint())

    app.get(API_TOAST_SUCCESS_TEST_URL, ToastSuccessEndpoint(relay))
    app.get(API_TOAST_ERROR_TEST_URL, ToastErrorEndpoint(relay))
    app.get(SUBSCRIBE_TO_TOAST_NOTIFICATIONS_URL, SubscribeToToastNotificationsEndpoint(relay))

    span.event("stariodemo.startup.ready")

    yield

    span.attr("stariodemo.shutting.down", True)
    span.event("stariodemo.shutdown.begin")
    span.event("stariodemo.shutdown.complete")
