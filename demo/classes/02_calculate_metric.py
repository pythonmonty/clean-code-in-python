"""Exercise - Open Closed Principle and Polymorphism.

Make sure you take the following aspects into consideration:
    - Is class `Model` open for extension but closed for modification?
    - How can you prevent the `if isinstance` checks here and in similar cases?
    - Does the class have one reason to change?
    - Is `Enum` the best base class to use for `SupportedModels`? Are there other implementations that come to mind?
"""

from enum import Enum
import logging
from sklearn.datasets import load_iris, fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, r2_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LinearRegression


class SupportedModels(Enum):
    """Supported machine learning models."""
    classifier = DecisionTreeClassifier
    regressor = LinearRegression


class Model:

    def __init__(self, model):
        self.model = model

    def calculate_metric(self, y_true, y_predicted):
        """Calculate metrics for a given model.

        :param y_true: True values of the model target.
        :param y_predicted: Predicted values of the model target.
        """
        if isinstance(self.model, SupportedModels.classifier.value):
            # Calculate accuracy for classifier
            metric = accuracy_score(y_true, y_predicted)
            logging.info(f"Model: {self.model.__class__.__name__}, "
                         f"Accuracy: {metric:.4f}")
        elif isinstance(self.model, SupportedModels.regressor.value):
            # Calculate R² for regressor
            metric = r2_score(y_true, y_predicted)
            logging.info(f"Model: {self.model.__class__.__name__}, "
                         f"R²: {metric:.4f}")
        else:
            raise NotImplementedError(f"Metrics for {self.model.__class__.__name__} "
                                      f"are not implemented.")
        return metric


if __name__ == "__main__":
    # Load datasets
    iris = load_iris()
    housing = fetch_california_housing()

    # Classification datasets
    X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(
        iris.data,
        iris.target,
        test_size=0.3,
        random_state=42,
    )

    # Regression datasets
    X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(
        housing.data,
        housing.target,
        test_size=0.3,
        random_state=42,
    )

    # Create instances of a classifier and a regressor
    classifier = Model(DecisionTreeClassifier())
    regressor = Model(LinearRegression())

    # Fit the models
    classifier.model.fit(X_train_cls, y_train_cls)
    regressor.model.fit(X_train_reg, y_train_reg)

    # Make predictions
    y_pred_cls = classifier.model.predict(X_test_cls)
    y_pred_reg = regressor.model.predict(X_test_reg)

    # Calculate metrics for each model
    accuracy = classifier.calculate_metric(y_test_cls, y_pred_cls)
    r2 = regressor.calculate_metric(y_test_reg, y_pred_reg)

    print(f"Accuracy: {accuracy}")
    print(f"R2: {r2}")
