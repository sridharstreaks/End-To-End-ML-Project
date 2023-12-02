from mlproject.config.configuration import ConfigurationManager
from mlproject.components.model_evaluation import ModelEvaluation
from mlproject import logger
from pathlib import Path

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        # Creating ConfigurationManager to manage project configurations.
        config = ConfigurationManager()

        # Retrieving model evaluation configuration.
        model_evaluation_config = config.get_model_evaluation_config()

        # Creating ModelEvaluation object with the obtained configuration.
        model_evaluation = ModelEvaluation(config=model_evaluation_config)

        # Saving evaluation results, including metrics.
        model_evaluation.save_results()


if __name__ == '__main__':
    try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj = ModelEvaluationTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
    except Exception as e:
        logger.exception(e)
        raise e
