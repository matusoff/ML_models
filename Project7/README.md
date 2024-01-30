Overview
The goal of this model is to predict whether or not a Waze user is retained or churned.

This modeling has three parts:

Part 1: Ethical considerations
Should the objective of the model be adjusted?

Part 2: Feature engineering
Perform feature selection, extraction, and transformation to prepare the data for modeling

Part 3: Modeling
Build the models, evaluate them, and advise on the next steps.

Business Scenario

The Leadership at Waze (mobile app for drivers) has requested the development of a machine learning model to predict user churn in their app.
To achieve the best results, it has been decided to build and test two tree-based models: Random Forest and XGBoost."

Data Understanding
This project uses a dataset called waze_dataset.csv. It contains synthetic data created for this project in partnership with Waze.
The data consisted of approximately 15k unique trips and 13 features.
The features included information on:
column

Column Name | Type | Description
ID | int | A sequential numbered index
label | obj | Binary target variable (“retained” vs “churned”) for if a user has churned anytime during the course of the month
sessions | int | The number of occurrences of a user opening the app during the month
drives | int | An occurrence of driving at least 1 km during the month
device | obj | The type of device a user starts a session with
total_sessions | float | A model estimate of the total number of sessions since a user has onboarded
n_days_after_onboarding | int | The number of days since a user signed up for the app
total_navigations_fav1 | int | Total navigations since onboarding to the user’s favorite place 1
total_navigations_fav2 | int | Total navigations since onboarding to the user’s favorite place 2
driven_km_drives | float | Total kilometers driven during the month
duration_minutes_drives | float | Total duration driven in minutes during the month
activity_days | int | Number of days the user opens the app during the month
driving_days | int | Number of days the user drives (at least 1 km) during the month
