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