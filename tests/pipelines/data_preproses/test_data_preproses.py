"""
This is a boilerplate test file for pipeline 'data_preproses'
generated using Kedro 1.0.0.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

from zenitra_project_transaction_fraud.pipelines.data_preproses.nodes import (
    age_bins_column,
    recovery_days_columns,
)
import pandas as pd
from datetime import datetime

def sample_df():
    return pd.DataFrame({
        "CustomerAge": [20, 30, 50, 70],
        "TransactionDate": pd.to_datetime([
            "2024-01-10",
            "2024-01-20",
            "2024-02-01",
            "2024-02-10",
        ]),
        "PreviousTransactionDate": pd.to_datetime([
            "2024-01-05",
            "2024-01-15",
            "2024-01-25",
            "2024-02-01",
        ]),
    })


def test_age_bins_column():
    df = sample_df()
    df_out = age_bins_column(df)

    assert "AgeGroup" in df_out.columns
    assert df_out["AgeGroup"].dtype.name == "category"

    # Cek label yang dihasilkan sesuai mapping
    expected_labels = ["Gen Z", "Millennial", "Gen X", "Boomer"]
    assert list(df_out["AgeGroup"]) == expected_labels


def test_recovery_days_columns():
    df = sample_df()
    df_out = recovery_days_columns(df)

    assert "RecencyDays" in df_out.columns
    assert df_out["RecencyDays"].dtype == "int64"

    expected_days = [5, 5, 7, 9]  # selisih hari berdasarkan dummy sample_df()
    assert list(df_out["RecencyDays"]) == expected_days


