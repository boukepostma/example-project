"""
This is a boilerplate pipeline 'user'
generated using Kedro 0.18.4
"""

def predict_with_mlflow(model, data):
    print("input:", data)
    output = model.predict(data)
    print("output", output)
    return output