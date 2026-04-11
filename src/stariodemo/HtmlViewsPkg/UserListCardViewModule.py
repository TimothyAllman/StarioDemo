from stario.html import Div

from stariodemo.DataStructsPkg.UserModule import UserDto
from stariodemo.HtmlComponentsPkg.DemoAppButtonModule import DemoAppButton


def UserListCardView(
    user: UserDto,
):
    """
    docstring
    """

    return Div(
        {"class": "mt-3 bg-gray-100 p-4"},  # {"class": "bg-gray-100 p-4 border border-gray-800"},
        Div(
            {"class": "flex flex-row justify-between"},
            Div(f"name => {user.username}"),
            Div(f"ID =>{user.id}"),
            Div(f"color =>{user.color}"),
            DemoAppButton(f"press me for {user.username}", buttoncolor="yellow" if user.username == "trin" else "blue"),
        ),
    )
