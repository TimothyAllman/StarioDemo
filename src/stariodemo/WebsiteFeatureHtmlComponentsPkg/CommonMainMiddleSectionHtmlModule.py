from stario.markup.html import Div


def CommonMainMiddleSectionHtml(
    *children,
    rightSidebar,
):
    return Div(
        {
            "class": "flex flex-row items-stretch",
        },
        Div(
            {"class": "flex-1 min-w-0 m-3"},
            *children,
        ),
        rightSidebar,
    )
