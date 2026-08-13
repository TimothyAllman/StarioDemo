from __future__ import annotations

import json

SESSION_STORAGE_KEY_THEME = "mytheme"
DEFAULT_THEME = "light"
VALID_THEMES = ("light", "dark", "blue")


def ValidateTheme(theme: str) -> str:
    if theme in VALID_THEMES:
        return theme
    return DEFAULT_THEME


THEME_INIT_JS = f"""
(() => {{
    const themeKey = {json.dumps(SESSION_STORAGE_KEY_THEME)};

    // Restore theme from session storage
    try {{
    const raw = sessionStorage.getItem(themeKey);
        if (raw) {{
            const theme = JSON.parse(raw);

            if (theme) {{ 
                $theme = theme;
                }} else {{
                $theme = {json.dumps(DEFAULT_THEME)};
                }}
            }}else {{
            $theme = {json.dumps(DEFAULT_THEME)};
            }}
    }} catch {{
         $theme = {json.dumps(DEFAULT_THEME)};
    }}

    // watch for theme changes and save to sessionStorage
    let lastTheme = $theme;
    setInterval(()=> {{
        
        if ($theme !== lastTheme) {{
        lastTheme = $theme;
        try {{
                sessionStorage.setItem(themeKey, JSON.stringify($theme))
            }}catch{{
                //do nothing
            }}
        }}

    }},100);
}}
)();
"""

# USERNAME_INIT_JS = f"""
# (() => {{
#     const themeKey = {json.dumps(SESSION_STORAGE_KEY_THEME)}

#     // Restore theme from session storage
#     try {{
#     const raw = sessionStorage.getitem(themeKey);
#     if (raw) {{
#         const theme = JSON.parse(raw);

#         if (theme) {{
#             $theme = theme;
#             }} else {{
#             $theme = {json.dumps(DEFAULT_THEME)};
#             }}

#         }}else {{
#         $theme = {json.dumps(DEFAULT_THEME)};
#         }}
#     }} catch {{
#          $theme = {json.dumps(DEFAULT_THEME)};
#     }}
# }}
# )
# """
