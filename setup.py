# File: setup.py
# Purpose: Configuration file for packaging the machine learning project as a Python package.

import setuptools  # Importing the setuptools library, used for packaging and distribution.

# Reading the README file for long description
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()
# Opens and reads the content of the README.md file to use as the long description of the package.

# Project metadata
__version__ = "0.0.0"  # Placeholder for the project version, typically updated during development.
REPO_NAME = "End-To-End-ML-Project"  # Name of the GitHub repository.
AUTHOR_USER_NAME = "sridharstreaks"  # GitHub username of the project author.
SRC_REPO = "mlProject"  # Name of the Python package.
AUTHOR_EMAIL = "sridharstreaks@gmail.com"  # Email address of the project author.

# Package setup
setuptools.setup(
    name=SRC_REPO,  # Name of the package.
    version=__version__,  # Version of the package.
    author=AUTHOR_USER_NAME,  # Author of the package.
    author_email=AUTHOR_EMAIL,  # Email of the author.
    description="A small python package for ml app",  # Short description of the package.
    long_description=long_description,  # Detailed description of the package from README.
    long_description_content_type="text/markdown",  # Type of long description (markdown in this case).
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",  # URL of the project repository.
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },  # Additional project URLs, in this case, the Bug Tracker.
    package_dir={"": "src"},  # Directory structure of the package (source code is in the "src" directory).
    packages=setuptools.find_packages(where="src")  # Find and include all packages in the "src" directory.
)
# Configures the package setup with the specified parameters, making it ready for distribution.
