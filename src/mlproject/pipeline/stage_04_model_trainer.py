from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_trainer import ModelTrainer
from mlproject import logger
from pathlib import Path

STAGE_NAME = "Model Trainer stage"


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Creating ConfigurationManager to manage project configurations.
        config = ConfigurationManager()

        # Retrieving model trainer configuration.
        model_trainer_config = config.get_model_trainer_config()

        # Creating ModelTrainer object with the obtained configuration.
        model_trainer = ModelTrainer(config=model_trainer_config)

        # Training the machine learning model.
        model_trainer.train()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelTrainerTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
