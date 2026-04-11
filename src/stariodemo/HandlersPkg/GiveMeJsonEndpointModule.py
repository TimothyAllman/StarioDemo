from stario import Context
from stario import Writer


def GiveMeJsonEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        w.json({"bank balance": 10000})

    return handler
