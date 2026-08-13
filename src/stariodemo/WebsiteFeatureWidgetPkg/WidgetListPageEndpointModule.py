from pydantic import BaseModel
from stario import Context
from stario import Writer
from stario import responses

from stariodemo.WebsiteFeatureHtmlComponentsPkg.PageHtmlModule import PageHtml
from stariodemo.WebsiteFeatureCustomPkg.NavBarAndFooterHtmlModule import NavBarAndFooterHtml
from stariodemo.WebsiteFeatureWidgetPkg.WidgetListHtmlModule import WidgetListHtml
from stariodemo.WebsiteFeatureWidgetPkg.WidgetSidebarHtmlModule import WidgetSideBarHtml


class WidgetListPageSignals(BaseModel):
    widget_name_filter: str = ""
    widget_status_filter: str = ""


async def ReadWidgetListPageSignals(
    c: Context,
) -> WidgetListPageSignals:

    widget_name_filter = c.req.query.get("widget_name_filter", "")
    widget_status_filter = c.req.query.get("widget_status_filter", "")

    signals = WidgetListPageSignals(
        widget_name_filter=widget_name_filter,
        widget_status_filter=widget_status_filter,
    )

    return signals


def WidgetListPageEndpoint():
    """
    Serve abc list page
    """

    async def handler(c: Context, w: Writer) -> None:

        signals = await ReadWidgetListPageSignals(c)

        responses.html(
            w,
            PageHtml(
                NavBarAndFooterHtml(
                    WidgetSideBarHtml(
                        WidgetListHtml(
                            name_filter=signals.widget_name_filter,
                            status_filter=signals.widget_status_filter,
                        ),
                    )
                ),
            ),
        )

    return handler
