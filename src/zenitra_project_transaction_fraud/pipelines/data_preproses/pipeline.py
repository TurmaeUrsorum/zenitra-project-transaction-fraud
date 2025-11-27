"""
This is a boilerplate pipeline 'data_preproses'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import (
    age_bins_column,
    recovery_days_columns,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            # node untuk case segmentation
            node(
                func=age_bins_column,
                inputs="data_cleaned",
                outputs="age_bins",
                name="age_bins_node",
            ),
            node(
                func=recovery_days_columns,
                inputs="age_bins",
                outputs="feature_engineered",
                name="recovery_days_node",
            ),
        ]
    )
