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
        classes="bg-backcolorsuccess border-edgecolorsuccess text-frontcolorsuccess",
    )


def MessageBoxWarningHtml(
    messageText="warning:",
):
    return MessageBoxHtml(
        title="Warning",
        slot=messageText,
        icon=IconAlertTriangleIcon(),
        classes="bg-backcolorwarning border-edgecolorwarning text-frontcolorwarning",
    )


def MessageBoxErrorHtml(
    messageText="An error occurred",
):
    return MessageBoxHtml(
        title="Error",
        slot=messageText,
        icon=MoodSadIcon(),
        classes="bg-backcolordanger border-edgecolordanger text-frontcolordanger",
    )
