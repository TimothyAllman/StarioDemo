from stario import Context
from stario import Writer
from stario import datastar

from stariodemo.HtmlHtmlsPkg.CalculationResultBoxHtmlModule import CalculationResultBoxHtml


def AbcCalculationEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        path the abc result box
        """
        datastar.sse.patch_elements(
            w,
            CalculationResultBoxHtml(
                result="running calculation...",
            ),
        )

    return handler
