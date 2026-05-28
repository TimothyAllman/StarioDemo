
from stario import datastar
from stario.html import Div
from stario.html import Input

from stariodemo.HtmlComponentsPkg.DemoAppButtonHtmlModule import DemoAppButtonHtml


def UserCreateHtml():
    """
    docstring
    """

    return Div(
        {"class": "mt-3 bg-gray-100 p-4"},  # {"class": "bg-gray-100 p-4 border border-gray-800"},
        Div(
            # {"class": "flex flex-row justify-between"},
            Input(
                {
                    "id": "message-input",
                    "type": "text",
                    "class": "message-input",
                    "placeholder": "Type a message...",
                    "autocomplete": "off",
                    "autofocus": True,
                },
                datastar.bind("message"),
                datastar.on(
                    "keydown",
                    """
                if (evt.key === 'Enter' && !evt.shiftKey && $message.trim()) {
                    evt.preventDefault();
                    @post('/send');
                    $message = '';
                }
                """,
                ),
                datastar.on("input", datastar.post("/typing")),
            ),
            DemoAppButtonHtml(
                "Create",
            ),
        ),
    )
