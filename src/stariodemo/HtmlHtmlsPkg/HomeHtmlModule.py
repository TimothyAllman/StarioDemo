from stario.html import Div

from stariodemo.HtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxErrorHtml
from stariodemo.HtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxInfoHtml
from stariodemo.HtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxSuccessHtml
from stariodemo.HtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxWarningHtml
from stariodemo.HtmlIconsPkg.PlaneIconModule import PlaneIcon


def HomeHtml(
    # user_id: str,
    # username: str,
    # color: str,
    # *,
    # messages: list[Message],
    # users: dict[str, User],
):
    """
    docstring
    """

    showPlaneIsTrue = False

    return Div(
        MessageBoxInfoHtml(),
        MessageBoxSuccessHtml(),
        MessageBoxWarningHtml(),
        MessageBoxErrorHtml(),
        PlaneIcon() if showPlaneIsTrue else None,
    )
