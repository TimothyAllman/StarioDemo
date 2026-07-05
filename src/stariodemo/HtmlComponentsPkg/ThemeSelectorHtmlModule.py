from stario import datastar
from stario.markup.html import Div
from stario.markup.html import Option
from stario.markup.html import Select
from stario.markup.html import Span


def ThemeSelectorHtml():
    return Div(
        {"class": "flex items-center bg-backcolor1 border border-frontcolor1 px-3 py-2 shadow-sm"},
        Span(
            {"class": "text-xs font-semibold text-frontcolor1"},
            "Theme",
        ),
        Select(
            {
                "id": "theme-selector",
                "class": "text-sm bg-backcolor1 text-frontcolor1 border border-frontcolor1 rounded px-2 py-1",
            },
            datastar.data.bind("theme"),
            datastar.data.on("change", "$theme=evt.target.value"),
            Option(
                {"value": "light"},
                "Light",
            ),
            Option(
                {"value": "dark"},
                "Dark",
            ),
            Option(
                {"value": "blue"},
                "Blue Light",
            ),
        ),
    )
