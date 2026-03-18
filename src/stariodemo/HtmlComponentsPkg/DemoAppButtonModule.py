from stario.html import Button


def DemoAppButton(*children):
    return Button(
        {
            "class": [
                "text-white font-semibold px-4 py-4 bg-blue-700",
                "hover:bg-blue-800 transition transform hover:scale-105",
            ]
        },
        *children,
    )
