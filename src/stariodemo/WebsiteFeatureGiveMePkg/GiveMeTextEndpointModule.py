from stario import Context
from stario import Writer
from stario import responses


def GiveMeTextEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
        """
        responses.text(
            w,
            "hi there",
        )

    return handler
