def add_moving_average(df, ma_short=10, ma_long=20):

    df["MA_SHORT"] = (
        df.groupby("Ticker")["Close"]
        .transform(lambda x: x.rolling(ma_short).mean())
    )

    df["MA_LONG"] = (
        df.groupby("Ticker")["Close"]
        .transform(lambda x: x.rolling(ma_long).mean())
    )

    return df


def add_daily_return(df):

    df["Daily Return"] = (
        df.groupby("Ticker")["Close"]
        .pct_change()
    )

    return df


def add_volatility(df, window=10):

    df["Volatility"] = (
        df.groupby("Ticker")["Daily Return"]
        .transform(lambda x: x.rolling(window).std())
    )

    return df
