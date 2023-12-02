import pandas as pd
import os
from mlproject import logger
from sklearn.linear_model import ElasticNet
import joblib
from mlproject.entity.config_entity import ModelEvaluationConfig
import numpy as np
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score
from mlproject.utils.common import save_json
from pathlib import Path

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        """
        Initializes the ModelEvaluation object with the provided configuration.

        Args:
            config (ModelEvaluationConfig): ModelEvaluationConfig object containing model evaluation settings.
        """
        self.config = config

    def eval_metrics(self, actual, pred):
        """
        Calculates evaluation metrics including RMSE, MAE, and R2.

        Args:
            actual: Ground truth values.
            pred: Predicted values.

        Returns:
            Tuple: Tuple containing RMSE, MAE, and R2.
        """
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2

    def save_results(self):
        """
        Loads the test data and the trained model, predicts on the test data, calculates metrics, and saves them.

        Returns:
            None
        """
        # Reading test data and trained model.
        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        # Extracting features and target variable from the test data.
        test_x = test_data.drop([self.config.target_column], axis=1)
        test_y = test_data[[self.config.target_column]]

        # Predicting target variable on the test data.
        predicted_qualities = model.predict(test_x)

        # Calculating evaluation metrics.
        (rmse, mae, r2) = self.eval_metrics(test_y, predicted_qualities)

        # Saving metrics as a JSON file locally.
        scores = {"rmse": rmse, "mae": mae, "r2": r2}
        save_json(path=Path(self.config.metric_file_name), data=scores)
