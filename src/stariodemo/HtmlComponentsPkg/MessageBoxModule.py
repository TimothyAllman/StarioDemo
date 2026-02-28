from stario.html import H1
from stario.html import Div

from stariodemo.HtmlComponentsPkg.PlaneIconModule import PlaneIcon


def MessageBox(
    title="message box",
    slot="slot content",
    classes="",
):
    return Div(
        {"class": "border-l-8 p-3 flex items-center space-x-4 " + classes},
        # PlaneIcon(),
        Div(
            # {"class": "flex-shrink-0"},
            PlaneIcon(),
        ),
        Div(
            Div(
                {"class": "font-bold"},
                title,
            ),
            slot,
        ),
    )


def MessageBoxInfo(messageText="some more information"):
    return MessageBox(
        title="Info",
        slot=messageText,
        classes="bg-blue-100 border-blue-500 text-blue-700",
    )


def MessageBoxSuccess(messageText="well done"):
    return MessageBox(
        title="Success",
        slot=messageText,
        classes="bg-green-100 border-green-500 text-green-700",
    )


def MessageBoxError(messageText="warning:"):
    return MessageBox(
        title="Warning",
        slot=messageText,
        classes="bg-yellow-100 border-yellow-500 text-yellow-700",
    )


def MessageBoxWarning(messageText="An error occured"):
    return MessageBox(
        title="Error",
        slot=messageText,
        classes="bg-red-100 border-red-500 text-red-700",
    )
