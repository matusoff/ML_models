Protein Prediction App based on Meta AI ESM model

## Overview
The **Protein Prediction App** is a web application that leverages state-of-the-art deep learning models to predict the 3D structure of proteins based on their amino acid sequences. This app uses the ESMFold model to provide structure predictions directly from protein sequences.

 [image](https://github.com/matusoff/ML_models/assets/94809104/203d0732-7c9c-4c17-ba96-e09ba59dc9d4)

## Features
- 🧬 **Protein Sequence Input:** Users can input protein sequences in the text area.
- 🧩 **Structure Prediction:** Uses ESMFold to predict protein structures.
- 📊 **Visualization:** Displays the predicted 3D structure using Py3DMol.
- 💾 **Download:** Allows users to download the predicted PDB files.

## Getting Started
To run the Protein Prediction App on your local machine, follow these steps:

### Prerequisites
Ensure you have Python 3.7+ installed along with the following libraries:
- `streamlit`
- `torch`
- `fair-esm`
- `requests`
- `py3dmol`
- `biotite`

Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

### Running the App
1. Start the Streamlit server:
    ```bash
    streamlit run app_v2.py
    ```
2. Open your web browser and navigate to `http://localhost:8501` to view the app.

## Usage
1. Enter the amino acid sequence of the protein in the input field.
2. Click the `Predict` button to generate the predicted 3D structure.
3. View the predicted structure and download the PDB file if needed.
