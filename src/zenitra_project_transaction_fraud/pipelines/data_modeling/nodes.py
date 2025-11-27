"""
This is a boilerplate pipeline 'data_modeling'
generated using Kedro 1.0.0
"""

from sklearn.ensemble import IsolationForest
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import typing as tp


def feature_transform(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    features_num = [
        "TransactionAmount",
        "AccountBalance",
        "CustomerAge",
        "TransactionDuration",
        "RecencyDays",
        "LoginAttempts",
    ]
    features_cat = ["Channel", "CustomerOccupation", "TransactionType"]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), features_num),
            ("cat", OneHotEncoder(handle_unknown="ignore"), features_cat),
        ]
    )

    X = df[features_num + features_cat]
    X_processed = preprocessor.fit_transform(X)
    X_processed = pd.DataFrame(
        X_processed, columns=preprocessor.get_feature_names_out() # type: ignore
    )

    return X_processed


def model_IF(df: pd.DataFrame) -> tp.Tuple[pd.DataFrame, IsolationForest]:
    df = df.copy()

    # hanya numerik
    df_num = df.select_dtypes(include="number")

    iso_model = IsolationForest(n_estimators=200, contamination=0.1, random_state=42)

    pred = iso_model.fit_predict(df_num)
    score = iso_model.decision_function(df_num)

    df["Anomaly_Flag"] = pred
    df["Anomaly_Score"] = score

    return df, iso_model


def model_KM(df: pd.DataFrame) -> tp.Tuple[pd.DataFrame, KMeans]:
    df = df.copy()

    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
    df["Cluster_ID"] = kmeans.fit_predict(df)

    return df, kmeans


def generate_reason(row, global_means):
    reasons = []
    if row["num__TransactionAmount"] > global_means["num__TransactionAmount"] * 3:
        reasons.append("Huge Amount")
    if row["num__LoginAttempts"] > 3:
        reasons.append("Brute Force (Login > 3)")
    if row["num__RecencyDays"] < 2:
        reasons.append("High Frequency (Rapid Tx)")
    if row["num__TransactionDuration"] < 20:
        reasons.append("Too Fast (Bot?)")
    if row["num__AccountBalance"] < 500 and row["num__TransactionAmount"] > 500:
        reasons.append("High Risk Spending")

    if not reasons and row["Anomaly_Flag"] == -1:
        return "Complex Pattern Anomaly"

    return ", ".join(reasons)


def anomalies_detect(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    features_num = [
        "num__TransactionAmount",
        "num__AccountBalance",
        "num__CustomerAge",
        "num__TransactionDuration",
        "num__RecencyDays",
        "num__LoginAttempts",
    ]

    global_means = df[features_num].mean()
    anomalies = df[df["Anomaly_Flag"] == -1].copy()
    anomalies["Reason"] = anomalies.apply(
        generate_reason, axis=1, global_means=global_means
    )

    anomalies = anomalies.sort_values(by="Anomaly_Score", ascending=True)

    return anomalies


def anomali_plot(df: pd.DataFrame) -> Figure:
    fig, ax = plt.subplots(1, 2, figsize=(16, 6))

    sns.scatterplot(
        data=df,
        x="num__TransactionDuration",
        y="num__TransactionAmount",
        hue="Anomaly_Flag",
        palette={1: "lightgrey", -1: "red"},
        style="Anomaly_Flag",
        markers={1: "o", -1: "X"},
        alpha=0.7,
        ax=ax[0],
    )
    ax[0].set_title(
        "Hasil Isolation Forest: Titik Merah adalah Anomali",
        fontsize=14,
        fontweight="bold",
    )
    ax[0].legend(title="Status (1=Normal, -1=Anomali)")

    sns.scatterplot(
        data=df,
        x="num__AccountBalance",
        y="num__TransactionDuration",
        hue="Cluster_ID",
        palette="viridis",
        s=60,
        alpha=0.8,
        ax=ax[1],
    )
    ax[1].set_title(
        "Hasil Clustering: Segmentasi Nasabah", fontsize=14, fontweight="bold"
    )
    ax[1].legend(title="Cluster Group")

    plt.tight_layout()

    return fig
