# Purpose: Data class definition for DataIngestionConfig.
# Creating a custom entity for 
"""Custom entities can be used to represent any type of object or concept that is not already defined in the Python standard library. 
They can be used to improve the readability and maintainability of your code."""

from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class DataIngestionConfig:
    """Data class for configuration related to data ingestion."""
    root_dir: Path             # Root directory for data ingestion artifacts.
    source_URL: str            # URL from which the data will be downloaded.
    local_data_file: Path      # Local path to store the downloaded data file.
    unzip_dir: Path            # Directory where the downloaded data will be extracted.


@dataclass(frozen=True)
class DataValidationConfig:
    """
    Data class for configuration related to data validation.

    Attributes:
        root_dir (Path): Root directory for data validation artifacts.
        STATUS_FILE (str): Path to the status file for recording validation status.
        unzip_data_dir (Path): Directory path of the data file for validation.
        all_schema (dict): Dictionary containing the schema for validation.
    """
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict


@dataclass(frozen=True)
class DataTransformationConfig:
    """
    Data class for configuration related to data transformation.

    Attributes:
        root_dir (Path): Root directory for data transformation artifacts.
        date_path (Path): Path to the input data file for transformation.
    """
    root_dir: Path
    data_path: Path


@dataclass(frozen=True)
class ModelTrainerConfig:
    """
    Data class for configuration related to model training.

    Attributes:
        root_dir (Path): Root directory for model training artifacts.
        train_data_path (Path): Path to the training data CSV file.
        test_data_path (Path): Path to the test data CSV file.
        model_name (str): File name for saving the trained machine learning model.
        alpha (float): Regularization strength for models that support regularization.
        l1_ratio (float): The mixing parameter for elastic net regularization.
        target_column (str): Name of the target column in the dataset.
    """
    root_dir: Path
    train_data_path: Path
    test_data_path: Path
    model_name: str
    alpha: float
    l1_ratio: float
    target_column: str


@dataclass(frozen=True)
class ModelEvaluationConfig:
    """
    Data class for configuration related to model evaluation.

    Attributes:
        root_dir (Path): Root directory for model evaluation artifacts.
        test_data_path (Path): Path to the test data CSV file.
        model_path (Path): Path to the trained machine learning model.
        all_params (dict): Dictionary containing all relevant parameters for model evaluation.
        metric_file_name (Path): File name for saving model evaluation metrics.
        target_column (str): Name of the target column in the dataset.
    """
    root_dir: Path
    test_data_path: Path
    model_path: Path
    all_params: dict
    metric_file_name: Path
    target_column: str
