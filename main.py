"""
Stario Demo
"""

from stario import App
from stario import Relay
from stario import Span
from stario import StaticAssets

from stariodemo.DatabasePiccoloTablesPkg.InitPiccoloDbModule import InitPiccoloDb
from stariodemo.FromTableDatabaseFunctionsPkg import PiccoloChatDb
from stariodemo.WebsiteFeatureAbcPkg.AbcRegisterEndpointsModule import AbcRegisterEndpoints
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppRegisterEndpointsModule import ChatAppRegisterEndpoints
from stariodemo.WebsiteFeatureGiveMePkg.GiveMeRegisterEndpointsModule import GiveMeRegisterEndpoints
from stariodemo.WebsiteFeatureHomePkg.HomeRegisterEndpointsModule import HomeRegisterEndpoints
from stariodemo.WebsiteFeatureStaticAssetsPkg.StaticAssetsModule import ASSETS
from stariodemo.WebsiteFeatureToastNotificationsPkg.ToastNotificationsRegisterEndpointsModule import ToastNotificationsRegisterEndpoints
from stariodemo.WebsiteFeatureWidgetPkg.WidgetRegisterEndpointsModule import WidgetRegisterEndpoints


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

    # Routes - closures inject db/relay where needed
    span.event("stariodemo.registering.routes")
    HomeRegisterEndpoints(app)
    AbcRegisterEndpoints(app)
    ChatAppRegisterEndpoints(app, relay, db)
    WidgetRegisterEndpoints(app)
    GiveMeRegisterEndpoints(app)
    ToastNotificationsRegisterEndpoints(app, relay)

    span.event("stariodemo.startup.ready")

    yield

    span.attr("stariodemo.shutting.down", True)
    span.event("stariodemo.shutdown.begin")
    span.event("stariodemo.shutdown.complete")
