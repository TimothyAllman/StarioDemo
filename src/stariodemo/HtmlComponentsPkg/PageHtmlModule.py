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

    --color-color1: #0e47a1; 
    --color-color11: #2365cf;
    --color-color111: #4287f5;

    --color-color2: #bd6004;
    --color-color22: #f2800f;
    --color-color222: #f2a85e;

    --color-color3: #fafaf9;
    --color-color33: #fafaf9;
    --color-color333: #fafaf9;

    --color-color4: #fafaf9;
    --color-color44: #fafaf9;
    --color-color444: #fafaf9;

    

    --color-bg: #fafaf9;
    --color-fg: #1c1917;
    --color-surface: #ffffff;
    --color-surface-hover: #fef3c7;
    --color-border: #e7e5e4;
    --color-border-strong: #d6d3d1;
    --color-accent: #f59e0b;
    --color-accent-light: #fbbf24;
    --color-accent-glow: rgba(245, 158, 11, 0.25);
    --color-accent-soft: #fef3c7;
    --color-muted: #78716c;

    --radius-custom: 10px;

    /* Chat-specific */
    --color-bubble-other: #ffffff;
    --color-bubble-own: #fef3c7;

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
        @apply bg-bg text-fg;

        /* Dotted pattern background like Stario */
        background-image: radial-gradient(circle, #d6d3d1 1px, transparent 1px);
        background-size: 24px 24px;
    }

    button:not(disabled),
    
    [role="button"]:not(:disabled){
        cursor: pointer;
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
            # Script({"src": "https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"}),
            # Script({"src": "https://unpkg.com/@tailwindcss/browser@4"}),
            # Style(
            #     {"type": "text/tailwindcss"},
            #     GLOBAL_CSS_STYLES,
            # ),
        ),
        Body(
            toy_inspector(position="bottom-right"),  # Dev tool: shows current signals state
            *children,
        ),
    )
