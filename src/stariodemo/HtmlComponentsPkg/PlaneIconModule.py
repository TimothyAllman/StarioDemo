from stario.html import Div
from stario.html import G
from stario.html import Path
from stario.html import Svg


def PlaneIcon(strokeWidth=10):
    return Div(
        {"class": "flex-shrink-0"},
        Svg(
            {"viewBox": "0 0 512 512"},
            G(
                {"fill": "none", "stroke": "#000", "stroke-width": "20", "stroke-linejoin": "round"},
                # Path({"d": "M143.533 256 79.267 384.533v-192.8L497 127.467z"}),
                Path({"d": "M143.533 256 79.267 384.533l119.352-73.448zM15 127.467h482L79.267 191.733z"}),
                # Path({"d": "M143.533 256 497 127.467l-241 241z"}),
            ),
        ),
    )


# return Div(
#         {"class": "flex-shrink-0"},
#         SafeString(
#             f"""
#         <svg viewBox="0 0 512 512">
#         <g fill="none" stroke="#000" stroke-width="{strokeWidth}" stroke-linejoin="round">
#             <path d="M143.533 256 79.267 384.533v-192.8L497 127.467z"/>
#             <path d="M143.533 256 79.267 384.533l119.352-73.448zM15 127.467h482L79.267 191.733z"/>
#             <path d="M143.533 256 497 127.467l-241 241z"/>
#         </g>
#         </svg>
#             """
#         ),
#     )
