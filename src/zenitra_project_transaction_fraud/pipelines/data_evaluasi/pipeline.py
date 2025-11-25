"""
This is a boilerplate pipeline 'data_evaluasi'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import evaluasi_model


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=evaluasi_model,
                inputs=["final_preprocessed_df", "kmedoids_model"],
                outputs=None,
                name="evaluasi_model",
            )
        ]
    )
