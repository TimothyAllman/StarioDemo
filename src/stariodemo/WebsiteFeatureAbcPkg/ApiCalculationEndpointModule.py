from stario import Context, responses
from stario import Writer


def ApiCalculationEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        responses.json(
            w,
            {
                "message": "success",
            },
        )

    return handler
