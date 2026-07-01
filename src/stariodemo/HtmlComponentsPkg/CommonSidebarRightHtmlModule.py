from stario import datastar
from stario.markup.html import Button
from stario.markup.html import Div
from stario.markup.html import P
from stario.markup.html import Span


def CommonSidebarRightHtml(
    *children,
):

    return Div(
        {
            "class": "shrink-0 flex flex-row items-stretch",
        },
        datastar.data.signals(
            {"rightSidebarOpen": False},
            if_missing=True,
        ),
        Button(
            {
                "class": " ".join(
                    [
                        "flex items-center justify-center h-12 w-8 self-center",
                        "text-white bg-slate-700 rounded-l-md",
                        "hover:bg-slate-900 transition",
                    ]
                ),
                "type": "button",
                "title": "Toggle right sidebar",
            },
            datastar.data.on("click", "$rightSidebarOpen=!$rightSidebarOpen"),
            Span(
                datastar.data.class_("block", "$rightSidebarOpen"),
                datastar.data.class_("hidden", "!$rightSidebarOpen"),
                ">>",
            ),
            Span(
                datastar.data.class_("hidden", "$rightSidebarOpen"),
                datastar.data.class_("block", "!$rightSidebarOpen"),
                "<<",
            ),
        ),
        Div(
            {
                "class": " ".join(
                    [
                        "min-h-screen bg-slate-100",
                        "transition-all duration-200 overflow-hidden",
                    ]
                )
            },
            datastar.data.classes(
                {
                    "w-[200px]": "$rightSidebarOpen",
                    "w-0": "!$rightSidebarOpen",
                }
            ),
            Div(
                {"class": "p-3"},
                Div(
                    datastar.data.show("$rightSidebarOpen"),
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
