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

/* Group 1 */
--color-backcolor1: var(--brand-backcolor1);
--color-backcolor1hover: var(--brand-backcolor1hover);
--color-edgecolor1: var(--brand-edgecolor1);
--color-frontcolor1: var(--brand-frontcolor1);

/* Group 2 */
--color-backcolor2: var(--brand-backcolor2);
--color-backcolor2hover: var(--brand-backcolor2hover);
--color-edgecolor2: var(--brand-edgecolor2);
--color-frontcolor2: var(--brand-frontcolor2);

/* Group 3 */
--color-backcolor3: var(--brand-backcolor3);
--color-backcolor3hover: var(--brand-backcolor3hover);
--color-edgecolor3: var(--brand-edgecolor3);
--color-frontcolor3: var(--brand-frontcolor3);
--color-frontcolor3hover: var(--brand-frontcolor3hover);

/* Group 4 */
--color-backcolor4: var(--brand-backcolor4);
--color-backcolor4hover: var(--brand-backcolor4hover);
--color-edgecolor4: var(--brand-edgecolor4);
--color-frontcolor4: var(--brand-frontcolor4);

/* Group 5 */
--color-backcolor5: var(--brand-backcolor5);
--color-backcolor5hover: var(--brand-backcolor5hover);
--color-edgecolor5: var(--brand-edgecolor5);
--color-frontcolor5: var(--brand-frontcolor5);
--color-frontcolor5hover: var(--brand-frontcolor5hover);


/* new ones above */
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
--color-backcolorinfo: var(--brand-backcolorinfo);
--color-edgecolorinfo: var(--brand-edgecolorinfo);
--color-frontcolorinfo: var(--brand-frontcolorinfo);
--color-backcolorsuccess: var(--brand-backcolorsuccess);
--color-edgecolorsuccess: var(--brand-edgecolorsuccess);
--color-frontcolorsuccess: var(--brand-frontcolorsuccess);
--color-backcolorwarning: var(--brand-backcolorwarning);
--color-edgecolorwarning: var(--brand-edgecolorwarning);
--color-frontcolorwarning: var(--brand-frontcolorwarning);
--color-backcolordanger: var(--brand-backcolordanger);
--color-edgecolordanger: var(--brand-edgecolordanger);
--color-frontcolordanger: var(--brand-frontcolordanger);
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

--brand-backcolor1: #ffffff;
--brand-backcolor1hover: #f8fafc;
--brand-edgecolor1: #e2e8f0;
--brand-frontcolor1: #0f172a;
--brand-backcolor2: #f8fafc;
--brand-backcolor2hover: #f1f5f9;
--brand-edgecolor2: #cbd5e1;
--brand-frontcolor2: #334155;
--brand-backcolor3: #eff6ff;
--brand-backcolor3hover: #dbeafe;
--brand-edgecolor3: #bfdbfe;
--brand-frontcolor3: #2563eb;
--brand-frontcolor3hover: #1d4ed8;
--brand-backcolor4: #f1f5f9;
--brand-backcolor4hover: #e2e8f0;
--brand-edgecolor4: #cbd5e1;
--brand-frontcolor4: #94a3b8;
--brand-backcolor5: #f0fdf4;
--brand-backcolor5hover: #dcfce7;
--brand-edgecolor5: #bbf7d0;
--brand-frontcolor5: #16a34a;
--brand-frontcolor5hover: #15803d;


/* new above */

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
--brand-backcolorinfo: #dbeafe;
--brand-edgecolorinfo: #3b82f6;
--brand-frontcolorinfo: #1e3a8a;
--brand-backcolorsuccess: #dcfce7;
--brand-edgecolorsuccess: #22c55e;
--brand-frontcolorsuccess: #166534;
--brand-backcolorwarning: #fef9c3;
--brand-edgecolorwarning: #eab308;
--brand-frontcolorwarning: #854d0e;
--brand-backcolordanger: #fee2e2;
--brand-edgecolordanger: #ef4444;
--brand-frontcolordanger: #991b1b;
--brand-bubble-other: #ffffff;
--brand-bubble-own: #fef3c7;
--brand-pattern-dot: #d6d3d1;
--brand-pattern-size: 24px 24px;
}
"""


SPECIFIC_COLORS_FOR_DARK_THEME_CSS = """
[data-theme="dark"]{

/* Primary Brand Group (Deep night canvas / crisp light text) */
--brand-backcolor1: #0f172a;        /* Deep slate background */
--brand-backcolor1hover: #1e293b;   /* Lighter slate on hover */
--brand-edgecolor1: #1e293b;        /* Subtle border definition */
--brand-frontcolor1: #f8fafc;       /* Off-white text for high contrast */

/* Secondary Brand Group (Elevated surfaces / cards) */
--brand-backcolor2: #1e293b;        /* Elevated card surface */
--brand-backcolor2hover: #334155;   /* Lighter surface on hover */
--brand-edgecolor2: #334155;        /* Card border */
--brand-frontcolor2: #cbd5e1;       /* Light gray secondary text */

/* Tertiary Brand Group (Vibrant accent highlights) */
--brand-backcolor3: #1e3a8a;        /* Deep navy accent background */
--brand-backcolor3hover: #2563eb;   /* Vibrant blue fill on hover */
--brand-edgecolor3: #3b82f6;        /* Bright blue border */
--brand-frontcolor3: #eff6ff;       /* Crisp ice-blue text */
--brand-frontcolor3hover: #ffffff;  /* Pure white text on hover */

/* Quaternary Brand Group (Disabled fields / inactive states) */
--brand-backcolor4: #020617;        /* Sunken, extra dark input fill */
--brand-backcolor4hover: #0f172a;   /* Subtle shift on hover */
--brand-edgecolor4: #1e293b;        /* Muted inactive border */
--brand-frontcolor4: #64748b;       /* Dark gray disabled text */

/* Quinary Brand Group (System alerts / positive success UI) */
--brand-backcolor5: #064e3b;        /* Deep emerald background */
--brand-backcolor5hover: #059669;   /* Bright emerald fill on hover */
--brand-edgecolor5: #10b981;        /* Vibrant green border */
--brand-frontcolor5: #ecfdf5;       /* Fresh mint success text */
--brand-frontcolor5hover: #ffffff;  /* Pure white text on hover */

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
--brand-backcolorinfo: #082f49;
--brand-edgecolorinfo: #38bdf8;
--brand-frontcolorinfo: #bae6fd;
--brand-backcolorsuccess: #052e16;
--brand-edgecolorsuccess: #16a34a;
--brand-frontcolorsuccess: #86efac;
--brand-backcolorwarning: #422006;
--brand-edgecolorwarning: #ca8a04;
--brand-frontcolorwarning: #fde68a;
--brand-backcolordanger: #450a0a;
--brand-edgecolordanger: #dc2626;
--brand-frontcolordanger: #fca5a5;
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
