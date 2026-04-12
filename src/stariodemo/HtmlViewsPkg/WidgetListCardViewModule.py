from stario.html import Div

from stariodemo.PiccoloPkg.WidgetDbModule import WidgetDto


def WidgetListCardView(
    widget: WidgetDto,
):
    """
    docstring
    """

    return Div(
        {"class": "mt-3 bg-gray-100 p-4"},  # {"class": "bg-gray-100 p-4 border border-gray-800"},
        Div(
            {"class": "flex flex-row justify-between"},
            Div(f"id => {widget.id}"),
            Div(f"title => {widget.title}"),
            Div(f"description =>{widget.description}"),
            Div(f"completed? =>{widget.is_completed}"),
            # DemoAppButton(f"press me for {widget.username}", buttoncolor="yellow" if widget.username == "trin" else "blue"),
        ),
    )
