from pydantic import BaseModel
from stario import Context
from stario import Writer
from stario import datastar

from stariodemo.WebsiteFeatureWidgetPkg.FromWidgetDbTableSelectManyItemsModule import FromWidgetDbTableSelectManyItems
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetListModule import WidgetListContentHtml
from stariodemo.WebsiteFeatureWidgetPkg.HtmlWidgetListModule import WidgetListNoContentHtml
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_LIST_PAGE_URL


class WidgetListApiSignals(BaseModel):
    widget_name_filter: str = ""
    widget_status_filter: str = ""


async def ReadWidgetListApiSignals(
    c: Context,
) -> WidgetListApiSignals:

    raw = await datastar.read_signals(
        c.req,
    )

    signals = WidgetListApiSignals.model_validate(raw)

    return signals


def WidgetListApiEndpoint():
    """
    docstring
    """

    async def handler(c: Context, w: Writer) -> None:

        signals = await ReadWidgetListApiSignals(c)

        widgets = await FromWidgetDbTableSelectManyItems(
            name_filter=signals.widget_name_filter or None,
            status_filter=signals.widget_status_filter or None,
        )

        sse = datastar.SSE(
            w,
        )

        sse.patch_elements(
            WidgetListContentHtml(
                widgets,
            )
            if widgets
            else WidgetListNoContentHtml()
        )

        newUrl = WIDGET_LIST_PAGE_URL.href(query={k: v for k, v in signals.model_dump().items() if v} or None)
        sse.execute_script(f"history.replaceState(null,'','{newUrl}')")

    return handler
