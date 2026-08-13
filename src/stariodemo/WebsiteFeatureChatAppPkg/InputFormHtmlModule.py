from stario import datastar

from stariodemo.WebsiteFeatureChatAppPkg.ChatAppInputFormHtmlModule import ChatAppInputFormHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppMessageInputHtmlModule import ChatAppMessageInputHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppSendButtonHtmlModule import ChatAppSendButtonHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppSendIconHtmlModule import ChatAppSendIconHtml
from stariodemo.WebsiteFeatureChatAppPkg.ChatAppUrlsModule import CHAT_TYPING_URL


def input_form_view():
    """
    Message input with keyboard and button support.

    Key Datastar patterns used here:
    - datastar.data.bind("message"): two-way binds input value to $message signal
    - datastar.data.on("keydown", ...): runs JS on keypress, @post triggers server request
    - datastar.data.attr({disabled: "!$message"}): reactively disables button when empty
    """
    return ChatAppInputFormHtml(
        datastar.data.on("submit", "evt.preventDefault()"),
        ChatAppMessageInputHtml(
            datastar.data.bind("message"),
            datastar.data.on(
                "keydown",
                """
                if (evt.key === 'Enter' && !evt.shiftKey && $message.trim()) {
                    evt.preventDefault();
                    @post('/send');
                    $message = '';
                }
                """,
            ),
            datastar.data.on("input", datastar.at.post(CHAT_TYPING_URL.href())),
        ),
        ChatAppSendButtonHtml(
            datastar.data.attr("disabled", "!$message"),
            datastar.data.on(
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
