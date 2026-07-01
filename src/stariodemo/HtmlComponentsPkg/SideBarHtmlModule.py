from stario.markup.html import Div


def SideBarHtml(
    *buttons,
):
    return Div(
        {"class": "flex flex-col"},
        [item for item in buttons],
    )
