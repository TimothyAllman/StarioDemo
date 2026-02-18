import uuid

from stario import Context
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlViewsPkg.AbcListViewModule import AbcListView
from stariodemo.HtmlViewsPkg.AbcSidebarViewModule import AbcSideBarView
from stariodemo.HtmlViewsPkg.NavBarAndFooterViewModule import NavBarAndFooterView


def AbcListPageEndpoint(noDeps: None):
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        w.html(
            page(
                NavBarAndFooterView(
                    AbcSideBarView(
                        AbcListView(),
                    )
                )
            )
        )

    return handler
