"""
This is a boilerplate pipeline 'user'
generated using Kedro 0.18.4
"""
import pandas as pd


def predict_with_mlflow(model, df):
    output = pd.DataFrame(model.predict(df), columns=["prediction"])
    return output
