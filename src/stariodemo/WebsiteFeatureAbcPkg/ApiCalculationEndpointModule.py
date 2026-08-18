from stario import Context
from stario import Writer
from stario import responses


def ApiCalculationEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        docstring
        """
        responses.json(
            w,
            {
                "message": "success",
            },
        )

    return handler
