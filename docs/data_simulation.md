# Data Simulation

This document outlines the process and methodology behind the data simulation for the Water Leak Detection Project. The corresponding Python script for this documentation can be found [here](../src/simulate_data.py).

## Overview

The `simulate_data.py` script is designed to generate simulated water usage data across multiple dimensions, representing different household water usage categories. This simulation includes normal daily usage and introduces anomalies to mimic real-world scenarios such as leaks or unusually high water usage.

## Usage Categories

The data simulation covers the following categories, which collectively add up to 100% of daily water usage:

- **Shower**: 25%
- **Dishwasher**: 15%
- **Laundry**: 20%
- **Kitchen**: 10%
- **Irrigation**: 18%
- **Car Wash**: 5%
- **Gardening**: 5%
- **Miscellaneous**: 2%

Each category is modeled with a normal distribution centered around a mean proportional to its percentage of total daily usage.

## Anomalies

Anomalies are introduced to the dataset to simulate days with potential leaks or faults. These are randomly generated for different categories on selected days, affecting between 150% to 300% of the typical daily usage. Approximately 2% of the days in the dataset feature anomalies, providing a realistic challenge for anomaly detection methods.

## Script Functions

- **simulate_data(days=365)**: Generates a DataFrame with a year's worth of simulated water usage data. The function handles both the creation of normal usage data and the introduction of anomalies.
- **save_data(data)**: Saves the generated DataFrame to a CSV file in the specified directory.

## Data Output

The script outputs a CSV file named `multidimensional_simulated_water_usage.csv`, containing the simulated daily usage for each category and an additional column marking anomaly days.

This simulated dataset forms the basis for further analysis, including data preprocessing, PCA, and anomaly detection using neural networks.

## Next Steps

Following data simulation, the next step involves preprocessing the data to standardize and normalize it, preparing it for PCA and subsequent neural network training.
