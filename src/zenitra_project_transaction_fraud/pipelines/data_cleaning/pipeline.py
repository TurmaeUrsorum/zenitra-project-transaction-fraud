"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import clean_data


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=clean_data,
                inputs="raw_data",
                outputs="data_cleaned",
                name="clean_data_node",
            )
        ]
    )
