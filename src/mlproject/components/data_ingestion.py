import os  # Operating system interface.
import urllib.request as request  # URL handling module.
import zipfile  # ZIP file processing module.
from mlproject import logger  # Logger specific to the mlProject package.
from mlproject.utils.common import get_size  # Common utility function for file size.
from mlproject.entity.config_entity import DataIngestionConfig
from pathlib import Path

# Purpose: Definition of the DataIngestion class for handling data download and extraction.

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        """
        Initializes the DataIngestion object with the provided configuration.

        Args:
            config (DataIngestionConfig): DataIngestionConfig object containing data ingestion settings.
        """
        self.config = config

    def download_file(self):
        """
        Downloads the data file from the specified source URL and logs the download information.
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"{filename} downloaded! with the following info:\n{headers}")
        else:
            logger.info(f"File already exists of size: {get_size(Path(self.config.local_data_file))}")

    def extract_zip_file(self):
        """
        Extracts the contents of the ZIP file into the specified directory.
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
