"""
This is a boilerplate pipeline 'data_preproses'
generated using Kedro 1.0.0
"""

import pandas as pd
import numpy as np


def age_bins_column(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    bins = [0, 25, 45, 60, 100]
    labels = ["Gen Z", "Millennial", "Gen X", "Boomer"]

    df["AgeGroup"] = pd.cut(df["CustomerAge"], bins=bins, labels=labels)
    print("-> Kolom 'AgeGroup' berhasil dibuat.")

    return df


def recovery_days_columns(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["RecencyDays"] = (df["TransactionDate"] - df["PreviousTransactionDate"]).dt.days  # type: ignore
    print("-> Kolom 'RecencyDays' berhasil dibuat.")

    return df
