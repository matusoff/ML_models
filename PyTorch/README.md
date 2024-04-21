# Image Recognition with PyTorch

This repository contains a Python script `torchnn.py` that trains an image recognition model using PyTorch, saves the trained model, and uses the saved model to perform image recognition. 
The training part can be commented out after the first run to use the model for inference without retraining.

## Project Overview

The `torchnn.py` script includes:
- Model training and saving functionality.
- Loading the saved model.
- Performing image recognition using the loaded model.

## Getting Started

### Prerequisites

- Python 3.9
- PyTorch
- Other necessary Python libraries

You can install PyTorch from its [official site](https://pytorch.org/get-started/locally/).

### Setup

1. Install Dependencies:
To install PyTorch, follow the instructions on the PyTorch website tailored to your operating system and preferences (CPU or GPU, Conda or Pip).

## Usage
Run the Script:
run the script to train and save the model:

   ```bash
   python torchnn.py
  ```
This will create a file model_state.pt which contains the trained model.

2. Comment Out Training Code:
After the initial training, you can comment out the training part in torchnn.py to prevent retraining every time you run the script.

3. Image Recognition:
Run the script again to perform image recognition using the saved model
