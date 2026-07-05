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
@import "tailwindcss";

@theme {
    --color-bg: var(--brand-bg);
    --color-fg: var(--brand-fg);
    --color-surface: var(--brand-surface);
    --color-surface-hover: var( --brand-surface);
    --color-border: var( --brand-border);
    --color-border-strong: var( --brand-border);
    --color-accent: var( --brand-accent);
    --color-accent-light: var( --brand-accent);
    --color-accent-glow: var( --brand-accent);
    --color-accent-soft: var( --brand-accent);
    --color-muted: var( --brand-muted);

   
    /* same across all themes */
    --color-bubble-other: #ffffff;
    --color-bubble-own: #fef3c7;
    --radius-custom: 10px;
    --shadow-glow: 0 0 0 3px rgba(245, 158, 11, 0.25);

}
"""

SPECIFIC_COLORS_FOR_LIGHT_THEME_CSS = """
:root,
[data-theme="light"]{
--brand-primary: #113322;
--brand-secondary: #113322;
--brand-bg: #113322;
--brand-fg: #113322;
--brand-surface: #113322;
--brand-surface: #113322;
--brand-border: #113322;
--brand-border: #113322;
--brand-accent: #113322;
--brand-accent: #113322;
--brand-accent: #113322;
--brand-accent: #113322;
--brand-muted: #113322;
}
"""

SPECIFIC_COLORS_FOR_DARK_THEME_CSS = """
[data-theme="dark"]{
--brand-primary: #113322;
--brand-secondary: #113322;
--brand-bg: #113322;
--brand-fg: #113322;
--brand-surface: #113322;
--brand-surface: #113322;
--brand-border: #113322;
--brand-border: #113322;
--brand-accent: #113322;
--brand-accent: #113322;
--brand-accent: #113322;
--brand-accent: #113322;
--brand-muted: #113322;
}
"""

BASE_NON_THEME_TAILWIND_V4_PREFLIGHT_DEFAULTS_CSS = """
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
        SPECIFIC_COLORS_FOR_LIGHT_THEME_CSS,
        SPECIFIC_COLORS_FOR_DARK_THEME_CSS,
        BASE_NON_THEME_TAILWIND_V4_PREFLIGHT_DEFAULTS_CSS,
        LAYER_BASE_CLOSING_BRACKET,
    ]
)
