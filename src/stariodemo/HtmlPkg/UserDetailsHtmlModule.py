from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml


def WidgetDetailsHtml():
    """
    docstring
    """

    return CommonMainMiddleSectionHtml(
        BigTitleHtml("details"),
        rightSidebar=None,
    )
