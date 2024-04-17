import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from config import RAW_DATA_DIR, PROCESSED_DATA_DIR


def load_data():
    file_path = f"{RAW_DATA_DIR}/multidimensional_simulated_water_usage.csv"
    data = pd.read_csv(file_path, parse_dates=["Date"])
    data.set_index("Date", inplace=True)
    return data


def normalize_data(data):
    # Drop the 'Anomaly' column and normalize other features
    features = data.drop(columns="Anomaly")
    mean = features.mean()
    std = features.std()

    # Perform Z-score normalization
    normalized_features = (features - mean) / std

    # Return the normalized data and the 'Anomaly' column
    return (
        pd.DataFrame(normalized_features, index=data.index, columns=features.columns),
        data["Anomaly"],
    )


def split_data(features, labels):
    # Splitting the data into 80% training and 20% testing
    X_train, X_test, y_train, y_test = train_test_split(
        features, labels, test_size=0.2, random_state=42
    )
    return X_train, X_test, y_train, y_test


def save_data(X_train, X_test, y_train, y_test):
    X_train.to_csv(f"{PROCESSED_DATA_DIR}/X_train.csv")
    X_test.to_csv(f"{PROCESSED_DATA_DIR}/X_test.csv")
    y_train.to_csv(f"{PROCESSED_DATA_DIR}/y_train.csv")
    y_test.to_csv(f"{PROCESSED_DATA_DIR}/y_test.csv")


def preprocess():
    data = load_data()
    features, labels = normalize_data(data)
    X_train, X_test, y_train, y_test = split_data(features, labels)
    save_data(X_train, X_test, y_train, y_test)


if __name__ == "__main__":
    preprocess()
