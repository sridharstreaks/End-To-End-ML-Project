from mlproject.config.configuration import ConfigurationManager
from mlproject.components.data_validation import DataValidation
from mlproject import logger

STAGE_NAME = "Data Validation stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Creating ConfigurationManager to manage project configurations.
        config = ConfigurationManager()

        # Retrieving data validation configuration.
        data_validation_config = config.get_data_validation_config()

        # Creating DataValidation object with the obtained configuration.
        data_validation = DataValidation(config=data_validation_config)

        # Performing data validation.
        data_validation.validate_all_columns()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
