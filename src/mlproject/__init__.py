# File: __init__.py
# Purpose: Initialization file for the mlProject package, configuring logging settings.

import os  # Operating system interface.
import sys  # System-specific parameters and functions.
import logging  # Logging framework for tracking events in the package.

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
# Logging format string to define the structure of log messages.

log_dir = "logs"  # Directory to store log files.
log_filepath = os.path.join(log_dir, "running_logs.log")  # Full path for the log file.
os.makedirs(log_dir, exist_ok=True)  # Creates the log directory if it doesn't exist.

logging.basicConfig(
    level=logging.INFO,  # Sets the logging level to INFO.
    format=logging_str,  # Specifies the format of log messages.

    handlers=[
        logging.FileHandler(log_filepath),  # Writes log messages to a file.
        logging.StreamHandler(sys.stdout)  # Outputs log messages to the console.
    ]
)
# Configures the logging system with the specified settings.

logger = logging.getLogger("mlprojectlogger")
# Creates a logger object named "mlprojectlogger" for use in the mlProject package.
