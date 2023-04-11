# flake8: noqa
from pathlib import Path
import numpy as np
import pandas as pd
import streamlit as st
from kedro.config import ConfigLoader
from kedro.framework.project import settings
from kedro.framework.startup import bootstrap_project
from kedro.io import DataCatalog

st.set_option("deprecation.showPyplotGlobalUse", False)

st.set_page_config(page_title="User app", layout="wide")

bootstrap_project = st.cache_resource(bootstrap_project)
bootstrap_project(Path.cwd())

def get_data_catalog(env: str):
    conf_path = str(settings.CONF_SOURCE)
    conf_loader = ConfigLoader(
        conf_source=conf_path, env=env
    )

    conf_catalog = conf_loader.get("catalog*", "catalog*/**")

    # Load parameters
    conf_params = conf_loader.get("parameters*/**")

    catalog = DataCatalog.from_config(conf_catalog)
    return catalog, conf_params

catalog, conf_params = get_data_catalog("local")

# Cache (expensive) operations to speed up the dashboard
@st.cache_data
def load_data(_catalog, name: str) -> pd.DataFrame:
    return _catalog.load(name)

df = load_data(catalog, "output")

st.dataframe(df)