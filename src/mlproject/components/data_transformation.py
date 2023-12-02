import os
from mlproject import logger
from sklearn.model_selection import train_test_split
import pandas as pd
from mlproject.entity.config_entity import DataTransformationConfig



# Purpose: Definition of the DataTransformation class for handling data transformation.

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        """
        Initializes the DataTransformation object with the provided configuration.

        Args:
            config (DataTransformationConfig): DataTransformationConfig object containing data transformation settings.
        """
        self.config = config

    ## Note: You can add different data transformation techniques such as Scaler, PCA, and all
    # You can perform all kinds of EDA in ML cycle here before passing this data to the model

    # I am only adding train_test_splitting because this data is already cleaned up

    def train_test_splitting(self):
        """
        Performs train-test splitting on the data and saves the resulting sets to CSV files.
        """
        # Reading the data file into a pandas DataFrame.
        data = pd.read_csv(self.config.data_path)

        # Splitting the data into training and test sets using a default split ratio of (0.75, 0.25).
        train, test = train_test_split(data)

        # Saving the training and test sets to CSV files in the root directory for data transformation artifacts.
        train.to_csv(os.path.join(self.config.root_dir, "train.csv"), index=False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"), index=False)

        # Logging information about the split.
        logger.info("Split data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        # Printing the shapes of the resulting sets.
        print(train.shape)
        print(test.shape)
