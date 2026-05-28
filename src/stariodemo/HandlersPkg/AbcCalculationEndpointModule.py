from stario import Context
from stario import Writer

from stariodemo.HtmlHtmlsPkg.CalculationResultBoxHtmlModule import CalculationResultBoxHtml


def AbcCalculationEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        path the abc result box
        """
        w.patch(
            CalculationResultBoxHtml(
                result="running calculation...",
            )
        )

    return handler
