from stario.markup.html import Div

from stariodemo.HtmlIconsPkg.IconAlertTriangleIconModule import IconAlertTriangleIcon
from stariodemo.HtmlIconsPkg.InfoCircleIconModule import InfoCircleIcon
from stariodemo.HtmlIconsPkg.MoodHappyIconModule import MoodHappyIcon
from stariodemo.HtmlIconsPkg.MoodSadIconModule import MoodSadIcon
from stariodemo.HtmlIconsPkg.PlaneIconModule import PlaneIcon


def MessageBoxHtml(
    title="message box",
    slot="slot content",
    icon=PlaneIcon(),
    classes="",
):
    return Div(
        {"class": "border-l-8 p-3 flex items-center space-x-4 " + classes},
        Div(
            # {"class": "flex-shrink-0"},
            icon,
        ),
        Div(
            Div(
                {"class": "font-bold"},
                title,
            ),
            slot,
        ),
    )


def MessageBoxInfoHtml(
    messageText="some more information",
):
    return MessageBoxHtml(
        title="Info",
        slot=messageText,
        icon=InfoCircleIcon(),
        classes="bg-backcolorinfo border-edgecolorinfo text-frontcolorinfo",
    )


def MessageBoxSuccessHtml(
    messageText="well done",
):
    return MessageBoxHtml(
        title="Success",
        slot=messageText,
        icon=MoodHappyIcon(),
        classes="bg-success-bg border-success-border text-success-fg",
    )


def MessageBoxErrorHtml(
    messageText="warning:",
):
    return MessageBoxHtml(
        title="Warning",
        slot=messageText,
        icon=IconAlertTriangleIcon(),
        classes="bg-warning-bg border-warning-edge text-warning-fg",
    )


def MessageBoxWarningHtml(
    messageText="An error occured",
):
    return MessageBoxHtml(
        title="Error",
        slot=messageText,
        icon=MoodSadIcon(),
        classes="bg-danger-bg border-danger-edge text-danger-fg",
    )
