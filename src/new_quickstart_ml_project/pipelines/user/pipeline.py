"""
This is a boilerplate pipeline 'user'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node

from .nodes import predict_with_mlflow


def create_pipeline(**kwargs):
    pipeline_user_app = Pipeline(
        [
            node(
                func=predict_with_mlflow,
                inputs=dict(model="pipeline_inference_model", data="raw_inputs"),
                outputs="predictions",
                tags="user",
            )
        ]
    )

    return pipeline_user_app
