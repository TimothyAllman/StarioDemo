import uuid

from stario import Context
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlViewsPkg.AbcAddViewModule import AbcAddView
from stariodemo.HtmlViewsPkg.AbcSidebarViewModule import AbcSideBarView
from stariodemo.HtmlViewsPkg.NavBarAndFooterViewModule import NavBarAnfFooterView


def AbcAddPageEndpoint(noDeps: None):
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        w.html(
            page(
                NavBarAnfFooterView(
                    AbcSideBarView(
                        AbcAddView(),
                    )
                )
            )
        )

    return handler
