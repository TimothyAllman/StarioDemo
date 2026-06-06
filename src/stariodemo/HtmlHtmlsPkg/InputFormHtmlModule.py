from stario import datastar

from stariodemo.DataStructsPkg.UrlsModule import CHAT_TYPING_URL
from stariodemo.HtmlHtmlsPkg.ChatAppInputFormHtmlModule import ChatAppInputFormHtml
from stariodemo.HtmlHtmlsPkg.ChatAppMessageInputHtmlModule import ChatAppMessageInputHtml
from stariodemo.HtmlHtmlsPkg.ChatAppSendButtonHtmlModule import ChatAppSendButtonHtml
from stariodemo.HtmlHtmlsPkg.ChatAppSendIconHtmlModule import ChatAppSendIconHtml


def input_form_view():
    """
    Message input with keyboard and button support.

    Key Datastar patterns used here:
    - datastar.bind("message"): two-way binds input value to $message signal
    - datastar.on("keydown", ...): runs JS on keypress, @post triggers server request
    - datastar.attr({disabled: "!$message"}): reactively disables button when empty
    """
    return ChatAppInputFormHtml(
        datastar.on("submit", "evt.preventDefault()"),
        ChatAppMessageInputHtml(
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
            datastar.on("input", datastar.post(CHAT_TYPING_URL)),
        ),
        ChatAppSendButtonHtml(
            datastar.attr("disabled", "!$message"),
            datastar.on(
                "click",
                """
                if ($message.trim()) {
                    @post('/send');
                    $message = '';
                    document.getElementById('message-input').focus();
                }
                """,
            ),
            ChatAppSendIconHtml(),
        ),
    )
