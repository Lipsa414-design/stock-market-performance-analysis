import pandas as pd
import numpy as np


def create_summary_report(df, sharpe, corr):

    report = {}

    report["Top Sharpe Stock"] = sharpe.idxmax()
    report["Top Sharpe Value"] = sharpe.max()

    report["Lowest Sharpe Stock"] = sharpe.idxmin()
    report["Lowest Sharpe Value"] = sharpe.min()

    corr_no_diag = corr.where(~np.eye(corr.shape[0], dtype=bool))
    max_corr = corr_no_diag.unstack().dropna().sort_values(ascending=False)

    top_pair = max_corr.index[0]

    report["Highest Correlation Pair"] = f"{top_pair[0]} - {top_pair[1]}"
    report["Highest Correlation Value"] = max_corr.iloc[0]

    return pd.DataFrame([report])
