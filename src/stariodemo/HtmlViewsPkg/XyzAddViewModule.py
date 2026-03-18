from stario.html import Div

from stariodemo.HtmlViewsPkg.UserCreateViewModule import UserCreateView


def XyzAddView(
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

    return Div(
        Div("xyz Add"),
        UserCreateView(),
    )
