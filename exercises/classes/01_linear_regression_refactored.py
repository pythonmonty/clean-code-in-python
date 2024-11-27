"""Exercise 01_linear_regression.py - Refactored."""
from typing import Any

import pandas as pd
from sklearn.linear_model import LinearRegression


class TrainingDataStandardizer:
    """Standardizer for training data."""

    def __init__(self, data: pd.DataFrame):
        """Instantiate a standardizer for training data."""
        self.data = data

    def standardize(self) -> None:
        """Standardize the data by removing the mean and dividing by standard deviation."""
        self.data = (self.data - self.data.mean()) / self.data.std()


class LinearRegressionTrainer:
    """Linear Regression trainer class."""

    def __init__(self):
        """Instantiate an empty model."""
        self.model = None

    def train(self, features: pd.DataFrame, target: pd.Series) -> object:
        """Train a linear regression model."""
        self.model = LinearRegression().fit(features, target)
        return self.model


class MeanSquaredErrorEvaluator:
    """Mean Squared Error evaluator."""

    @staticmethod
    def evaluate(model: Any, features: pd.DataFrame, target: pd.Series) -> float:
        """Evaluate the Mean Squared Error given the features and the target."""
        predictions = model.predict(features)
        mean_squared_error = ((predictions - target) ** 2).mean()
        return mean_squared_error


if __name__ == "__main__":
    input_data = {
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [10, 20, 30, 40, 50],
        "feature3": [100, 200, 300, 400, 500],
        "target": [15, 25, 35, 45, 55]
    }

    input_data = pd.DataFrame(input_data)

    # Standardize data
    standardizer = TrainingDataStandardizer(input_data)
    standardizer.standardize()
    print(f"Standardized data:\n {standardizer.data}")

    # Train model
    input_data_target = standardizer.data["target"]
    input_data_features = standardizer.data[standardizer.data.columns.difference(["target"])]
    linear_model = LinearRegressionTrainer().train(input_data_features, input_data_target)

    # Calculate MSE
    MeanSquaredErrorEvaluator().evaluate(linear_model, input_data_features, input_data_target)
