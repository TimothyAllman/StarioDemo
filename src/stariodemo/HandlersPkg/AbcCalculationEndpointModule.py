from stario import Context
from stario import Writer
from stario.datastar import SSE

from stariodemo.HtmlPkg.CalculationResultBoxHtmlModule import CalculationResultBoxHtml


def AbcCalculationEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        path the abc result box
        """
        sse = SSE(w)
        sse.patch_elements(
            CalculationResultBoxHtml(
                result="running calculation...",
            ),
        )

    return handler
