"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 1.0.0
"""

import pandas as pd
import typing as tp


def clean_data(df: pd.DataFrame, params: tp.Dict) -> pd.DataFrame:
    df_main_features = df[params["columns"]]

    df_main_features = df_main_features.dropna()

    df_main_features = df_main_features.drop_duplicates()

    return df_main_features
