from stariodemo.HtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.HtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml


def AbcAddHtml(
    # user_id: str,
    # username: str,
    # color: str,
    # *,
    # messages: list[Message],
    # users: dict[str, Widget],
):
    """
    docstring
    """

    return CommonMainMiddleSectionHtml(
        BigTitleHtml("abc add"),
        rightSidebar=CommonSidebarRightHtml(),
    )
