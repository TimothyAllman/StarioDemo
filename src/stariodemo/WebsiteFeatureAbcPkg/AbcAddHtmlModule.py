from stariodemo.WebsiteFeatureHtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml


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
