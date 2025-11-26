"""
This is a boilerplate pipeline 'data_EDA'
generated using Kedro 1.0.0
"""

from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import seaborn as sns
import numpy as np
import scipy.stats as ss


def numeric_feature(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include=["int64", "float64"])


def categorical_feature(df: pd.DataFrame) -> pd.DataFrame:
    return df.select_dtypes(include=["object"])


# case untuk user segmentation


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


# case untuk fraud detection


def skewnes_check_fig_fraud(df: pd.DataFrame) -> Figure:
    df_numeric = numeric_feature(df)
    fig = plt.figure(figsize=(20, 10))
    for i, col in enumerate(df_numeric.columns):
        ax = fig.add_subplot(2, 3, i + 1)
        sns.histplot(x=np.log1p(df_numeric[col]), ax=ax)
        ax.set_title(col)
    plt.title("Distribution of Numeric Features")
    plt.tight_layout()
    plt.close(fig)
    return fig


def check_outliers_fig_fraud(df: pd.DataFrame) -> Figure:
    df_numeric = numeric_feature(df)
    fig = plt.figure(figsize=(20, 10))
    for i, col in enumerate(df_numeric.columns):
        ax = fig.add_subplot(2, 3, i + 1)
        sns.boxplot(x=df_numeric[col], ax=ax)
        ax.set_title(col)
    plt.tight_layout()
    plt.title("Boxplot of Numeric Features")
    plt.close(fig)
    return fig


def modality_check_fig_fraud(df: pd.DataFrame) -> Figure:
    df_numeric = numeric_feature(df)
    fig = plt.figure(figsize=(20, 10))
    for i, col in enumerate(df_numeric.columns):
        ax = fig.add_subplot(2, 3, i + 1)
        sns.kdeplot(df_numeric[col], ax=ax)  # type: ignore
        ax.set_title(col)
    plt.tight_layout()
    plt.title("Modality of Numeric Features")
    plt.close(fig)
    return fig


def distribusi_kategori_fig_fraud(df: pd.DataFrame) -> Figure:
    df_categorical2 = categorical_feature(df)
    df_categorical2 = df_categorical2.drop(
        [
            "Location",
            "AccountID",
            "DeviceID",
            "IP Address",
            "MerchantID",
            "TransactionID",
        ],
        axis=1,
    )
    fig = plt.figure(figsize=(20, 10))
    for i, col in enumerate(df_categorical2.columns):
        ax = fig.add_subplot(2, 3, i + 1)
        sns.barplot(
            x=df_categorical2[col].value_counts().index[:10],
            y=df_categorical2[col].value_counts().values[:10],
        )
        ax.set_title(col)
    plt.tight_layout()
    plt.title("Distribution of Categorical Features")
    plt.close(fig)
    return fig


def distribusi_kategori_loc_fig_fraud(df: pd.DataFrame) -> Figure:
    df_categorical_location = categorical_feature(df)
    df_categorical_location = df_categorical_location.drop(
        ["TransactionID", "AccountID", "DeviceID", "IP Address", "MerchantID"], axis=1
    )
    df_categorical = categorical_feature(df)
    df_categorical = df_categorical.drop(
        ["TransactionID", "AccountID", "DeviceID", "IP Address", "MerchantID"], axis=1
    )
    df_categorical_location = (
        df_categorical_location["Location"].value_counts().head(5).index
    )
    fig = plt.figure(figsize=(20, 10))
    sns.barplot(
        x=df_categorical_location,
        y=df_categorical["Location"].value_counts().head(5).values,
    )
    plt.title("Distribution of Location")
    plt.close(fig)
    return fig


def korelasi_heatmap_fig_fraud(df: pd.DataFrame) -> Figure:
    df_numeric = numeric_feature(df)
    corr = df_numeric.corr() * 100  # ubah ke persen

    fig = plt.figure(figsize=(10, 6))
    sns.heatmap(
        corr,
        annot=True,  # tampilkan angkanya
        fmt=".1f",  # 1 angka desimal
        cmap="coolwarm",
    )
    plt.title("Correlation Heatmap (in %)")
    plt.close(fig)
    return fig


def pca_fig_fraud(df: pd.DataFrame) -> Figure:
    df_numeric = numeric_feature(df)
    scaled = StandardScaler().fit_transform(df_numeric)
    pca = PCA(n_components=2)
    pca_data = pca.fit_transform(scaled)

    df["PC1"], df["PC2"] = pca_data[:, 0], pca_data[:, 1]

    fig = plt.figure(figsize=(20, 10))
    sns.scatterplot(data=df, x="PC1", y="PC2")
    plt.title("PCA 2D — Potential Patterns / Outliers")
    plt.close(fig)
    return fig


def cramers_v(x, y):
    confusion = pd.crosstab(x, y)
    chi2 = ss.chi2_contingency(confusion)[0]
    n = confusion.sum().sum()
    phi2 = chi2 / n
    r, k = confusion.shape
    phi2_corr = max(0, phi2 - ((k - 1) * (r - 1)) / (n - 1))
    r_corr = r - ((r - 1) ** 2) / (n - 1)
    k_corr = k - ((k - 1) ** 2) / (n - 1)
    return np.sqrt(phi2_corr / min((k_corr - 1), (r_corr - 1)))


def cramer_v_fig_fraud(df: pd.DataFrame) -> Figure:
    df_categorical = categorical_feature(df)
    df_categorical = df_categorical.drop(
        ["TransactionID", "AccountID", "DeviceID", "IP Address", "MerchantID"], axis=1
    )

    corr_matrix = pd.DataFrame(
        [
            [
                cramers_v(df_categorical[col_i], df_categorical[col_j])
                for col_j in df_categorical.columns
            ]
            for col_i in df_categorical.columns
        ],
        columns=df_categorical.columns,
        index=df_categorical.columns,
    )

    fig = plt.figure(figsize=(8, 6))
    sns.heatmap(
        corr_matrix * 100, annot=True, fmt=".2f", cmap="coolwarm", vmin=0, vmax=1
    )
    plt.title("Cramér's V Heatmap")
    plt.close(fig)
    return fig
