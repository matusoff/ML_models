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
```bash pip install -r requirements.txt
```

### Finally run the following command
python app.py 

Now, open up you local host and port MLflow Documentation

MLflow tutorial

cmd mlflow ui dagshub dagshub

MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/Kidney-Disease-Classification-MLflow-DVC.mlflow MLFLOW_TRACKING_USERNAME=entbappy MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 python script.py

Run this to export as env variables:

export MLFLOW_TRACKING_URI=https://dagshub.com/entbappy/Kidney-Disease-Classification-MLflow-DVC.mlflow

export MLFLOW_TRACKING_USERNAME=entbappy

export MLFLOW_TRACKING_PASSWORD=6824692c47a369aa6f9eac5b10041d5c8edbcef0 DVC cmd dvc init dvc repro dvc dag About MLflow & DVC MLflow

Its Production Grade Trace all of your expriements Logging & taging your model DVC

Its very lite weight for POC only lite weight expriements tracker It can perform Orchestration (Creating Pipelines) AWS-CICD-Deployment-with-Github-Actions

Login to AWS console.

Create IAM user for deployment #with specific access

EC2 access : It is virtual machine

ECR: Elastic Container registry to save your docker image in aws

#Description: About the deployment

Build docker image of the source code

Push your docker image to ECR

Launch Your EC2

Pull Your image from ECR in EC2

Lauch your docker image in EC2

#Policy:

AmazonEC2ContainerRegistryFullAccess

AmazonEC2FullAccess

Create ECR repo to store/save docker image

Save the URI: 566373416292.dkr.ecr.us-east-1.amazonaws.com/chicken
Create EC2 machine (Ubuntu)
Open EC2 and Install docker in EC2 Machine: #optinal
sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker 6. Configure EC2 as self-hosted runner: setting>actions>runner>new self hosted runner> choose os> then run command one by one 7. Setup github secrets: AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI =

ECR_REPOSITORY_NAME = simple-app