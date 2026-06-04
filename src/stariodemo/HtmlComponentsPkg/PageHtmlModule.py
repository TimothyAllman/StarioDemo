from stario.html import Body
from stario.html import Head
from stario.html import Html
from stario.html import Link
from stario.html import Meta
from stario.html import Script
from stario.html import Style
from stario.html import Title
from stario.toys import toy_inspector

GLOBAL_CSS_STYLES = """
@theme {
    --bg: #fafaf9;
    --fg: #1c1917;
    --surface: #ffffff;
    --surface-hover: #fef3c7;
    --border: #e7e5e4;
    --border-strong: #d6d3d1;
    --accent: #f59e0b;
    --accent-light: #fbbf24;
    --accent-glow: rgba(245, 158, 11, 0.25);
    --accent-soft: #fef3c7;
    --muted: #78716c;
    --radius: 10px;

    /* Chat-specific */
    --bg-bubble-other: #ffffff;
    --bg-bubble-own: #fef3c7;

}

@layer base{

    /* Tailwind v4 should do this for you via "preflight" but just in case we add it here */
    * {
        box-sizing: border-box;
        margin: 0;
        padding: 0;
    }

    html, body {
        height: 100%;
        font-family: system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
    }

    body {
        background: var(--bg);
        color: var(--fg);

        /* Dotted pattern background like Stario */
        background-image: radial-gradient(circle, #d6d3d1 1px, transparent 1px);
        background-size: 24px 24px;
    }

    button:not(disabled)
    [role="button"]:not(:disabled){
        cursor:pointer;
    }
}
"""


def PageHtml(
    *children,
):
    """
    Base HTML shell with Datastar loaded.

    """
    return Html(
        {"lang": "en"},
        Head(
            Meta({"charset": "UTF-8"}),
            Meta({"name": "viewport", "content": "width=device-width, initial-scale=1"}),
            Title("Template - Stario"),
            Link({"rel": "stylesheet", "href": "/static/css/style.css"}),
            Script({"type": "module", "src": "/static/js/datastar.js"}),
            # Script({"src": "https://cdn.tailwindcss.com"}), tailwind v3
            Script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"}),
            Style(
                {"type": "text/tailwindcss"},
                GLOBAL_CSS_STYLES,
            ),
        ),
        Body(
            toy_inspector(position="bottom-right"),  # Dev tool: shows current signals state
            *children,
        ),
    )
