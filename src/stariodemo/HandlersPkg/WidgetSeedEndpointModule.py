from stario import Context
from stario import Writer

from stariodemo.PiccoloPkg.SeedWidgetModule import SeedWidget


def WidgetSeedEndpoint():
    async def handler(c: Context, w: Writer) -> None:

        # Create some tasks
        await SeedWidget()

        w.empty(204)

    return handler
