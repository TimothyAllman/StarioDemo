from stario.markup.html import Div
from stario.markup.html import Input
from stario.markup.html import Label

from stariodemo.WebsiteFeatureHtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonActionButtonHtmlModule import CommonActionButtonHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_ADD_API_URL


def WidgetAddHtml():
    """
    Renders the Widget Add section using formless, naked inputs
    and direct button dispatch attributes passed via Python dictionaries.
    """
    return CommonMainMiddleSectionHtml(
        BigTitleHtml("Widget Add"),
        # 1. Parent container with an explicit ID dictionary
        Div(
            {"id": "widget-input-wrapper"},
            Label("Widget Name"),
            # Inputs with attributes passed via dictionaries
            Input({"name": "name", "type": "text", "required": "true"}),
            Label("Widget Age"),
            Input({"name": "age", "type": "number", "min": "0", "required": "true"}),
            # 2. Custom button accepting attributes for Datastar to scrape the inputs
            CommonActionButtonHtml(
                buttonText="Save new widget",
                buttonHref=WIDGET_ADD_API_URL.href(),
            ),
        ),
        rightSidebar=None,
    )
