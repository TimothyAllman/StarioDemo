from stario.html import Div


def ChatAppChatEmptyStateHtml():
    return Div(
        {
            "class": [
                "empty-state text-muted text-[0.9rem] p-8 text-center bg-surface rounded-[10px] border border-border-light",
            ]
        },
        "No messages yet. Say hello!",
    )
