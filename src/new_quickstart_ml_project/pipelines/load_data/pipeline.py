"""
This is a boilerplate pipeline 'load_data'
generated using Kedro 0.18.4
"""

from kedro.pipeline import Pipeline, node, pipeline


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline([
        node(
            lambda x:x,
            inputs="input",
            outputs="output",
            name="load_data",
        )],
        inputs=["input"],
        outputs=["output"],
    )
