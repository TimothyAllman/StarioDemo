from stario import datastar
from stario.html import Button
from stario.html import Div
from stario.html import Span


def CommonSidebarLeftHtml(
    navItems: list,
    *children,
):

    return Div(
        {"class": "flex flex-row"},
        datastar.signals({"sidebarOpen": True}, ifmissing=True),
        Div(
            {"class": "min-h-screen bg-slate-100 transition-all duration-200 overflow-hidden"},
            datastar.classes(
                {
                    "w-[200px]": "$sidebarOpen",
                    "w-0": "!$sidebarOpen",
                }
            ),
            Div(
                {"class": "p-3"},
                Div(
                    datastar.show("$sidebarOpen"),
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
                    "class": ["flex items-center justify-center h-12 w-8", "text-white bg-slate-700 rounded-r-md", "hover:bg-slate-900 transition"],
                    "type": "button",
                    "title": "Toggle sidebar",
                },
                datastar.on("click", "$sidebarOpen=!$sidebarOpen"),
                Span(
                    datastar.class_("block", "$sidebarOpen"),
                    datastar.class_("hidden", "!$sidebarOpen"),
                    "<<",
                ),
                Span(
                    datastar.class_("hidden", "$sidebarOpen"),
                    datastar.class_("block", "!$sidebarOpen"),
                    ">>",
                ),
            ),
        ),
        Div(
            {"class": "flex-1 min-w-0"},
            *children,
        ),
    )
