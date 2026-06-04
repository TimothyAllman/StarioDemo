from stario.html import Span


def ChatAppHtml(
    avatar_text: str,
    avatar_title,
    avatar_color,
):
    return Span(
        {
            "class": "avatar w-7 h-7 rounded-full flex items-center justify-center text-[0.7em] font-semibold text-white border-2 border-surface -ml-2 cursor-default uppercase shadow-sm last:ml-0",
            "style": {
                "background-color": avatar_color,
            },
            "title": avatar_title,
        },
        avatar_text,
    )
