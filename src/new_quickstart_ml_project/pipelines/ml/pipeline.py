"""
This is a boilerplate pipeline
generated using Kedro 0.18.7
"""

from kedro.pipeline import Pipeline, node, pipeline

from .nodes import make_predictions, split_data, train_model, preprocess


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func = preprocess,
                inputs = "inputs",
                outputs= "features",
                name="preprocess_features",
                tags=["training", "inference"],
            ),
            node(
                func=split_data,
                inputs=[
                    "features",
                    "labels",
                    "params:train_fraction",
                    "params:random_state",
                ],
                outputs=["X_train", "X_test", "y_train", "y_test"],
                name="split",
                tags=["training"],
            ),
            node(
                func=train_model,
                inputs=["X_train", "X_test", "y_train", "y_test", "params:n_neighbors"],
                outputs=["trained_model", "accuracy"],
                name="train_model",
                tags=["training"],
            ),
            node(
                func=make_predictions,
                inputs=["trained_model", "features"],
                outputs="y_pred",
                name="make_predictions_inference",
                tags=["inference"],
            ),
        ]
    )
