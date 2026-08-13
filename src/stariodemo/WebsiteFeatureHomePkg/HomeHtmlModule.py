from stariodemo.BasicStructsPkg.UrlsModule import API_TOAST_ERROR_TEST_URL
from stariodemo.BasicStructsPkg.UrlsModule import API_TOAST_SUCCESS_TEST_URL
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonActionButtonHtmlModule import CommonActionButtonHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxErrorHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxInfoHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxSuccessHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.MessageBoxHtmlModule import MessageBoxWarningHtml
from stariodemo.WebsiteFeatureSvgIconsPkg.PlaneIconModule import PlaneIcon


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
