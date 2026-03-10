from stario.html import Div

from stariodemo.HtmlComponentsPkg.MessageBoxModule import MessageBoxError
from stariodemo.HtmlComponentsPkg.MessageBoxModule import MessageBoxInfo
from stariodemo.HtmlComponentsPkg.MessageBoxModule import MessageBoxSuccess
from stariodemo.HtmlComponentsPkg.MessageBoxModule import MessageBoxWarning
from stariodemo.HtmlComponentsPkg.PlaneIconModule import PlaneIcon


def HomeView(
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
        MessageBoxInfo(),
        MessageBoxSuccess(),
        MessageBoxWarning(),
        MessageBoxError(),
        PlaneIcon() if showPlaneIsTrue else None,
    )
