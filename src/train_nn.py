import pandas as pd
import tensorflow as tf
from config import PROCESSED_DATA_DIR, MODELS_DIR

models = tf.keras.models
layers = tf.keras.layers


def load_data():
    X_train = pd.read_csv(f"{PROCESSED_DATA_DIR}/X_train_pca.csv", index_col=0)
    X_test = pd.read_csv(f"{PROCESSED_DATA_DIR}/X_test_pca.csv", index_col=0)
    y_train = pd.read_csv(f"{PROCESSED_DATA_DIR}/y_train.csv", index_col=0)
    y_test = pd.read_csv(f"{PROCESSED_DATA_DIR}/y_test.csv", index_col=0)
    return X_train, X_test, y_train.squeeze(), y_test.squeeze()


def build_model(input_dim):
    model = models.Sequential()
    model.add(layers.Dense(10, activation="relu", input_shape=(input_dim,)))
    model.add(layers.Dense(8, activation="relu"))
    model.add(layers.Dense(1, activation="sigmoid"))
    model.compile(optimizer="adam", loss="binary_crossentropy", metrics=["accuracy"])
    return model


def train_model(model, X_train, y_train):
    history = model.fit(
        X_train, y_train, epochs=100, batch_size=32, validation_split=0.2
    )
    return history


def main():
    X_train, X_test, y_train, y_test = load_data()
    model = build_model(input_dim=X_train.shape[1])
    history = train_model(model, X_train, y_train)

    # Save the trained model
    model.save(f"{MODELS_DIR}/water_leak_detection_model.keras")

    # Optionally, plot training history or evaluate the model on the test set
    # ...


if __name__ == "__main__":
    main()
