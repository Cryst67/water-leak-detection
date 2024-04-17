# config.py
import os

# Base directory for data storage
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
MODELS_DIR = os.path.join(BASE_DIR, "models")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")

# Parameters for data simulation
AVERAGE_DAILY_USE = 300  # average water usage in liters
VARIABILITY = 0.1  # standard deviation as a fraction of average use
ANOMALY_FREQUENCY = 0.02  # fraction of days that have anomalies
ANOMALY_MULTIPLIER = (1.5, 3)  # range of multipliers for anomalies
