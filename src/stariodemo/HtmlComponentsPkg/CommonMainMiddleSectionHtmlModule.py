from stario.html import Div


def CommonMainMiddleSectionHtml(
    *children,
    rightSidebar,
):
    return Div(
        {
            "class": "flex flex-row gap-3 items-stretch",
        },
        Div(
            {"class": "flex-1 min-w-0 my-3"},
            *children,
        ),
        rightSidebar,
    )
