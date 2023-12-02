import os
from mlproject import logger
import pandas as pd
from mlproject.entity.config_entity import DataValidationConfig


# Purpose: Definition of the DataValidation class for handling data validation.

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        """
        Initializes the DataValidation object with the provided configuration.

        Args:
            config (DataValidationConfig): DataValidationConfig object containing data validation settings.
        """
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validates all columns in the data file against the specified schema.

        Returns:
            bool: True if all columns are present in the schema, False otherwise.
        """
        try:
            validation_status = None

            # Reading the data file into a pandas DataFrame.
            data = pd.read_csv(self.config.unzip_data_dir)
            
            # Extracting the column names from the data.
            all_cols = list(data.columns)

            # Extracting the expected columns from the schema.
            all_schema = self.config.all_schema.keys()

            # Validating each column against the schema.
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")
                else:
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"Validation status: {validation_status}")

            return validation_status

        except Exception as e:
            # Handling and re-raising any exceptions that occur during the validation process.
            raise e
