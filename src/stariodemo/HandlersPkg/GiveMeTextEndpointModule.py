from stario import Context
from stario import Writer


def GiveMeTextEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        w.text("hi there")

    return handler
