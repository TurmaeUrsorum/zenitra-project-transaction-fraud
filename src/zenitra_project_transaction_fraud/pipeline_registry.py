"""Project pipelines."""

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline
from .pipelines.data_cleaning import pipeline as dc
from .pipelines.data_EDA import pipeline as de
from .pipelines.data_preproses import pipeline as dp
from .pipelines.data_modeling import pipeline as dm
from .pipelines.data_evaluasi import pipeline as deval


def register_pipelines() -> dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    data_cleaning_pipeline = dc.create_pipeline()
    data_EDA_pipeline = de.create_pipeline()
    data_preproses_pipeline = dp.create_pipeline()
    data_modeling_pipeline = dm.create_pipeline()
    data_evaluasi_pipeline = deval.create_pipeline()

    return {
        "__default__": data_cleaning_pipeline
        + data_EDA_pipeline
        + data_preproses_pipeline
        + data_modeling_pipeline
        + data_evaluasi_pipeline,
        "deval": data_evaluasi_pipeline,
        "dc": data_cleaning_pipeline,
        "de": data_EDA_pipeline,
        "dp": data_preproses_pipeline,
        "dm": data_modeling_pipeline,
    }
