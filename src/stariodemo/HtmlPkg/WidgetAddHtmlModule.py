from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml


def WidgetAddHtml():
    """
    docstring
    """

    return CommonMainMiddleSectionHtml(
        BigTitleHtml("add"),
        rightSidebar=None,
    )
