import plotly.express as px


def plot_price(df, output_path, show_chart=False):

    fig = px.line(
        df,
        x="Date",
        y="Close",
        color="Ticker",
        title="Stock Price Trend"
    )

    fig.write_html(f"{output_path}/charts/price_trend.html")

    if show_chart:
        fig.show()


def plot_moving_average(df, output_path, show_chart=False):

    fig = px.line(
        df,
        x="Date",
        y=["Close", "MA_SHORT", "MA_LONG"],
        color="Ticker",
        title="Moving Average Analysis"
    )

    fig.write_html(f"{output_path}/charts/moving_average.html")

    if show_chart:
        fig.show()


def plot_daily_returns(df, output_path, show_chart=False):

    fig = px.histogram(
        df,
        x="Daily Return",
        color="Ticker",
        title="Daily Return Distribution"
    )

    fig.write_html(f"{output_path}/charts/daily_returns.html")

    if show_chart:
        fig.show()


def plot_faceted_area(df, output_path, show_chart=False):

    fig = px.area(
        df,
        x="Date",
        y="Close",
        color="Ticker",
        facet_col="Ticker",
        facet_col_wrap=2,
        labels={
            "Date": "Date",
            "Close": "Closing Price",
            "Ticker": "Company"
        },
        title="Stock Price Comparison (Faceted Area Chart)"
    )

    fig.write_html(
        f"{output_path}/charts/faceted_area_chart.html"
    )

    if show_chart:
        fig.show()


# =================================
# Chart registry (AUTO RUN ALL PLOTS)
# =================================

ALL_PLOTS = [
    plot_price,
    plot_moving_average,
    plot_daily_returns,
    plot_faceted_area
]
