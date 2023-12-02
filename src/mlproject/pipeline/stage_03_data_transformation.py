from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_transformation import DataTransformation
from mlproject import logger
from pathlib import Path


STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Purpose: Main script or module for the machine learning project.

        try:
            # Reading the status from the data validation process.
            with open(Path("artifacts/data_validation/status.txt"), "r") as f:
                status = f.read().split(" ")[-1]

            # Checking if the data validation was successful based on the status.
            if status == "True":
                # If validation is successful, proceed with data transformation.
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.train_test_splitting()

            else:
                # If validation is not successful, raise an exception.
                raise Exception("Your data schema is not valid")

        except Exception as e:
            # Handling and printing any exceptions that occur during the process.
            print(e)
