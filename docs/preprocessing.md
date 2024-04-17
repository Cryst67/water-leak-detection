# Data Preprocessing Documentation

This document describes the preprocessing steps implemented in the `preprocess_data.py` script for the Water Leak Detection Project. The corresponding Python script can be found [here](../src/preprocess_data.py).

## Overview

The preprocessing script prepares the simulated water usage data for subsequent analysis and modeling. The key processes include normalizing the data and splitting it into training and test sets.

## Normalization

Normalization is crucial for ensuring that each feature contributes equally to the analysis, particularly important for PCA and machine learning models.

### Method

Z-score normalization (standardization) is used, where the mean of each feature is subtracted from the data points and then divided by the standard deviation:

\[ z = \frac{(x - \mu)}{\sigma} \]

Where:
- \( x \) is a data point.
- \( \mu \) is the mean of the feature.
- \( \sigma \) is the standard deviation of the feature.

This method ensures that each feature has zero mean and unit variance, facilitating more stable and fast convergence in machine learning algorithms.

## Data Splitting

The data is split into training and test datasets:

- **Training Data**: Used to train the machine learning models.
- **Test Data**: Used to evaluate the performance of the models and ensure that they generalize well to new, unseen data.

The split ratio is typically 80% for training and 20% for testing, ensuring a sufficient amount of data for training while also providing a robust set for evaluation.

## Saving Processed Data

The processed data is saved in CSV format to the `processed` directory, making it easily accessible for further steps in the project. This includes separate files for training features, training labels, test features, and test labels.

## Conclusion

This preprocessing script is a foundational step in the project pipeline, ensuring that the data is appropriately normalized and split, setting the stage for effective and accurate model training and evaluation.

## Usage

To run the preprocessing script, execute the following command from the project root directory:

```bash
python src/preprocess_data.py
```

This will process the raw data, split it into training and test sets, and save the processed data for further use.