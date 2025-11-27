"""
This is a boilerplate pipeline 'data_cleaning'
generated using Kedro 1.0.0
"""

from kedro.pipeline import Node, Pipeline, node  # noqa
from .nodes import (
    clean_data,
    date_formated,
    age_formated,
    balance_formated,
    account_id_handled,
    channel_occupation_handled,
    teknis_fromated,
    duration_login_handled,
    string_consistent,
    dated_formated_handled,
    dated_drop,
)


def create_pipeline(**kwargs) -> Pipeline:
    return Pipeline(
        [
            node(
                func=clean_data,
                inputs=["data_raw", "params:clean_data"],
                outputs="cleaned_data",
                name="clean_data_node",
            ),
            node(
                func=date_formated,
                inputs=["cleaned_data", "params:date_formated"],
                outputs="date_formated",
                name="date_formated_node",
            ),
            node(
                func=age_formated,
                inputs="date_formated",
                outputs="age_formated",
                name="age_formated_node",
            ),
            node(
                func=balance_formated,
                inputs="age_formated",
                outputs="balance_formated",
                name="balance_formated_node",
            ),
            node(
                func=account_id_handled,
                inputs="balance_formated",
                outputs="account_id_handled",
                name="account_id_handled_node",
            ),
            node(
                func=channel_occupation_handled,
                inputs="account_id_handled",
                outputs="channel_occupation_handled",
                name="channel_occupation_handled_node",
            ),
            node(
                func=teknis_fromated,
                inputs="channel_occupation_handled",
                outputs="teknis_fromated",
                name="teknis_fromated_node",
            ),
            node(
                func=duration_login_handled,
                inputs="teknis_fromated",
                outputs="duration_login_handled",
                name="duration_login_handled_node",
            ),
            node(
                func=string_consistent,
                inputs="duration_login_handled",
                outputs="string_consistent",
                name="string_consistent_node",
            ),
            node(
                func=dated_formated_handled,
                inputs="string_consistent",
                outputs="dated_formated_handled",
                name="dated_formated_handled_node",
            ),
            node(
                func=dated_drop,
                inputs="dated_formated_handled",
                outputs="data_cleaned",
                name="dated_drop_node",
            ),
        ]
    )
