"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines.data_cleaning import pipeline as dc
from .pipelines.data_EDA import pipeline as de


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_cleaning_pipeline = dc.create_pipeline()
    data_EDA_pipeline = de.create_pipeline()

    return {
        "__default__": data_cleaning_pipeline + data_EDA_pipeline,
        "dc": data_cleaning_pipeline,
        "de": data_EDA_pipeline,
    }

    return
