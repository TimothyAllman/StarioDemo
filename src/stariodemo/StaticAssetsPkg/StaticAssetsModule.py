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
/* different across themes */
--color-primary: var(--brand-primary);
--color-secondary: var(--brand-secondary);
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
/* eventually change this to backcolorinfo */
--color-info-bg: var(--brand-info-bg);
--color-info-border: var(--brand-info-border);
--color-info-fg: var(--brand-info-fg);
--color-success-bg: var(--brand-success-bg);
--color-success-border: var(--brand-success-border);
--color-success-fg: var(--brand-success-fg);
--color-warning-bg: var(--brand-warning-bg);
--color-warning-border: var(--brand-warning-border);
--color-warning-fg: var(--brand-warning-fg);
--color-danger-bg: var(--brand-danger-bg);
--color-danger-border: var(--brand-danger-border);
--color-danger-fg: var(--brand-danger-fg);
--color-pattern-dot: var(--brand-pattern-dot);
--color-pattern-size: var(--brand-pattern-size);


/* same across all themes */
/* colors */
--color-bubble-other: #ffffff;
--color-bubble-own: #fef3c7;

/* not colors */
--breakpoint-xs: 480px
--radius-custom: 10px;
--shadow-glow: 0 0 0 3px rgba(245, 158, 11, 0.25);

}
"""

SPECIFIC_COLORS_FOR_LIGHT_THEME_CSS = """
:root,
[data-theme="light"]{
--brand-primary: #113322;
--brand-secondary: #00bcd4;
--brand-bg: #fafaf9;
--brand-fg: #1c1917;
--brand-surface: #ffffff;
--brand-surface-hover: #fef3c7;
--brand-border-light: #e7e5e4;
--brand-border-strong: #d6d3d1;
--brand-accent: #f59e0b;
--brand-accent-light: #fbbf24;
--brand-accent-soft: #fef3c7;
--brand-muted: #78716c;
--brand-info-bg: #dbeafe;
--brand-info-border: #3b82f6;
--brand-info-fg: #1e3a8a;
--brand-success-bg: #dcfce7;
--brand-success-border: #22c55e;
--brand-success-fg: #166534;
--brand-warning-bg: #fef9c3;
--brand-warning-border: #eab308;
--brand-warning-fg: #854d0e;
--brand-danger-bg: #fee2e2;
--brand-danger-border: #ef4444;
--brand-danger-fg: #991b1b;
--brand-bubble-other: #ffffff;
--brand-bubble-own: #fef3c7;
--brand-pattern-dot: #d6d3d1;
--brand-pattern-size: 24px 24px;
}
"""


SPECIFIC_COLORS_FOR_DARK_THEME_CSS = """
[data-theme="dark"]{
--brand-primary: #113322;
--brand-secondary: #00bcd4;
--brand-bg: #0f172a;
--brand-fg: #e2e8f0;
--brand-surface: #111827;
--brand-surface-hover: #1f2937;
--brand-border-light: #334155;
--brand-border-strong: #475569;
--brand-accent: #38bdf8;
--brand-accent-light: #7dd3fc;
--brand-accent-soft: #082f49;
--brand-muted: #94a3b8;
--brand-info-bg: #082f49;
--brand-info-border: #38bdf8;
--brand-info-fg: #bae6fd;
--brand-success-bg: #052e16;
--brand-success-border: #16a34a;
--brand-success-fg: #86efac;
--brand-warning-bg: #422006;
--brand-warning-border: #ca8a04;
--brand-warning-fg: #fde68a;
--brand-danger-bg: #450a0a;
--brand-danger-border: #dc2626;
--brand-danger-fg: #fca5a5;
--brand-pattern-dot: #334155;
--brand-pattern-size: 50px 50px;
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
