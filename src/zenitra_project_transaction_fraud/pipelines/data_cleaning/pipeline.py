"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import clean_data, clean_data_fraud


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            # node untuk case segmentation
            node(
                func=clean_data,
                inputs=["data_raw", "params:data_cleaning_segmentation"],
                outputs="data_cleaned",
                name="clean_data_node",
            ),
            # node untuk case fraud detection
            node(
                func=clean_data_fraud,
                inputs="data_raw",
                outputs="data_cleaned_fraud",
                name="clean_data_node_fraud",
            ),
        ]
    )
