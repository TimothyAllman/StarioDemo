from stario import datastar
from stario.markup.html import Div
from stario.markup.html import Option
from stario.markup.html import Select
from stario.markup.html import Span


def ThemeSelectorHtml():
    return Div(
        {"class": "flex items-center bg-surface border border-border-light px-3 py-2 shadow-sm"},
        Span(
            {"class": "text-xs font-semibold text-muted"},
            "Theme",
        ),
        Select(
            {
                "id": "theme-selector",
                "class": "text-sm bg-surface text-fg border border-border-strong rounded px-2 py-1",
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
        ),
    )
