from stario import at
from stario import data
from stario.html import Div
from stario.html import Input

from stariodemo.HtmlComponentsPkg.DemoAppButtonModule import DemoAppButton


def UserCreateView():
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
                data.bind("message"),
                data.on(
                    "keydown",
                    """
                if (evt.key === 'Enter' && !evt.shiftKey && $message.trim()) {
                    evt.preventDefault();
                    @post('/send');
                    $message = '';
                }
                """,
                ),
                data.on("input", at.post("/typing")),
            ),
            DemoAppButton(
                "Create",
            ),
        ),
    )
