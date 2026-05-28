from stario import Context
from stario import Writer
from stario import responses


def GiveMeJsonEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        responses.json(
            w,
            {"bank balance": 10000},
        )

    return handler
