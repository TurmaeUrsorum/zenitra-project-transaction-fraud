"""
This is a boilerplate pipeline 'data_preproses'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import (
    feature_engineering,
    skew_fix,
    handle_outliers,
    robust_scaler,
    final_dataset,
    feature_engineering_fraud,
    scaling_numerik_fraud,
    location_top_N,
    one_hot_encoder_fraud,
    final_dataset_fraud,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            # node untuk case segmentation
            node(
                func=feature_engineering,
                inputs=["data_cleaned", "params:feature_engineering"],
                outputs="feature_engineering",
                name="feature_engineering",
            ),
            node(
                func=skew_fix,
                inputs=["feature_engineering", "params:skew_fix"],
                outputs="skew_fix",
                name="skew_fix",
            ),
            node(
                func=handle_outliers,
                inputs=["skew_fix", "params:handle_outliers"],
                outputs="handle_outliers",
                name="handle_outliers",
            ),
            node(
                func=robust_scaler,
                inputs="handle_outliers",
                outputs="robust_scaler_df",
                name="robust_scaler_df",
            ),
            node(
                func=final_dataset,
                inputs="robust_scaler_df",
                outputs="final_preprocessed_df",
                name="final_preprocessed_df",
            ),
            # node untuk case fraud detection
            node(
                func=feature_engineering_fraud,
                inputs="data_cleaned_fraud",
                outputs="feature_engineering_fraud",
                name="feature_engineering_fraud",
            ),
            node(
                func=scaling_numerik_fraud,
                inputs="feature_engineering_fraud",
                outputs="scaling_numerik_fraud",
                name="scaling_numerik_fraud",
            ),
            node(
                func=location_top_N,
                inputs="feature_engineering_fraud",
                outputs="location_top_N",
                name="location_top_N",
            ),
            node(
                func=one_hot_encoder_fraud,
                inputs="location_top_N",
                outputs="one_hot_encoder_fraud",
                name="one_hot_encoder_fraud",
            ),
            node(
                func=final_dataset_fraud,
                inputs=["one_hot_encoder_fraud", "scaling_numerik_fraud"],
                outputs="final_preprocessed_df_fraud",
                name="final_preprocessed_df_fraud",
            ),
        ]
    )
