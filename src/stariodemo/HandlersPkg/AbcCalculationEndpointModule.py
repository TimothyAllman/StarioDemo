from stario import Context
from stario import Writer

from stariodemo.HtmlViewsPkg.CalculationResultBoxViewModule import CalculationResultBoxView


def AbcCalculationEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        path the abc result box
        """
        w.patch(
            CalculationResultBoxView(
                result="running calculation...",
            )
        )

    return handler
