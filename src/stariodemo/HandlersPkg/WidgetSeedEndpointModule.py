from stario import Context
from stario import Writer

from stariodemo.DataStructsPkg.UrlsModule import XYZ_LIST_PAGE_URL
from stariodemo.PiccoloPkg.SeedWidgetModule import SeedWidget


def WidgetSeedEndpoint():
    async def handler(c: Context, w: Writer) -> None:

        # Create some tasks
        await SeedWidget()

        w.redirect(XYZ_LIST_PAGE_URL)

        # w.empty(204)

    return handler
