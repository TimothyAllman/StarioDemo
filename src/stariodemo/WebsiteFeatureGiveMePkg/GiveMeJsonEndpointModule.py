from stario import Context
from stario import Writer
from stario import responses


def GiveMeJsonEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
        """
        responses.json(
            w,
            {"bank balance": 10000},
        )

    return handler
