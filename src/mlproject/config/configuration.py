# Purpose: Main script or module for the machine learning project.

# Importing constants and utility functions from mlproject package.
from mlproject.constants import *
from mlproject.utils.common import read_yaml,create_directories
from mlproject.entity.config_entity import DataIngestionConfig,DataValidationConfig

# Purpose: Definition of the ConfigurationManager class for managing project configurations.

class ConfigurationManager:
    def __init__(
        self,
        config_filepath=CONFIG_FILE_PATH,
        params_filepath=PARAMS_FILE_PATH,
        schema_filepath=SCHEMA_FILE_PATH):
        """
        Initializes the ConfigurationManager with default or provided file paths.

        Args:
            config_filepath (Path, optional): Path to the configuration file. Defaults to CONFIG_FILE_PATH.
            params_filepath (Path, optional): Path to the parameters file. Defaults to PARAMS_FILE_PATH.
            schema_filepath (Path, optional): Path to the schema file. Defaults to SCHEMA_FILE_PATH.
        """
        # Reading configuration, parameters, and schema files using read_yaml function.
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        self.schema = read_yaml(schema_filepath)

        # Creating the root directory for project artifacts.
        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        """
        Gets the configuration for data ingestion.

        Returns:
            DataIngestionConfig: Data class containing data ingestion configuration.
        """
        # Extracting data ingestion configuration from the overall project configuration.
        config = self.config.data_ingestion

        # Creating the root directory for data ingestion artifacts.
        create_directories([config.root_dir])

        # Creating a DataIngestionConfig object with the extracted configuration.
        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config
    


    def get_data_validation_config(self) -> DataValidationConfig:
        """
        Retrieves the configuration for data validation.

        Returns:
            DataValidationConfig: Data class containing data validation configuration.
        """
        # Extracting data validation configuration and schema from the overall project configuration.
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        # Creating the root directory for data validation artifacts.
        create_directories([config.root_dir])

        # Creating a DataValidationConfig object with the extracted configuration.
        data_validation_config = DataValidationConfig(
            root_dir=config.root_dir,
            STATUS_FILE=config.STATUS_FILE,
            unzip_data_dir=config.unzip_data_dir,
            all_schema=schema,
        )

        return data_validation_config
