"""
This is a boilerplate pipeline 'data_modeling'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import (
    feature_transform,
    model_IF,
    model_KM,
    generate_reason,
    anomalies_detect,
    anomali_plot,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=feature_transform,
                inputs="feature_engineered",
                outputs="feature_transformed",
                name="feature_transform_node",
            ),
            node(
                func=model_IF,
                inputs="feature_transformed",
                outputs=["anomalies_df", "model_IF"],
                name="model_IF_node",
            ),
            node(
                func=model_KM,
                inputs="anomalies_df",
                outputs=["clusters_df", "model_KM"],
                name="model_KM_node",
            ),
            node(
                func=anomalies_detect,
                inputs="clusters_df",
                outputs="anomalies_detect_df",
                name="anomalies_detect_node",
            ),
            node(
                func=anomali_plot,
                inputs="anomalies_detect_df",
                outputs="anomalies_plot_fig",
                name="anomalies_plot_node",
            ),
        ]
    )
