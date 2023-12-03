# File: prediction_pipeline.py
# Purpose: Definition of the PredictionPipeline class for making predictions using a trained model.

import joblib  # Library for saving and loading scikit-learn models.
import numpy as np  # Numerical operations library.
import pandas as pd  # Data manipulation library.
from pathlib import Path  # Object-oriented interface to filesystem paths.

class PredictionPipeline:
    def __init__(self):
        """
        Initializes the PredictionPipeline object by loading a pre-trained machine learning model.

        Model path: 'artifacts/model_trainer/model.joblib'
        """
        # Loading the pre-trained machine learning model into the 'model' attribute.
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    def predict(self, data):
        """
        Makes predictions using the loaded machine learning model.

        Args:
            data: Input data for prediction.

        Returns:
            prediction: Predicted values.
        """
        # Using the loaded model to make predictions on the input data.
        prediction = self.model.predict(data)

        # Returning the predicted values.
        return prediction
