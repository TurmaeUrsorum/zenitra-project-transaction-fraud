"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 1.0.0
"""

import pandas as pd
import typing as tp
import logging

log = logging.getLogger(__name__)


def clean_data(df: pd.DataFrame, params: tp.Dict) -> pd.DataFrame:
    df = df.copy()

    df_main_features = df.dropna(subset=params["subset"])

    df_main_features = df_main_features.drop_duplicates(
        subset=params["subset"]
    )

    return df_main_features


def date_formated(df: pd.DataFrame, params: tp.Dict) -> pd.DataFrame:
    df = df.copy()
    df["TransactionDate"] = pd.to_datetime(
        df["TransactionDate"], errors=params["errors"]
    )
    df["PreviousTransactionDate"] = pd.to_datetime(
        df["PreviousTransactionDate"], errors=params["errors"]
    )
    df["TransactionHour"] = df["TransactionDate"].dt.hour #type: ignore

    return df


def age_formated(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    median_age = df["CustomerAge"].median()
    df["CustomerAge"] = df["CustomerAge"].fillna(median_age)

    anomalous_age = df[(df["CustomerAge"] < 0) | (df["CustomerAge"] > 100)].shape[0]
    if anomalous_age > 0:
        log.info(
            f"-> Mengoreksi {anomalous_age} data umur tidak wajar (negatif/>100) menjadi median."
        )
        df.loc[(df["CustomerAge"] < 0) | (df["CustomerAge"] > 100), "CustomerAge"] = (
            median_age
        )

    return df


def balance_formated(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    critical_cols = ["AccountBalance", "TransactionAmount", "TransactionType"]
    df = df.dropna(subset=critical_cols)
    return df


def account_id_handled(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    missing_acc = df["AccountID"].isnull().sum()
    if missing_acc > 0:
        print(
            f"-> Menghapus {missing_acc} baris dengan AccountID kosong (Data Orphan)."
        )
        df = df.dropna(subset=["AccountID"])

    return df


def channel_occupation_handled(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    for col in ["Channel", "CustomerOccupation"]:
        if df[col].isnull().sum() > 0:
            mode_val = df[col].mode()[0]
            df[col] = df[col].fillna(mode_val)
            print(f"-> Mengisi '{col}' kosong dengan Modus: {mode_val}")

    return df


def teknis_fromated(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    tech_cols = ["DeviceID", "IP Address", "MerchantID", "Location"]
    df[tech_cols] = df[tech_cols].fillna("Unknown")
    print(f"-> Mengisi data kosong pada {tech_cols} dengan 'Unknown'.")

    return df


def duration_login_handled(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    num_cols = ["TransactionDuration", "LoginAttempts"]
    for col in num_cols:
        if df[col].isnull().sum() > 0:
            median_val = df[col].median()
            df[col] = df[col].fillna(median_val)
            print(f"-> Mengisi '{col}' kosong dengan Median: {median_val}")

    return df


def string_consistent(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    str_cols = ["Location", "Channel", "CustomerOccupation"]
    for col in str_cols:

        df[col] = df[col].astype(str).str.strip().str.title()
    print("-> Melakukan standardisasi format teks (Title Case) pada kolom kategori.")

    return df


def dated_formated_handled(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    anomalies = df[df["TransactionDate"] < df["PreviousTransactionDate"]].shape[0]

    if anomalies > (0.5 * df.shape[0]):
        print(f"   [DETECTION] Ditemukan {anomalies} baris dengan tanggal terbalik.")
        print(
            "   [ACTION] Melakukan penukaran (Swap) nilai antara TransactionDate dan PreviousTransactionDate."
        )

        temp_date = df["TransactionDate"].copy()
        df["TransactionDate"] = df["PreviousTransactionDate"]
        df["PreviousTransactionDate"] = temp_date

        print(
            "   [SUCCESS] Kolom tanggal telah diperbaiki. Sekarang Logis (Current > Previous)."
        )

        return df
    else:
        print("   [INFO] Logika tanggal sudah benar.")

        return df


def dated_drop(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.dropna(subset=["TransactionDate", "PreviousTransactionDate"])

    return df
