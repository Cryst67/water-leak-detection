# Neural Network Training

This document outlines the process and findings from the neural network training phase of the Water Leak Detection Project. The associated code can be found in the `train_nn.py` script within the project's `src` directory.

## Overview

A neural network was constructed and trained to identify anomalies in water usage data. The training process involved using PCA-reduced data to ensure the model could learn from the most significant features without unnecessary noise or redundancy.

## Training Process

The model was trained over 100 epochs with a batch size of 32. Early on, the accuracy was relatively low, but by epoch 34, the model achieved 100% accuracy on the training set. While high accuracy is typically the goal, this rapid attainment of perfect accuracy raised concerns about potential overfitting.

## Observations

- **Early High Accuracy**: The model's rapid convergence to 100% accuracy suggests it may be memorizing the training data rather than learning general patterns.
- **Simple Data**: The dataset used for training might be too simplistic, which can cause the model to easily overfit. Real-world data often contains more noise and complexity.

## Overfitting Concerns

Given the simplicity of the simulated data and the quick achievement of high accuracy, the model's ability to generalize to new, unseen data is uncertain. Overfitting is a common challenge when the model is too complex relative to the amount and diversity of the training data.

## Conclusion

The neural network training phase highlighted the importance of model evaluation beyond mere accuracy. Ensuring the model generalizes well to unseen data is critical for its success in a real-world setting. Future iterations of the project will focus on enhancing the dataset's complexity and implementing strategies to mitigate overfitting.

## Usage

To repeat the model training process, run the following command from the project root directory:

```bash
python src/train_nn.py
```

This script will train the model and save it to the models directory for subsequent evaluation and potential deployment.