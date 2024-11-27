"""Exercise - Single Responsibility Principle.

Focus on the class `Model` and refactor it.

Make sure you take the following aspects into consideration:
    - Does class `Model` have a single responsibility, one reason to change?
    - Are all names intention-revealing?
    - What assumptions are made for the type of the instance attribute `data`?
        - What consequence can this assumption have and how could you prevent it?
"""

import pandas as pd
from sklearn.linear_model import LinearRegression


class Model:
    """Linear Regression Model."""

    def __init__(self, data: pd.DataFrame):
        """Initialize a model instance."""
        self.data = data
        self.model = None

    def train(self) -> None:
        """Train linear regression model."""
        # Preprocess data
        self.data = (self.data - self.data.mean()) / self.data.std()

        # Train model
        features = self.data.columns.difference(["target"])
        self.model = LinearRegression().fit(self.data[features], self.data["target"])

    def evaluate(self) -> float:
        """Evaluate model performance with Mean Squared Error (MSE)."""
        features = self.data.columns.difference(["target"])
        predictions = self.model.predict(self.data[features])
        mean_squared_error = ((predictions - self.data["target"]) ** 2).mean()
        return mean_squared_error


if __name__ == "__main__":
    input_data = {
        "feature1": [1, 2, 3, 4, 5],
        "feature2": [10, 20, 30, 40, 50],
        "feature3": [100, 200, 300, 400, 500],
        "target": [15, 25, 35, 45, 55]
    }

    input_data = pd.DataFrame(input_data)

    model = Model(input_data)
    model.train()
    mse = model.evaluate()
    print(f"MSE: {mse}")
