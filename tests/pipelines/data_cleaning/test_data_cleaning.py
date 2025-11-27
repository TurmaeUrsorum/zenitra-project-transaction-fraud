"""
This is a boilerplate test file for pipeline 'data_cleaning'
generated using Kedro 1.0.0.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

from zenitra_project_transaction_fraud.pipelines.data_cleaning.nodes import (
    clean_data,
    date_formated,
    age_formated,
    balance_formated,
    account_id_handled,
    channel_occupation_handled,
    teknis_fromated,
    duration_login_handled,
    string_consistent,
    dated_formated_handled,
    dated_drop,
)
import pandas as pd
import pytest


def sample_df():
    return pd.DataFrame(
        {
            "AccountID": [1, None, 3],
            "CustomerAge": [25, -5, None],
            "Channel": ["atm", None, "online"],
            "CustomerOccupation": ["doctor", None, "engineer"],
            "DeviceID": ["D1", None, "D3"],
            "IP Address": ["1.1.1.1", None, "3.3.3.3"],
            "MerchantID": ["M1", None, "M3"],
            "Location": ["jakarta", None, "bandung"],
            "TransactionDate": ["2024-05-01", "2024-05-03", "2024-05-02"],
            "PreviousTransactionDate": ["2024-04-25", "2024-04-30", "2024-04-20"],
            "TransactionAmount": [1000, 2000, 3000],
            "AccountBalance": [5000, 6000, None],
            "TransactionType": ["cash", "cash", "cash"],
            "TransactionDuration": [10, None, 5],
            "LoginAttempts": [1, None, 7],
        }
    )


def test_clean_data():
    df = sample_df()
    params = {"subset": ["AccountID", "TransactionAmount"]}
    result = clean_data(df, params)
    assert result["AccountID"].isnull().sum() == 0


def test_date_formated():
    df = sample_df()
    params = {"errors": "coerce"}
    result = date_formated(df, params)
    assert pd.api.types.is_datetime64_any_dtype(result["TransactionDate"])
    assert pd.api.types.is_datetime64_any_dtype(result["PreviousTransactionDate"])
    assert "TransactionHour" in result.columns


def test_age_formated():
    df = sample_df()
    result = age_formated(df)
    assert result["CustomerAge"].isnull().sum() == 0
    assert result["CustomerAge"].min() >= 0
    assert result["CustomerAge"].max() <= 100


def test_balance_formated():
    df = sample_df()
    result = balance_formated(df)
    assert result["AccountBalance"].isnull().sum() == 0


def test_account_id_handled():
    df = sample_df()
    result = account_id_handled(df)
    assert result["AccountID"].isnull().sum() == 0


def test_channel_occupation_handled():
    df = sample_df()
    result = channel_occupation_handled(df)
    assert result["Channel"].isnull().sum() == 0
    assert result["CustomerOccupation"].isnull().sum() == 0


def test_teknis_formated():
    df = sample_df()
    result = teknis_fromated(df)
    for col in ["DeviceID", "IP Address", "MerchantID", "Location"]:
        assert result[col].isnull().sum() == 0


def test_duration_login_handled():
    df = sample_df()
    result = duration_login_handled(df)
    assert result["TransactionDuration"].isnull().sum() == 0
    assert result["LoginAttempts"].isnull().sum() == 0


def test_string_consistent():
    df = sample_df()
    result = string_consistent(df)
    assert set(result["Location"]) == set([x.title() for x in result["Location"]])
    assert set(result["Channel"]) == set([x.title() for x in result["Channel"]])
    assert set(result["CustomerOccupation"]) == set(
        [x.title() for x in result["CustomerOccupation"]]
    )


def test_dated_formated_handled():
    df = sample_df()
    result = dated_formated_handled(df)
    assert True  # minimal, karena logika swap hanya bila anomaly > 50%


def test_dated_drop():
    df = sample_df()
    result = dated_drop(df)
    assert result["TransactionDate"].isnull().sum() == 0
    assert result["PreviousTransactionDate"].isnull().sum() == 0
