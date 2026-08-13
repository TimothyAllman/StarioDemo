import plotly.graph_objects as go
from stario.markup import SafeString
from stario.markup.html import Div

from stariodemo.WebsiteFeatureHtmlComponentsPkg.BigTitleHtmlModule import BigTitleHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonMainMiddleSectionHtmlModule import CommonMainMiddleSectionHtml
from stariodemo.WebsiteFeatureHtmlComponentsPkg.CommonSidebarRightHtmlModule import CommonSidebarRightHtml


def PlotlyGraphHtml():
    """
    docstring
    """

    # 1. Define the data
    x_data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y_data = [10, 15, 13, 17, 22, 18, 25, 29, 24, 30]

    # 2. Create the figure
    fig = go.Figure()

    # 3. Add the line trace
    fig.add_trace(
        go.Scatter(
            x=x_data,
            y=y_data,
            mode="lines+markers",  # Combines lines and data point markers
            name="Trend A",  # Label for the legend
            line=dict(color="royalblue", width=3),  # Customizes line style
            marker=dict(size=8, symbol="circle"),  # Customizes marker style
        )
    )

    # 4. Update the layout
    fig.update_layout(
        title="Simple Line Graph Using Graph Objects",
        xaxis_title="X-Axis Label",
        yaxis_title="Y-Axis Label",
        template="plotly_white",  # Clean, minimalist background theme
    )

    graphHtml = fig.to_html(
        full_html=False,
    )

    return CommonMainMiddleSectionHtml(
        BigTitleHtml(
            title="PlotlyGraph",
        ),
        Div(
            SafeString(graphHtml),
        ),
        rightSidebar=CommonSidebarRightHtml(),
    )
