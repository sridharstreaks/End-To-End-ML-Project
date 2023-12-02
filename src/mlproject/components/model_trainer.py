import pandas as pd
import os
from mlproject import logger
from sklearn.linear_model import ElasticNet
import joblib
from mlproject.entity.config_entity import ModelTrainerConfig

# Purpose: Definition of the ModelTrainer class for training a machine learning model.

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        """
        Initializes the ModelTrainer object with the provided configuration.

        Args:
            config (ModelTrainerConfig): ModelTrainerConfig object containing model training settings.
        """
        self.config = config

    def train(self):
        """
        Trains a machine learning model using ElasticNet regression.
        """
        # Reading training and test data from CSV files.
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)

        # Extracting features and target variables from the data.
        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]

        # Creating an ElasticNet regression model with specified alpha and l1_ratio.
        lr = ElasticNet(alpha=self.config.alpha, l1_ratio=self.config.l1_ratio, random_state=42)

        # Training the model on the training data.
        lr.fit(train_x, train_y)

        # Saving the trained model using joblib in the specified root directory.
        joblib.dump(lr, os.path.join(self.config.root_dir, self.config.model_name))
