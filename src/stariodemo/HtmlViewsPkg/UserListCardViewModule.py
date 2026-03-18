from stario.html import Div

from stariodemo.DataStructsPkg.UserModule import User


def UserListCardView(
    user: User,
):
    """
    docstring
    """

    return Div(
        Div(user.username),
        Div(user.id),
        Div(user.color),
    )
