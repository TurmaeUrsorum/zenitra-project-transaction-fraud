"""
This is a boilerplate pipeline 'data_EDA'
generated using Kedro 1.0.0
"""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
import pandas as pd
import seaborn as sns
import numpy as np


def analisis_univariat(df: pd.DataFrame) -> Figure:
    fig, axes = plt.subplots(2, 2, figsize=(16, 10))
    fig.suptitle("Analisis Univariat: Distribusi Data", fontsize=16)

    sns.histplot(df["CustomerAge"], bins=20, kde=True, color="skyblue", ax=axes[0, 0]) #type: ignore
    axes[0, 0].set_title("Distribusi Umur Nasabah")

    sns.countplot(
        y="CustomerOccupation",
        data=df,
        order=df["CustomerOccupation"].value_counts().index,
        palette="viridis",
        ax=axes[0, 1],
    )
    axes[0, 1].set_title("Jumlah Nasabah per Pekerjaan")

    sns.boxplot(x="AccountBalance", data=df, color="lightgreen", ax=axes[1, 0])
    axes[1, 0].set_title("Sebaran Saldo Rekening (Cek Outlier)")

    channel_counts = df["Channel"].value_counts()
    axes[1, 1].pie(
        channel_counts,
        labels=channel_counts.index,
        autopct="%1.1f%%",
        colors=sns.color_palette("pastel"),
        startangle=90,
    )
    axes[1, 1].set_title("Persentase Penggunaan Kanal")

    plt.tight_layout()
    # plt.close(fig)

    return fig


def analisis_bivariat(df: pd.DataFrame) -> Figure:
    fig, axes = plt.subplots(2, 2, figsize=(16, 12))
    fig.suptitle("Analisis Bivariat", fontsize=16)

    avg_balance = (
        df.groupby("CustomerOccupation")["AccountBalance"]
        .mean()
        .sort_values(ascending=False)
        .index
    )
    sns.barplot(
        x="CustomerOccupation",
        y="AccountBalance",
        data=df,
        order=avg_balance,
        palette="Blues_d",
        ax=axes[0, 0],
    )
    axes[0, 0].set_title("Rata-rata Saldo per Pekerjaan")
    axes[0, 0].set_ylabel("Saldo Rata-rata ($)")

    sns.histplot(
        df["TransactionAmount"], #type: ignore
        bins=30,
        kde=True,
        color="purple",
        log_scale=True,
        ax=axes[0, 1],
    )

    axes[0, 1].set_title(
        "Sebaran Nominal Transaksi (Log Scale)", fontsize=12, fontweight="bold"
    )
    axes[0, 1].set_xlabel("Nominal ($) - Skala Logaritma")
    axes[0, 1].set_ylabel("Frekuensi")

    mean_val = df["TransactionAmount"].mean()
    axes[0, 1].axvline(
        mean_val, color="red", linestyle="--", label=f"Rata-rata: ${mean_val:.0f}"
    )
    axes[0, 1].legend()

    sns.countplot(x="AgeGroup", hue="Channel", data=df, palette="Set2", ax=axes[1, 0])
    axes[1, 0].set_title("Preferensi Kanal Transaksi per Generasi")
    axes[1, 0].legend(title="Channel", loc="upper right")

    sns.scatterplot(
        x="AccountBalance",
        y="TransactionAmount",
        hue="CustomerOccupation",
        alpha=0.6,
        data=df,
        ax=axes[1, 1],
    )
    axes[1, 1].set_title("Korelasi Saldo vs Nilai Transaksi")

    plt.tight_layout()
    # plt.close(fig)

    return fig


def analisis_multivariate_korelasi(df: pd.DataFrame) -> Figure:
    fig = plt.figure(figsize=(10, 6))

    corr_matrix = df[
        [
            "TransactionAmount",
            "AccountBalance",
            "CustomerAge",
            "TransactionDuration",
            "RecencyDays",
            "LoginAttempts",
        ]
    ].corr()

    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", fmt=".2f", linewidths=0.5)
    plt.title("Matriks Korelasi Antar Variabel Numerik")
    # plt.close(fig)

    return fig


def customer_occupation(df: pd.DataFrame) -> Figure:
    fig = plt.figure(figsize=(12, 6))

    data_q1 = (
        df.groupby("CustomerOccupation")["AccountBalance"]
        .mean()
        .sort_values(ascending=False)
        .reset_index()
    )

    colors_q1 = [
        "#005b96" if x == data_q1["AccountBalance"].max() else "#d3d3d3"
        for x in data_q1["AccountBalance"]
    ]

    ax1 = sns.barplot(
        x="AccountBalance", y="CustomerOccupation", data=data_q1, palette=colors_q1
    )

    plt.title(
        "Dokter adalah Nasabah Paling Bernilai dengan Rata-rata Saldo Tertinggi",
        fontsize=16,
        fontweight="bold",
        loc="left",
        pad=20,
    )
    plt.xlabel("Rata-rata Saldo ($)", fontsize=12)
    plt.ylabel("")

    for i, v in enumerate(data_q1["AccountBalance"]):
        ax1.text(
            v + 100,
            i,
            f"${v:,.0f}",
            va="center",
            fontweight="bold",
            color="#333333",
            fontsize=11,
        )

    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    # plt.close(fig)

    return fig


def customer_occupation_transaction(df: pd.DataFrame) -> Figure:
    fig, ax = plt.subplots(figsize=(12, 6))

    ct_product = (
        pd.crosstab(df["CustomerOccupation"], df["TransactionType"], normalize="index")
        * 100
    )
    ct_product = ct_product.sort_values(by="Credit", ascending=False)

    ax = ct_product.plot(
        kind="barh",
        stacked=True,
        color=["#d62728", "#2ca02c"],
        figsize=(12, 6),
        width=0.7,
        ax=ax,
    )

    plt.title(
        "Pensiunan (Retired) Paling Sering Menggunakan Kartu Kredit (30%)",
        fontsize=18,
        fontweight="bold",
        loc="left",
    )
    plt.xlabel("Persentase Transaksi (%)", fontsize=12)
    plt.ylabel("")
    plt.legend(title="Tipe Transaksi", bbox_to_anchor=(1, 1))

    for c in ax.containers:
        labels = [f"{w:.0f}%" if w > 5 else "" for w in c.datavalues] #type: ignore
        ax.bar_label(
            c, #type: ignore
            labels=labels,
            label_type="center",
            color="white",
            fontweight="bold",
            fontsize=11,
        )

    sns.despine(left=True, bottom=True)
    plt.tight_layout()
    # plt.close(fig)

    return fig


def agegroup_with_channel(df: pd.DataFrame) -> Figure:
    fig, ax = plt.subplots(figsize=(12, 6))

    data_q2 = pd.crosstab(df["AgeGroup"], df["Channel"], normalize="index") * 100

    ax2 = data_q2.plot(
        kind="bar",
        stacked=True,
        color=["#ff9999", "#66b3ff", "#99ff99"],
        figsize=(12, 6),
        width=0.8,
        edgecolor="white",
        ax=ax,
    )

    plt.title(
        "Preferensi Kanal Merata: Gen Z Masih Menggunakan Cabang & ATM",
        fontsize=16,
        fontweight="bold",
        loc="left",
        pad=20,
    )
    plt.xlabel("Kelompok Usia", fontsize=12)
    plt.ylabel("Persentase Penggunaan (%)", fontsize=12)
    plt.xticks(rotation=0)
    plt.legend(title="Media Transaksi", bbox_to_anchor=(1.02, 1), loc="upper left")

    for c in ax2.containers: 
        labels = [f"{v:.0f}%" for v in c.datavalues] #type: ignore
        ax2.bar_label(
            c, #type: ignore
            labels=labels,
            label_type="center",
            color="black",
            fontweight="bold",
            fontsize=10,
        )

    sns.despine(top=True, right=True)
    plt.tight_layout()
    # plt.close(fig)

    return fig


def persebaran_login_attempts(df: pd.DataFrame) -> Figure:
    fig = plt.figure(figsize=(12, 6))

    suspicious_login = df[df["LoginAttempts"] > 3]
    normal_login = df[df["LoginAttempts"] <= 3]

    plt.scatter(
        normal_login["TransactionDuration"],
        normal_login["TransactionAmount"],
        c="lightgrey",
        alpha=0.5,
        label="Normal Login",
        s=30,
    )

    plt.scatter(
        suspicious_login["TransactionDuration"],
        suspicious_login["TransactionAmount"],
        c="red",
        label="Suspicious (>3 Logins)",
        s=100,
        edgecolors="black",
    )

    plt.title(
        "RED FLAG: 58 Transaksi Terjadi Setelah Gagal Login >3 Kali",
        fontsize=16,
        fontweight="bold",
        loc="left",
    )
    plt.xlabel("Durasi Transaksi (detik)")
    plt.ylabel("Nilai Transaksi ($)")
    plt.legend(loc="upper right")

    for i, row in suspicious_login.iterrows():
        if row["TransactionAmount"] > 1000:
            plt.text(
                row["TransactionDuration"] + 5,
                row["TransactionAmount"],
                row["TransactionID"],
                fontsize=9,
                fontweight="bold",
                color="darkred",
            )

    sns.despine()
    plt.tight_layout()
    # plt.close(fig)

    return fig
