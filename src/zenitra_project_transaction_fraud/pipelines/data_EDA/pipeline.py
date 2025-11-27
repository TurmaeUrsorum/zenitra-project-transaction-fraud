"""
This is a boilerplate pipeline 'data_EDA'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import (
    analisis_univariat,
    analisis_bivariat,
    analisis_multivariate_korelasi,
    customer_occupation,
    customer_occupation_transaction,
    agegroup_with_channel,
    persebaran_login_attempts,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            # node untuk case segmentation
            node(
                func=analisis_univariat,
                inputs="feature_engineered",
                outputs="analisis_univariat_fig",
                name="analisis_univariat_node",
            ),
            node(
                func=analisis_bivariat,
                inputs="feature_engineered",
                outputs="analisis_bivariat_fig",
                name="analisis_bivariat_node",
            ),
            node(
                func=analisis_multivariate_korelasi,
                inputs="feature_engineered",
                outputs="analisis_multivariate_korelasi_fig",
                name="analisis_multivariate_korelasi_node",
            ),
            node(
                func=customer_occupation,
                inputs="feature_engineered",
                outputs="customer_occupation_fig",
                name="customer_occupation_node",
            ),
            node(
                func=customer_occupation_transaction,
                inputs="feature_engineered",
                outputs="customer_occupation_transaction_fig",
                name="customer_occupation_transaction_node",
            ),
            node(
                func=agegroup_with_channel,
                inputs="feature_engineered",
                outputs="agegroup_with_channel_fig",
                name="agegroup_with_channel_node",
            ),
            node(
                func=persebaran_login_attempts,
                inputs="feature_engineered",
                outputs="persebaran_login_attempts_fig",
                name="persebaran_login_attempts_node",
            ),
        ]
    )
