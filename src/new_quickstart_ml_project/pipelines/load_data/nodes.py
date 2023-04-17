"""
This is a boilerplate pipeline
generated using Kedro 0.18.7
"""

import logging
from typing import  Tuple

import pandas as pd
import numpy as np

from sklearn.neighbors import KNeighborsClassifier

def split_data(
    data: pd.DataFrame, 
    labels: pd.DataFrame,
    train_fraction: float,
    random_state: int,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.Series, pd.Series]:
    """Splits data into features and target training and test sets.

    Args:
        data: Data containing features and target.
        parameters: Parameters defined in parameters.yml.
    Returns:
        Split data.
    """
    data_train_idx = data.sample(
        frac=train_fraction, random_state=random_state
    ).index
    X_train = data.loc[data_train_idx,:]
    X_test = data.drop(data_train_idx)
    y_train = labels.loc[data_train_idx,:]
    y_test = labels.drop(data_train_idx)
    return X_train, X_test, y_train, y_test

def train_model(
    X_train: pd.DataFrame,
    X_test: pd.DataFrame,
    y_train: pd.DataFrame,
    y_test: pd.DataFrame,
    n_neighbors: int
) -> KNeighborsClassifier:
    model = KNeighborsClassifier(n_neighbors)
    trained_model = model.fit(X_train, np.ravel(y_train))
    y_pred = trained_model.predict(X_test)
    accuracy = (y_pred == y_test.iloc[:,0].values).sum() / len(y_test)
    return trained_model, accuracy

def make_predictions(
    trained_model: KNeighborsClassifier, X: pd.DataFrame
) -> pd.Series:
    """Uses fitted nearest neighbor classifier to create predictions.

    Args:
        trained_model: Fitted nearest neighbor model
        X: Test data for features.

    Returns:
        y_pred: Prediction of the target variable.
    """
    return trained_model.predict(X)

def preprocess(x):
    return x