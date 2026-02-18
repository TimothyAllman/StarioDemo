import time

from stario import asset
from stario import at
from stario import data
from stario.html import Body
from stario.html import Button
from stario.html import Div
from stario.html import Form
from stario.html import Head
from stario.html import Html
from stario.html import Input
from stario.html import Link
from stario.html import Meta
from stario.html import SafeString
from stario.html import Script
from stario.html import Span
from stario.html import Title
from stario.toys import toy_inspector

from stariodemo.DataStructsPkg.MessageModule import Message
from stariodemo.DataStructsPkg.UserModule import User


def input_form_view():
    """
    Message input with keyboard and button support.

    Key Datastar patterns used here:
    - data.bind("message"): two-way binds input value to $message signal
    - data.on("keydown", ...): runs JS on keypress, @post triggers server request
    - data.attr({disabled: "!$message"}): reactively disables button when empty
    """
    return Form(
        {"id": "input-form", "class": "input-form"},
        data.on("submit", "evt.preventDefault()"),
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
        Button(
            {
                "type": "button",
                "class": "send-button",
            },
            data.attr({"disabled": "!$message"}),
            data.on(
                "click",
                """
                if ($message.trim()) {
                    @post('/send');
                    $message = '';
                    document.getElementById('message-input').focus();
                }
                """,
            ),
            Span(
                {"class": "send-icon"},
                SafeString(
                    """<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M14.536 21.686a.5.5 0 0 0 .937-.024l6.5-19a.496.496 0 0 0-.635-.635l-19 6.5a.5.5 0 0 0-.024.937l7.93 3.18a2 2 0 0 1 1.112 1.11z"/><path d="m21.854 2.147-10.94 10.939"/></svg>"""
                ),
            ),
        ),
    )
