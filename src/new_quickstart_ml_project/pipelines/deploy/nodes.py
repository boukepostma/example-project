"""
This is a boilerplate pipeline 'deploy'
generated using Kedro 0.18.4
"""
from typing import Dict
import json
import mlflow
import pandas as pd
from mlflow.deployments import get_deploy_client
import os


def create_endpoint(endpoint_name: str, endpoint_config: Dict[str, str]) -> bool:
    deployment_client = get_deploy_client(mlflow.get_tracking_uri())

    endpoint_config_path = "endpoint_config.json"
    with open(endpoint_config_path, "w") as outfile:
        outfile.write(json.dumps(endpoint_config))

    try:
        deployment_client.create_endpoint(
            name=endpoint_name,
            config={"endpoint-config-file": endpoint_config_path},
        )
        os.remove(endpoint_config_path)
    except:
        os.remove(endpoint_config_path)
        raise
    return True


def deploy(
    deployment_name,
    deploy_config,
    traffic_config,
    endpoint_name,
    model_name,
    endpoint_confirmation,
) -> bool:
    if not endpoint_confirmation:
        raise ValueError("endpoint_confirmation should be True")

    deployment_client = get_deploy_client(mlflow.get_tracking_uri())

    deployment_config_path = "deployment_config.json"
    with open(deployment_config_path, "w") as outfile:
        outfile.write(json.dumps(deploy_config))

    traffic_config_path = "traffic_config.json"
    with open(traffic_config_path, "w") as outfile:
        outfile.write(json.dumps(traffic_config))

    try:
        deployment_client.create_deployment(
            name=deployment_name,
            endpoint=endpoint_name,
            model_uri=f"models:/{model_name}/None",
            config={"deploy-config-file": deployment_config_path},
        )

        deployment_client.update_endpoint(
            endpoint=endpoint_name,
            config={"endpoint-config-file": traffic_config_path},
        )
        os.remove(traffic_config_path)
        os.remove(deployment_config_path)
    except:
        os.remove(traffic_config_path)
        os.remove(deployment_config_path)
        raise
    return True


def test(endpoint_name, deployment_confirmation):
    if not deployment_confirmation:
        raise ValueError("deployment_confirmation should be True")

    deployment_client = get_deploy_client(mlflow.get_tracking_uri())
    cols = "sepal_length,sepal_width,petal_length,petal_width".split(",")
    vals = [5.1, 3.5, 1.4, 0.2]
    data = {"columns": cols, "data": [vals], "index": [0]}
    samples = pd.DataFrame(**data)

    print(deployment_client.predict(endpoint=endpoint_name, df=samples))
