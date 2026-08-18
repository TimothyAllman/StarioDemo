from stario import datastar
from stario.markup.html import Div
from stario.markup.html import Input
from stario.markup.html import Label

from stariodemo.WebsiteFeatureHtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonActionButtonHtmlModule import CommonActionButtonHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.WebsiteFeatureWidgetPkg.UrlsWidgetModule import WIDGET_ADD_API_URL


def WidgetAddHtml():
    """
    Renders the Widget Add section using formless inputs bound to Datastar signals.
    """
    return CommonMainMiddleSectionHtml(
        BigTitleHtml("Widget Add"),
        Div(
            {"id": "widget-input-wrapper"},
            # Initialize empty signal states for your input bindings
            datastar.data.signals(
                {
                    "name": "",
                    "age": "",
                },
                if_missing=True,
            ),
            Label("Widget Name"),
            Div(
                Input(
                    {
                        "type": "text",
                        "required": "true",
                    },
                    # Synchronises input values with the "name" signal state
                    datastar.data.bind("name"),
                ),
            ),
            Label("Widget Age"),
            Div(
                Input(
                    {
                        "type": "number",
                        "min": "0",
                        "required": "true",
                    },
                    # Synchronises input values with the "age" signal state
                    datastar.data.bind("age"),
                ),
            ),
            # Direct dispatch action to send the payload to the backend
            CommonActionButtonHtml(
                buttonText="Save new widget",
                buttonHref=WIDGET_ADD_API_URL.href(),
                # Note: Ensure CommonActionButtonHtml accepts or routes Datastar
                # triggers like datastar.data.on("click", datastar.at.post(...))
                # if you aren't relying on standard anchor navigation tags.
            ),
        ),
        rightSidebar=None,
    )
