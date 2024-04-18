# Automated Machine Learning App

Streamlit web application allows users to upload datasets, perform exploratory data analysis, model their data using various machine learning algorithms, and download the best performing model. It leverages powerful libraries such as Pandas, PyCaret, and Pandas Profiling to provide a comprehensive tool for machine learning tasks.

## Features

- **Data Upload**: Users can upload their own CSV files to start the analysis.
- **Data Profiling**: Generate and view a detailed exploratory data analysis report using Pandas Profiling.
- **Model Building**: Automatically compare different machine learning models and select the best one.
- **Model Download**: Download the trained model for offline use.

## Installation

To run this project locally, you need to have Python installed on your machine (Python 3.7-3.10 recommended). You can then follow these steps:

1. Install the required dependencies:
   ```
   pip install -r requirements.txt
   
   ```

2. Run the Streamlit application:
    ```
   streamlit run test.py
   
   ```
 
## Usage
After installation, the application will start running on your local server. You can access it by navigating to http://localhost:8501 in your web browser. Here’s how to use the application:

- Upload: Navigate to the 'Upload' tab in the sidebar to upload your dataset.
- Profiling: After uploading, select the 'Profiling' tab to view a detailed report of your dataset.
- Machine Learning: Choose the 'Machine Learning' tab to build and compare models. Select your target variable and press 'Run Modelling' to start the process.
- Download: After modeling, you can download the best performing model from the 'Download' tab.


