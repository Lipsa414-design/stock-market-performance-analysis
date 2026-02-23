import os
from datetime import datetime

import config

from src.pipeline import run_pipeline
from src.risk_metrics import sharpe_ratio
from src.report import create_summary_report
from src.plots import ALL_PLOTS


# ===============================
# Output folder with timestamp
# ===============================

timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

BASE_OUTPUT = f"outputs/{config.EXPERIMENT_NAME}_{timestamp}"

os.makedirs(f"{BASE_OUTPUT}/charts", exist_ok=True)
os.makedirs(f"{BASE_OUTPUT}/tables", exist_ok=True)


# ===============================
# Run pipeline
# ===============================

data, corr = run_pipeline(config)


# ===============================
# Risk metrics
# ===============================

sharpe = sharpe_ratio(data)

print("\nSharpe Ratio:")
print(sharpe)


# ===============================
# Summary report
# ===============================

summary = create_summary_report(data, sharpe, corr)

print("\nSummary Report:")
print(summary)


# ===============================
# Save outputs
# ===============================

corr.to_csv(f"{BASE_OUTPUT}/tables/correlation_matrix.csv")
sharpe.to_csv(f"{BASE_OUTPUT}/tables/sharpe_ratio.csv")
summary.to_csv(
    f"{BASE_OUTPUT}/tables/summary_report.csv",
    index=False
)


# ===============================
# Generate charts (AUTO LOOP)
# ===============================

if config.SAVE_CHARTS:

    for plot_func in ALL_PLOTS:
        plot_func(
            data,
            BASE_OUTPUT,
            config.SHOW_CHARTS
        )


print(f"\nOutputs saved to: {BASE_OUTPUT}")
