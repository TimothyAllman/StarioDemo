from stario import datastar
from stario.html import Button
from stario.html import Div
from stario.html import P
from stario.html import Span


def CommonSidebarRightHtml(
    *children,
):

    return Div(
        {
            "class": "shrink-0 flex flex-row items-stretch",
        },
        datastar.signals({"rightSidebarOpen": False}, ifmissing=True),
        Button(
            {
                "class": [
                    "flex items-center justify-center h-12 w-8 self-center",
                    "text-white bg-slate-700 rounded-l-md",
                    "hover:bg-slate-900 transition",
                ],
                "type": "button",
                "title": "Toggle right sidebar",
            },
            datastar.on("click", "$rightSidebarOpen=!$rightSidebarOpen"),
            Span(
                datastar.class_("block", "$rightSidebarOpen"),
                datastar.class_("hidden", "!$rightSidebarOpen"),
                ">>",
            ),
            Span(
                datastar.class_("hidden", "$rightSidebarOpen"),
                datastar.class_("block", "!$rightSidebarOpen"),
                "<<",
            ),
        ),
        Div(
            {
                "class": [
                    "min-h-screen bg-slate-100",
                    "transition-all duration-200 overflow-hidden",
                ]
            },
            datastar.classes(
                {
                    "w-[200px]": "$rightSidebarOpen",
                    "w-0": "!$rightSidebarOpen",
                }
            ),
            Div(
                {"class": "p-3"},
                Div(
                    datastar.show("$rightSidebarOpen"),
                    Div(
                        {"class": "flex flex-col gap-2"},
                        *children
                        if children
                        else [
                            P(
                                {"class": "text-sm text-gray-600 text-center"},
                                "No extra actions",
                            )
                        ],
                    ),
                ),
            ),
        ),
    )
