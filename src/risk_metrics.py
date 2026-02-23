import numpy as np


def sharpe_ratio(df):

    returns = df.groupby("Ticker")["Close"].pct_change()

    temp = df.copy()
    temp["Returns"] = returns

    sharpe = (
        temp.groupby("Ticker")["Returns"]
        .mean()
        .div(temp.groupby("Ticker")["Returns"].std())
        * np.sqrt(252)
    )

    return sharpe
