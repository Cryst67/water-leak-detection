import os
import numpy as np
import pandas as pd
from config import (
    RAW_DATA_DIR,
    AVERAGE_DAILY_USE,
    VARIABILITY,
    ANOMALY_FREQUENCY,
    ANOMALY_MULTIPLIER,
)


def simulate_data(days=365):
    # Define usage proportions for each category to sum to 100%
    categories = {
        "Shower": 0.25,
        "Dishwasher": 0.15,
        "Laundry": 0.20,
        "Kitchen": 0.10,
        "Irrigation": 0.18,
        "Car Wash": 0.05,
        "Gardening": 0.05,
        "Miscellaneous": 0.02,
    }

    # DataFrame to hold the data with an index for dates
    dates = pd.date_range(start="2024-01-01", periods=days)
    data = pd.DataFrame(index=dates)

    # Simulate normal usage for each category
    for category, proportion in categories.items():
        mean_usage = AVERAGE_DAILY_USE * proportion
        std_dev = mean_usage * VARIABILITY
        data[category] = np.random.normal(mean_usage, std_dev, days)

    # Introduce anomalies at a specified frequency
    num_anomalies = int(days * ANOMALY_FREQUENCY)
    anomaly_days = np.random.choice(days, num_anomalies, replace=False)
    data["Anomaly"] = 0  # Initialize anomaly column

    for day in anomaly_days:
        if (
            np.random.rand() < 0.5
        ):  # Random chance to alter each category on an anomaly day
            for category in categories:
                data.loc[data.index[day], category] *= np.random.uniform(
                    *ANOMALY_MULTIPLIER
                )
            data.loc[data.index[day], "Anomaly"] = (
                1  # Mark this day as having an anomaly
            )

    return data


def save_data(data):
    filename = "multidimensional_simulated_water_usage.csv"
    filepath = os.path.join(RAW_DATA_DIR, filename)
    data.to_csv(filepath)
    print(f"Data saved to {filepath}")


if __name__ == "__main__":
    data = simulate_data()
    save_data(data)
