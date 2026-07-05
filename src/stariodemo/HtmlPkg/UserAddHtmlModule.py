from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml


def UserAddHtml():
    """
    docstring
    """

    return CommonMainMiddleSectionHtml(
        BigTitleHtml("add"),
        rightSidebar=None,
    )
