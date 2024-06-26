Kidney Disease Classification MLflow DVC
### Workflows

1. Update config.yaml
2. Update params.yaml
3. Update the entity
4. Update the configuration manager in src config
5. Update the comp9nents
6. Update the pipeline
7. Update the main.py
8. Update the dvc.yaml
9. app.py


### Instalation

### STEPS:
Clone the repository
```bash
https://github.com/matusoff/ML_models/KidneyDiseaseDeepLearningProject
```
### STEP 01- Create a conda environment after opening the repository

conda create -p kidney python=3.8 -y
conda activate kidney

### STEP 02- install the requirements
```bash 
pip install -r requirements.txt
```

### Finally run the following command
python app.py 


### MLflow
[Documentation](https://mlflow.org/docs/latest/index.html)

'''
#### cmd
-mlflow ui
'''

### dagshub
[dagshub](https://dagshub.com)

MLFLOW_TRACKING_URI=https://dagshub.com/YourLink.mlflow

MLFLOW_TRACKING_USERNAME=YourUserName

MLFLOW_TRACKING_PASSWORD=YourTrackingPassword

python script.py

Run this to export as env variables:

### Linux or macOS
```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/YourLink.mlflow
export MLFLOW_TRACKING_USERNAME=YourUserName
export MLFLOW_TRACKING_PASSWORD=YourTrackingPassword
```

### Windows
```bash
set MLFLOW_TRACKING_URI=https://dagshub.com/YourLink.mlflow
set MLFLOW_TRACKING_USERNAME=YourUserName
set MLFLOW_TRACKING_PASSWORD=YourTrackingPassword
```


### DVC cmd

1. dvc init
2. dvc repro
3. dvc dag

### About MLflow & DVC

#### MLflow

- It is Production Grade
- Trace all of your expriements
- Logging & taging your model

#### DVC

- It is very lite weight for POC only
- lite weight expriements tracker
- It can perform Orchestration (Creating Pipelines)
