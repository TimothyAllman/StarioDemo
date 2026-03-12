from stario import Context
from stario import Writer

from stariodemo.HtmlComponentsPkg.PageModule import page
from stariodemo.HtmlViewsPkg.AbcCalculationViewModule import AbcCalculationView
from stariodemo.HtmlViewsPkg.AbcListViewModule import AbcListView
from stariodemo.HtmlViewsPkg.AbcSidebarViewModule import AbcSideBarView
from stariodemo.HtmlViewsPkg.NavBarAndFooterViewModule import NavBarAndFooterView


def AbcCalculationPageEndpoint():
    async def handler(c: Context, w: Writer) -> None:
        """
        Serve abc list page
        """
        w.html(
            page(
                NavBarAndFooterView(
                    AbcSideBarView(
                        AbcCalculationView(),
                    )
                )
            )
        )

    return handler
