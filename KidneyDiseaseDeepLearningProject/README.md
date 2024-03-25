Kidney Disease Classification MLflow DVC
### Workflows

1. Update config.yaml
2. Update secrets.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the dvc.yaml
10. app.py


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

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/YourLink.mlflow
export MLFLOW_TRACKING_USERNAME=YourUserName
export MLFLOW_TRACKING_PASSWORD=YourTrackingPassword
```
