"""
This is a boilerplate test file for pipeline 'data_EDA'
generated using Kedro 1.0.0.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""

from zenitra_project_transaction_fraud.pipelines.data_EDA.nodes import (
    analisis_univariat,
    analisis_bivariat,
    analisis_multivariate_korelasi,
    customer_occupation,
    customer_occupation_transaction,
    agegroup_with_channel,
    persebaran_login_attempts,
)

import pandas as pd
from matplotlib.figure import Figure


# --- Dummy dataset untuk keperluan test ---
def sample_df():
    data = {
        "CustomerAge": [21, 35, 50, 42, 28],
        "CustomerOccupation": ["Student", "Engineer", "Doctor", "Retired", "Doctor"],
        "AccountBalance": [1000, 5000, 12000, 7000, 15000],
        "Channel": ["Online", "ATM", "Branch", "Online", "ATM"],
        "TransactionAmount": [50, 300, 2000, 500, 1500],
        "TransactionDuration": [40, 55, 20, 100, 35],
        "RecencyDays": [3, 1, 20, 5, 0],
        "LoginAttempts": [1, 6, 2, 8, 4],
        "TransactionID": ["TX01", "TX02", "TX03", "TX04", "TX05"],
        "TransactionType": ["Credit", "Debit", "Credit", "Credit", "Debit"],
        "AgeGroup": ["Gen Z", "Millenial", "Gen X", "Gen X", "Gen Z"],
    }
    return pd.DataFrame(data)


# --- Helper untuk semua test ---
def assert_valid_figure(fig):
    assert isinstance(fig, Figure)
    assert len(fig.axes) > 0


# -------------------------- TEST CASES ---------------------------

def test_analisis_univariat():
    df = sample_df()
    fig = analisis_univariat(df)
    assert_valid_figure(fig)


def test_analisis_bivariat():
    df = sample_df()
    fig = analisis_bivariat(df)
    assert_valid_figure(fig)


def test_analisis_multivariate_korelasi():
    df = sample_df()
    fig = analisis_multivariate_korelasi(df)
    assert_valid_figure(fig)


def test_customer_occupation():
    df = sample_df()
    fig = customer_occupation(df)
    assert_valid_figure(fig)


def test_customer_occupation_transaction():
    df = sample_df()
    fig = customer_occupation_transaction(df)
    assert_valid_figure(fig)


def test_agegroup_with_channel():
    df = sample_df()
    fig = agegroup_with_channel(df)
    assert_valid_figure(fig)


def test_persebaran_login_attempts():
    df = sample_df()
    fig = persebaran_login_attempts(df)
    assert_valid_figure(fig)