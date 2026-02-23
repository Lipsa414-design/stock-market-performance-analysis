import os
from datetime import datetime

import config

from src.pipeline import run_pipeline
from src.risk_metrics import sharpe_ratio
from src.report import create_summary_report
from src.plots import plot_price


# output folder (timestamped)
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

BASE_OUTPUT = f"outputs/{config.EXPERIMENT_NAME}_{timestamp}"

os.makedirs(f"{BASE_OUTPUT}/charts", exist_ok=True)
os.makedirs(f"{BASE_OUTPUT}/tables", exist_ok=True)


# run analysis
data, corr = run_pipeline(config)

sharpe = sharpe_ratio(data)

summary = create_summary_report(data, sharpe, corr)


# save tables
corr.to_csv(f"{BASE_OUTPUT}/tables/correlation_matrix.csv")
sharpe.to_csv(f"{BASE_OUTPUT}/tables/sharpe_ratio.csv")
summary.to_csv(f"{BASE_OUTPUT}/tables/summary_report.csv", index=False)


# charts
if config.SAVE_CHARTS:
    plot_price(
        data,
        BASE_OUTPUT,
        config.SHOW_CHARTS
    )

print(f"Outputs saved to: {BASE_OUTPUT}")
