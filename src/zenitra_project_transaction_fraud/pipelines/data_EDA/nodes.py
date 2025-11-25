"""
This is a boilerplate pipeline 'data_EDA'
generated using Kedro 1.0.0
"""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import seaborn as sns


def numeric_feature(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include=["int64", "float64"])


def categorical_feature(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include=["object"])


def skewness_check_fig(df: pd.DataFrame) -> Figure:
    df_numeric = numeric_feature(df)
    fig = plt.figure(figsize=(20, 10))
    for i, col in enumerate(df_numeric.columns):
        ax = fig.add_subplot(2, 5, i + 1)
        sns.histplot(x=df_numeric[col], ax=ax)
        ax.set_title(col)
    plt.tight_layout()
    plt.close(fig)
    return fig


def outlires_check_fig(df: pd.DataFrame) -> Figure:
    df_numeric = numeric_feature(df)
    fig = plt.figure(figsize=(20, 10))
    for i, col in enumerate(df_numeric.columns):
        ax = fig.add_subplot(2, 5, i + 1)
        sns.boxplot(x=df_numeric[col], ax=ax)
        ax.set_title(col)
    plt.tight_layout()
    plt.close(fig)
    return fig


def transaction_type_bar_fig(df: pd.DataFrame) -> Figure:
    df_cat = categorical_feature(df)
    fig = plt.figure(figsize=(20, 10))
    sns.barplot(
        x=df_cat["TransactionType"].value_counts().index,
        y=df_cat["TransactionType"].value_counts().values,
    )
    plt.tight_layout()
    plt.close(fig)
    return fig


def channel_bar_fig(df: pd.DataFrame) -> Figure:
    df_cat = categorical_feature(df)
    fig = plt.figure(figsize=(20, 10))
    sns.barplot(
        x=df_cat["Channel"].value_counts().index,
        y=df_cat["Channel"].value_counts().values,
    )
    plt.tight_layout()
    plt.close(fig)
    return fig


def location_bar_fig(df: pd.DataFrame) -> Figure:
    df_cat = categorical_feature(df)
    top5 = df_cat["Location"].value_counts().head(5)
    fig = plt.figure(figsize=(20, 10))
    plt.barh(top5.index[::-1], top5.values[::-1])  # type: ignore
    plt.xlabel("Count")
    plt.ylabel("Location")
    plt.title("Top 5 Location")
    plt.tight_layout()
    plt.close(fig)
    return fig


def customer_occupation_bar_fig(df: pd.DataFrame) -> Figure:
    df_cat = categorical_feature(df)
    fig = plt.figure(figsize=(20, 10))
    sns.barplot(
        x=df_cat["CustomerOccupation"].value_counts().index,
        y=df_cat["CustomerOccupation"].value_counts().values,
    )
    plt.tight_layout()
    plt.close(fig)
    return fig

def korelasi_heatmap_fig(df: pd.DataFrame) -> Figure:
    df_numeric = numeric_feature(df)
    fig = plt.figure(figsize=(20, 10))
    sns.heatmap(df_numeric.corr(), annot=True)
    plt.tight_layout()
    plt.close(fig)
    return fig
