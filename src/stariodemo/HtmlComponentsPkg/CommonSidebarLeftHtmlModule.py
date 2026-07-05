from stario import datastar
from stario.markup.html import Button
from stario.markup.html import Div
from stario.markup.html import Span


def CommonSidebarLeftHtml(
    navItems: list,
    *children,
):

    return Div(
        {"class": "flex flex-row"},
        datastar.data.signals(
            {"sidebarOpen": True},
            if_missing=True,
        ),
        Div(
            {"class": "min-h-screen bg-backcolor3 transition-all duration-200 overflow-hidden"},
            datastar.data.classes(
                {
                    "w-[200px]": "$sidebarOpen",
                    "w-0": "!$sidebarOpen",
                }
            ),
            Div(
                {"class": "p-3"},
                Div(
                    datastar.data.show("$sidebarOpen"),
                    Div(
                        {"class": "flex flex-col gap-2"},
                        *navItems,
                    ),
                ),
            ),
        ),
        Div(
            {"class": "min-h-screen flex items-center"},
            Button(
                {
                    "class": " ".join(
                        [
                            "flex items-center justify-center h-12 w-8",
                            "text-frontcolor4 bg-backcolor4 rounded-r-md",
                            "hover:bg-backcolor4hover transition",
                        ]
                    ),
                    "type": "button",
                    "title": "Toggle sidebar",
                },
                datastar.data.on("click", "$sidebarOpen=!$sidebarOpen"),
                Span(
                    datastar.data.class_("block", "$sidebarOpen"),
                    datastar.data.class_("hidden", "!$sidebarOpen"),
                    "<<",
                ),
                Span(
                    datastar.data.class_("hidden", "$sidebarOpen"),
                    datastar.data.class_("block", "!$sidebarOpen"),
                    ">>",
                ),
            ),
        ),
        Div(
            {"class": "flex-1 min-w-0"},
            *children,
        ),
    )
