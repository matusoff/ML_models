import streamlit as st
import plotly.express as px 

import os
import pandas as pd

import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

from pycaret.regression import setup, compare_models, pull, save_model

with st.sidebar: 
    st.image("https://www.onepointltd.com/wp-content/uploads/2020/03/inno2.png")
    st.title("Auto Streamlit")
    choice = st.radio("Navigation", ["Upload", "Profile", "Machine Learning", "Download"])
    st.info("Hello")

if os.path.exists("dataset.csv"): 
    df = pd.read_csv('dataset.csv', index_col=None)


if choice == "Upload": 
    st.title("Upload")
    file = st.file_uploader("Upload Your Dataset")
    if file: 
        df = pd.read_csv(file, index_col=None)
        df.to_csv("dataset.csv", index=None)
        st.dataframe(df)

if choice == "Profile": 
    st.title("Profile")
    profile_df = df.profile_report()
    st_profile_report(profile_df)


if choice == "Machine Learning": 
    if 'df' in locals() or 'df' in globals():  # Check if df is defined
        chosen_target = st.selectbox('Choose the Target Column', df.columns)
        if st.button('Run Modelling'): 
            # Sample the data to speed up the process, adjust the fraction as needed
            sample_df = df.sample(frac=0.1, random_state=123) if len(df) > 5000 else df

            # Setup with simplified parameters to minimize initial computation overhead
            setup_data = setup(data=sample_df, target=chosen_target, session_id=123, silent=True, 
                               numeric_imputation='mean',  # Impute missing numerics
                               categorical_imputation='mode',  # Impute missing categoricals
                               ignore_features=[],  # List any features to ignore here
                               verbose=False)  # Reduce output to streamline processing

            # Compare a few simple models to identify if a specific model is causing the issue
            best_model = compare_models(include=['lr', 'ridge', 'lasso', 'rf', 'gbr', 'ada', 'knn', 'et'], n_select=1, verbose=False)

            # Retrieve and display the performance metrics of the best model
            compare_df = pull()
            st.dataframe(compare_df)

            # Save the best model
            save_model(best_model, 'best_model')
    else:
        st.error("No dataset loaded. Please upload a dataset first.")


if choice == "Download":
    with open("best_model.pkl", 'rb') as f: 
        st.download_button("Download Model", f, "best_model_test.pkl")
