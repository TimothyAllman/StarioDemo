from stario.markup.html import Div
from stario.markup.html import P

from stariodemo.HandlersPkg.WidgetDeleteEndpointModule import WIDGET_DELETE_URL
from stariodemo.HtmlComponentsPkg.CommonActionButtonHtmlModule import CommonActionButtonHtml


def WidgetCardHtml(
    widgetDto,
):
    return Div(
        {"class": "border rounded p-4 bg-backcolor1 text-frontcolor1 border-edgecolor1 shadow-sm mb-3"},
        Div(
            {"class:": "flex items center justify-between"},
            P(
                {"class": "text-lg font-semibold"},
                f"{widgetDto.id} - {widgetDto.name}",
            ),
            P(
                {"class": "text-lg font-semibold"},
                f"{widgetDto.name}",
            ),
        ),
        Div(
            {"class": "grid grid-cols-1 md:grid-cols-3 gap-2 mt-3"},
            P(
                {"class": "text-sm"},
                f"Address: {widgetDto.name}",
            ),
            P(
                {"class": "text-sm"},
                f"number: {widgetDto.username}",
            ),
        ),
        Div(
            {"class": "flex items-center justify-between mt-3"},
            # RedirectButtonHtml(
            #     name=,
            #     url=details_url
            # )
            "GoToView",
        ),
        CommonActionButtonHtml(
            buttonText="delete",
            buttonHref=WIDGET_DELETE_URL.href(id=widgetDto.id),
        ),
    )
