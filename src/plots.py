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
