"""Exercise 02_calculate_metric.py - Refactored."""

from abc import ABC, abstractmethod
from typing import Any, Protocol, runtime_checkable

import pandas as pd
from sklearn.datasets import fetch_california_housing, load_iris
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, r2_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier


@runtime_checkable
class MLModelInterface(Protocol):
    """Abstract interface for the representation of Machine Learning models."""

    def fit(self, *args, **kwargs) -> Any:
        """Fit an ML model."""
        pass

    def predict(self, *args, **kwargs) -> Any:
        """Predict with an ML model."""
        pass


class CalculateMetricBaseModel(ABC):
    """Abstract base class for models with a method to calculate metrics."""

    def __init__(self, model: MLModelInterface, metric_function: callable):
        """Instantiate a CalculateMetricBaseModel instance."""
        self.model = model
        self.metric_function = metric_function

    @abstractmethod
    def calculate_metric(self, *args, **kwargs):
        """Calculate metric abstract method."""
        pass


class CalculateMetricMixin:
    """Mixin class providing a concrete implementation for calculate_metric."""

    def calculate_metric(self, features: pd.DataFrame, target: pd.Series):
        """Calculate metric implementation given a metric function."""
        predicted_target = self.model.predict(features)
        metric = self.metric_function(target, predicted_target)
        return metric


class ClassifierModel(CalculateMetricMixin, CalculateMetricBaseModel):
    """Classifier model type."""

    def __init__(self):
        """Instantiate a Decision Tree Classifier model."""
        model = DecisionTreeClassifier()
        metric_function = accuracy_score
        super().__init__(model, metric_function)


class RegressorModel(CalculateMetricMixin, CalculateMetricBaseModel):
    """Regressor model type."""

    def __init__(self):
        """Instantiate a Linear Regression model."""
        model = LinearRegression()
        metric_function = r2_score
        super().__init__(model, metric_function)


if __name__ == "__main__":
    # Load datasets
    iris = load_iris()
    housing = fetch_california_housing()

    # Split datasets into training and testing sets
    X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(
        iris.data,
        iris.target,
        test_size=0.3,
        random_state=42,
    )
    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
        housing.data,
        housing.target,
        test_size=0.3,
        random_state=42,
    )

    classifier = ClassifierModel()
    classifier.model.fit(X_train_cls, y_train_cls)
    print(classifier.calculate_metric(X_test_cls, y_test_cls))

    regressor = RegressorModel()
    regressor.model.fit(X_train_reg, y_train_reg)
    print(regressor.calculate_metric(X_test_reg, y_test_reg))
