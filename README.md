# End-To-End-ML-Project
Common skeleton for end to end ml project with deployment

# Workflows

## 1. Update config.yaml
   - Modify the configuration file to reflect any changes in project settings.

## 2. Update schema.yaml
   - Make adjustments to the schema file to accommodate changes in data structure or model requirements.

## 3. Update params.yaml
   - Update parameter values as needed for the machine learning model or application.

## 4. Update the entity
   - If applicable, update the entity representation or definition in the project.

## 5. Update the configuration manager in src config
   - Modify the configuration manager in the 'src' directory to manage project configurations effectively.

## 6. Update the components
   - Make necessary updates to the individual components or modules within the project.

## 7. Update the pipeline
   - Adjust the machine learning pipeline to incorporate changes in data processing, model training, or evaluation.

## 8. Update main.py
   - Update the main script or module with any changes related to the core functionality of the project.

## 9. Update app.py
   - If applicable, update the application script or module for any changes related to deployment or interaction with the user interface.


# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/sridharstreaks/End-To-End-ML-Project/
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n mlproj python=3.8 -y
```

```bash
conda activate mlproj
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```