def calculate_correlation(df):

    price_matrix = df.pivot(
        index="Date",
        columns="Ticker",
        values="Close"
    )

    return price_matrix.corr()
