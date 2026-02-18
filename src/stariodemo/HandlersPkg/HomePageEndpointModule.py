import uuid

from stario import Context
from stario import Writer

from stariodemo.DataStructsPkg.GenerateColorModule import generate_color
from stariodemo.DataStructsPkg.GenerateUserNameModule import generate_username
from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlViewsPkg.ChatViewModule import chat_view
from stariodemo.HtmlViewsPkg.HomeViewModule import HomeView
from stariodemo.HtmlViewsPkg.NavBarAndFooterViewModule import NavBarAnfFooterView


def HomePageEndpoint(noDeps: None):
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve the home page
        """
        user_id = str(uuid.uuid4())[:8]
        username = generate_username()
        color = generate_color()

        # Pass empty collections - user will get real data after subscribing
        w.html(
            page(
                NavBarAnfFooterView(
                    HomeView(),
                )
            )
        )

    return handler
