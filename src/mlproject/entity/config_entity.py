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
