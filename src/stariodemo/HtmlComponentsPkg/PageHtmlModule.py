from stario import datastar
from stario.debug import debug_inspector
from stario.markup.html import Body
from stario.markup.html import Head
from stario.markup.html import Html
from stario.markup.html import Link
from stario.markup.html import Meta
from stario.markup.html import Script
from stario.markup.html import Style
from stario.markup.html import Title

from stariodemo.StaticAssetsPkg.StaticAssetsModule import DATASTAR_JS
from stariodemo.StaticAssetsPkg.StaticAssetsModule import GLOBAL_CSS_STYLES
from stariodemo.StaticAssetsPkg.StaticAssetsModule import STYLE_CSS


def PageHtml(
    *children,
):
    """
    Base HTML shell with Datastar loaded.

    """
    return Html(
        {"lang": "en"},
        datastar.data.signals(
            {
                "theme": "light",
            },
            if_missing=True,
        ),
        datastar.data.attr(
            "data-theme",
            "$theme",
        ),
        Head(
            Meta({"charset": "UTF-8"}),
            Meta({"name": "viewport", "content": "width=device-width, initial-scale=1"}),
            Title("Template - Stario"),
            Link({"rel": "stylesheet", "href": STYLE_CSS}),
            Script({"type": "module", "src": DATASTAR_JS}),
            # Script({"src": "https://cdn.tailwindcss.com"}), tailwind v3
            Script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"}),
            # Script({"src": "https://unpkg.com/@tailwindcss/browser@4"}),
            Style(
                {"type": "text/tailwindcss"},
                GLOBAL_CSS_STYLES,
            ),
        ),
        Body(
            {
                "style": " ".join(
                    [
                        "background-color: var(--brand-backcolor1);",
                        "color: var(--brand-frontcolor1);",
                        "background-image: radial-gradient(circle, var(--bg-pattern-dot) 1px, transparent 1px);",
                        "background-size: var(--bg-pattern-size, 24px 24px);",
                    ]
                ),
            },
            debug_inspector(position="bottom-right"),  # Dev tool: shows current signals state
            *children,
        ),
    )
