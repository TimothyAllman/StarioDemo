"""Shared static assets for the chat-room example."""

from pathlib import Path

from stario import AssetManifest

# Cheap at import time: scan + fingerprint only. Serving (compression, caching)
# is paid in bootstrap when StaticAssets wraps the manifest.
ASSETS = AssetManifest(
    Path(__file__).resolve().parent.parent / "static",
)
STYLE_CSS = ASSETS.href("/css/style.css")
DATASTAR_JS = ASSETS.href("/js/datastar.js")

# custom CSS stuff
PLACEHOLDER_TAILWIND_V4_TOKENS_FOR_USE_IN_HTML = """
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
"""


BASE_CSS = """
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
"""

LAYER_BASE_OPENING_BRACKET = """
@layer base{
"""

LAYER_BASE_CLOSING_BRACKET = """
}
"""

GLOBAL_CSS_STYLES = "\n\n".join(
    [
        PLACEHOLDER_TAILWIND_V4_TOKENS_FOR_USE_IN_HTML,
        LAYER_BASE_OPENING_BRACKET,
        BASE_CSS,
        LAYER_BASE_CLOSING_BRACKET,
    ]
)
