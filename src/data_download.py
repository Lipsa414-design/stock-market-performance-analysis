import yfinance as yf


def download_data(tickers, start, end):

    df = yf.download(
        tickers,
        start=start,
        end=end,
        group_by="ticker",
        auto_adjust=True
    )

    # wide → long format
    df = df.stack(level=0).reset_index()

    df.columns = [
        "Date",
        "Ticker",
        "Open",
        "High",
        "Low",
        "Close",
        "Volume"
    ]

    return df
