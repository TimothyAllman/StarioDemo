from stario import Context
from stario import Writer


def ApiCalculationEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        w.json(
            {
                "message": "success",
            }
        )

    return handler
