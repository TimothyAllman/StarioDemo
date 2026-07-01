from stario.markup.html import Span


def ChatAppAvatarHtml(
    avatar_text: str,
    avatar_title,
    avatar_color,
):
    return Span(
        {
            "class": "avatar w-7 h-7 rounded-full flex items-center justify-center text-[0.7rem] font-semibold text-white border-2 border-surface -ml-2 cursor-default uppercase shadow-sm last:ml-0",
            "style": {
                "background-color": avatar_color,
            },
            "title": avatar_title,
        },
        avatar_text,
    )


def ChatAppAvatarMoreHtml(
    more_text: str,
):
    return Span(
        {
            "class": "avatar more w-7 h-7 rounded-full flex items-center justify-center font-semibold border-2 border-surface -ml-2 cursor-default uppercase shadow-sm last:ml-0 bg-border-strong text-muted text-[0.6rem]",
        },
        more_text,
    )
