"""
This is a boilerplate test file for pipeline 'data_modeling'
generated using Kedro 1.0.0.
Please add your pipeline tests here.

Kedro recommends using `pytest` framework, more info about it can be found
in the official documentation:
https://docs.pytest.org/en/latest/getting-started.html
"""
from zenitra_project_transaction_fraud.pipelines.data_modeling.nodes import (
    feature_transform,
    model_IF,
    model_KM,
    generate_reason,
    anomalies_detect,
    anomali_plot,
)
from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use("Agg")  # agar test plot tidak membuka GUI
from matplotlib.figure import Figure

def sample_df():
    return pd.DataFrame({
        "TransactionAmount": [50, 5000, 600, 2000, 100],
        "AccountBalance": [200, 8000, 400, 500, 10000],
        "CustomerAge": [22, 45, 34, 60, 19],
        "TransactionDuration": [10, 90, 15, 200, 7],
        "RecencyDays": [1, 10, 0, 20, 2],
        "LoginAttempts": [1, 6, 2, 10, 4],
        "Channel": ["Online", "ATM", "Branch", "ATM", "Online"],
        "CustomerOccupation": ["Student", "Engineer", "Doctor", "Retired", "Doctor"],
        "TransactionType": ["Credit", "Debit", "Credit", "Credit", "Debit"],
    })

def assert_valid_figure(fig):
    assert isinstance(fig, Figure)
    assert len(fig.axes) > 0

def test_feature_transform():
    df = sample_df()
    X = feature_transform(df)

    assert isinstance(X, pd.DataFrame)
    assert X.shape[0] == df.shape[0]
    # hasil transform harus lebih banyak kolom setelah OHE
    assert X.shape[1] > df.select_dtypes(include="number").shape[1]

def test_model_IF():
    df = sample_df()
    df_out, model = model_IF(df)

    assert isinstance(df_out, pd.DataFrame)
    assert isinstance(model, IsolationForest)
    assert "Anomaly_Flag" in df_out.columns
    assert "Anomaly_Score" in df_out.columns

def test_model_KM():
    df = feature_transform(sample_df())
    df_out, model = model_KM(df)

    assert isinstance(df_out, pd.DataFrame)
    assert isinstance(model, KMeans)
    assert "Cluster_ID" in df_out.columns

def test_generate_reason():
    df = feature_transform(sample_df())
    df["Anomaly_Flag"] = [-1, 1, -1, 1, -1]  # mock anomaly
    global_means = df.mean()

    row = df.iloc[0]
    reason = generate_reason(row, global_means)

    assert isinstance(reason, str)
    assert len(reason) > 0

def test_anomalies_detect():
    df = feature_transform(sample_df())
    df["Anomaly_Flag"] = [-1, 1, -1, 1, -1]
    df["Anomaly_Score"] = np.random.randn(len(df))

    anomalies = anomalies_detect(df)

    assert isinstance(anomalies, pd.DataFrame)
    assert "Reason" in anomalies.columns
    assert all(anomalies["Anomaly_Flag"] == -1)

def test_anomali_plot():
    df = feature_transform(sample_df())
    df["Anomaly_Flag"] = [-1, 1, -1, 1, -1]
    df["Cluster_ID"] = [0, 1, 2, 1, 0]

    fig = anomali_plot(df)

    assert_valid_figure(fig)

