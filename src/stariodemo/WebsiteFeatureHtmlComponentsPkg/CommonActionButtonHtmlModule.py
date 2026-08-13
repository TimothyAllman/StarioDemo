from stario import datastar
from stario.markup.html import Button


def CommonActionButtonHtml(buttonText, buttonHref):
    return Button(
        {
            "type": "button",
            "class": "bg-backcolor2 text-frontcolor2 border border-edgecolor2",
        },
        datastar.data.on(
            "click",
            datastar.at.get(buttonHref),
        ),
        buttonText,
    )
