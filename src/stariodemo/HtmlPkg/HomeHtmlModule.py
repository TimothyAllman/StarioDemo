from stariodemo.DataStructsPkg.UrlsModule import API_TOAST_ERROR_TEST_URL
from stariodemo.DataStructsPkg.UrlsModule import API_TOAST_SUCCESS_TEST_URL
from stariodemo.HtmlComponentsPkg.CommonActionButtonHtmlModule import CommonActionButtonHtml
from stariodemo.HtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.HtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxErrorHtml
from stariodemo.HtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxInfoHtml
from stariodemo.HtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxSuccessHtml
from stariodemo.HtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxWarningHtml
from stariodemo.HtmlIconsPkg.PlaneIconModule import PlaneIcon


def HomeHtml(
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

    showPlaneIsTrue = False

    return CommonMainMiddleSectionHtml(
        MessageBoxInfoHtml(),
        MessageBoxSuccessHtml(),
        MessageBoxWarningHtml(),
        MessageBoxErrorHtml(),
        PlaneIcon() if showPlaneIsTrue else None,
        CommonActionButtonHtml(
            buttonText="Try Error",
            buttonHref=API_TOAST_ERROR_TEST_URL.href(),
        ),
        CommonActionButtonHtml(
            buttonText="Try Success",
            buttonHref=API_TOAST_SUCCESS_TEST_URL.href(),
        ),
        rightSidebar=None,
    )
