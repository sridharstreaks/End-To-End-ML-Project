import os
from pathlib import Path
import logging

# creating a logging string to capture the logs with time and message
logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')

# Create a variable to hold the name of the main project folder which will contain all project related resources
project_name = "mlproject"

list_of_files = [
    f"src/{project_name}/__init__.py",  # Initialization file for the main project module

    f"src/{project_name}/components/__init__.py",  # Initialization file for the components module

    f"src/{project_name}/utils/__init__.py",  # Initialization file for the utilities module
    f"src/{project_name}/utils/common.py",  # Common utility functions used across the project

    f"src/{project_name}/config/__init__.py",  # Initialization file for the configuration module

    f"src/{project_name}/config/configuration.py",  # Configuration settings for the project

    f"src/{project_name}/pipeline/__init__.py",  # Initialization file for the pipeline module

    f"src/{project_name}/entity/__init__.py",  # Initialization file for the entity module

    f"src/{project_name}/entity/config_entity.py",  # Entity class for handling configuration data

    f"src/{project_name}/constants/__init__.py",  # Initialization file for the constants module

    "config/config.yaml",  # YAML file containing general project configuration

    "params.yaml",  # YAML file containing parameters for the machine learning model

    "schema.yaml",  # YAML file specifying the schema for data inputs or outputs

    "main.py",  # Main Python script for running the project

    "app.py",  # Python script defining the application logic

    "requirements.txt",  # File listing required Python packages and their versions

    "setup.py",  # Script for packaging and distributing the project

    "research/trials.ipynb",  # Jupyter Notebook for documenting research trials and experiments

    "templates/index.html",  # HTML template file for the project's web interface
]

for filepath in list_of_files:
    filepath = Path(filepath) #converts path based on the os (here windows)

    filedir, filename = os.path.split(filepath) #os.path.split breaksdown a fullpath into filename and directoryname

    if filedir !="":
        os.makedirs(filedir,exist_ok=True) #checks if the directory already exists
        logging.info(f"creating directory; {filedir} for the file: {filename}") #logs the creation of file directory

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass  # Creates an empty file if it doesn't exist or is empty
            logging.info(f"creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")  # Logs that the file already exists

