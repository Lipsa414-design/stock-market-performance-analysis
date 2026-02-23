from src.data_download import download_data
from src.indicators import (
    add_moving_average,
    add_daily_return,
    add_volatility
)
from src.analysis import calculate_correlation


def run_pipeline(config):

    df = download_data(
        config.TICKERS,
        config.START_DATE,
        config.END_DATE
    )

    df = add_moving_average(
        df,
        config.MA_SHORT,
        config.MA_LONG
    )

    df = add_daily_return(df)

    df = add_volatility(
        df,
        config.VOL_WINDOW
    )

    corr = calculate_correlation(df)

    return df, corr
