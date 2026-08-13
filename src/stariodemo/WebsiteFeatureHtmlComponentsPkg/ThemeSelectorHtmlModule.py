from stario import datastar
from stario.markup.html import Option
from stario.markup.html import Select


def ThemeSelectorHtml():
    return Select(
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
    )
