"""
This is a boilerplate pipeline 'deploy'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import deploy, create_endpoint, test


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=create_endpoint,
                inputs=["params:endpoint_name", "params:endpoint_config"],
                outputs="endpoint_confirmation",
                name="create_endpoint",
                tags=["deployment"],
            ),
            node(
                func=deploy,
                inputs=[
                    "params:deployment_name",
                    "params:deploy_config",
                    "params:traffic_config",
                    "params:endpoint_name",
                    "params:model_name",
                    "endpoint_confirmation",
                ],
                outputs="deployment_confirmation",
                name="deploy",
                tags=["deployment"],
            ),
            node(
                func=test,
                inputs=["params:endpoint_name", "deployment_confirmation"],
                outputs=None,
                name="test",
                tags=["deployment"],
            ),
        ]
    )
