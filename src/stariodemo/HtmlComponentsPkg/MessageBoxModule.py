from stario.html import Div

from stariodemo.HtmlIconsPkg.IconAlertTriangleIconModule import IconAlertTriangleIcon
from stariodemo.HtmlIconsPkg.InfoCircleIconModule import InfoCircleIcon
from stariodemo.HtmlIconsPkg.MoodHappyIconModule import MoodHappyIcon
from stariodemo.HtmlComponentsPkg.MoodSadIconModule import MoodSadIcon
from stariodemo.HtmlIconsPkg.PlaneIconModule import PlaneIcon


def MessageBox(
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


def MessageBoxInfo(
    messageText="some more information",
):
    return MessageBox(
        title="Info",
        slot=messageText,
        icon=InfoCircleIcon(),
        classes="bg-blue-100 border-blue-500 text-blue-700",
    )


def MessageBoxSuccess(
    messageText="well done",
):
    return MessageBox(
        title="Success",
        slot=messageText,
        icon=MoodHappyIcon(),
        classes="bg-green-100 border-green-500 text-green-700",
    )


def MessageBoxError(
    messageText="warning:",
):
    return MessageBox(
        title="Warning",
        slot=messageText,
        icon=IconAlertTriangleIcon(),
        classes="bg-yellow-100 border-yellow-500 text-yellow-700",
    )


def MessageBoxWarning(
    messageText="An error occured",
):
    return MessageBox(
        title="Error",
        slot=messageText,
        icon=MoodSadIcon(),
        classes="bg-red-100 border-red-500 text-red-700",
    )
