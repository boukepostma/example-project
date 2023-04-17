"""Project pipelines."""
from platform import python_version

from typing import Dict

from kedro.framework.project import find_pipelines
from kedro.pipeline import Pipeline

from kedro_mlflow.pipeline import pipeline_ml_factory
from pip._internal.operations.freeze import freeze
# from new_quickstart_ml_project import __version__ as PROJECT_VERSION

def register_pipelines() -> Dict[str, Pipeline]:
    """Register the project's pipelines.

    Returns:
        A mapping from pipeline names to ``Pipeline`` objects.
    """
    pipelines = find_pipelines()
    
    default_pipeline = sum(pipelines.values())
    training_pipeline = default_pipeline.only_nodes_with_tags("training")
    inference_pipeline = default_pipeline.only_nodes_with_tags("inference")
    deploy_pipeline =  default_pipeline.only_nodes_with_tags("deployment")
    user_pipeline = default_pipeline.only_nodes_with_tags("user")

    training_pipeline_ml = pipeline_ml_factory(
        training=training_pipeline,
        inference=inference_pipeline,
        input_name="raw_inputs",
        log_model_kwargs=dict(
            registered_model_name="some_registered_model_name",
            artifact_path="new_quickstart_ml_project",
            conda_env={
                "name": "mlflow-env",
                "channels": ["conda-forge"],
                "dependencies": [
                    f"python={python_version()}",
                    *[pkg.replace("==", "=") for pkg in freeze() if 'pip' in pkg], 
                    {
                        "pip" : [pkg for pkg in freeze() if 'pip' not in pkg]
                    }
                ]
            },
            code_path=["pyproject.toml", "src/new_quickstart_ml_project"]
        ),
    )

    return {
        "__default__": default_pipeline,
        "training" : training_pipeline_ml,
        "inference": inference_pipeline,
        "deploy" : deploy_pipeline,
        "user": user_pipeline,
    }
