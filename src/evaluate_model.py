import tensorflow as tf
import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    roc_auc_score,
    roc_curve,
)

load_model = tf.keras.models.load_model

import matplotlib.pyplot as plt
from config import PROCESSED_DATA_DIR, MODELS_DIR


def load_data():
    X_test = pd.read_csv(f"{PROCESSED_DATA_DIR}/X_test_pca.csv", index_col=0)
    y_test = pd.read_csv(
        f"{PROCESSED_DATA_DIR}/y_test.csv", index_col=0
    ).squeeze()  # ensure y_test is a Series
    return X_test, y_test


def evaluate_model(model, X_test, y_test):
    # Make predictions
    y_pred_prob = model.predict(X_test).ravel()  # Ensure it's flattened
    y_pred = (y_pred_prob > 0.5).astype(int)  # Adjust threshold as necessary

    # Safe check for metrics calculation
    if len(np.unique(y_test)) > 1:  # Ensure there are at least two classes present
        roc_auc = roc_auc_score(y_test, y_pred_prob)
        print(f"ROC AUC: {roc_auc}")
    else:
        print("ROC AUC not defined with one class present in y_test.")

    # Calculate other metrics safely
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, zero_division=0)
    recall = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    print(f"Accuracy: {accuracy}")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")
    print(f"F1 Score: {f1}")

    return y_pred_prob, y_pred


def plot_confusion_matrix(
    y_test, y_pred, labels=[0, 1], file_path="assets/confusion_matrix.png"
):
    cm = confusion_matrix(y_test, y_pred, labels=labels)
    fig, ax = plt.subplots()
    im = ax.imshow(cm, interpolation="nearest", cmap="Blues")
    ax.figure.colorbar(im, ax=ax)
    # We want to show all ticks...
    ax.set(
        xticks=np.arange(cm.shape[1]),
        yticks=np.arange(cm.shape[0]),
        # ... and label them with the respective list entries
        xticklabels=labels,
        yticklabels=labels,
        title="Confusion Matrix",
        ylabel="True label",
        xlabel="Predicted label",
    )

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    fmt = ".2f" if cm.dtype == "float" else "d"
    thresh = cm.max() / 2.0
    for i in range(cm.shape[0]):
        for j in range(cm.shape[1]):
            ax.text(
                j,
                i,
                format(cm[i, j], fmt),
                ha="center",
                va="center",
                color="white" if cm[i, j] > thresh else "black",
            )
    fig.tight_layout()
    plt.savefig(file_path)
    plt.show()


def plot_roc_curve(y_test, y_pred_prob, file_path="assets/roc_curve.png"):
    fpr, tpr, _ = roc_curve(y_test, y_pred_prob)
    plt.plot(
        fpr,
        tpr,
        color="darkorange",
        label=f"ROC curve (area = {roc_auc_score(y_test, y_pred_prob):.2f})",
    )
    plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
    plt.xlabel("False Positive Rate")
    plt.ylabel("True Positive Rate")
    plt.title("Receiver Operating Characteristic (ROC) Curve")
    plt.legend()
    plt.savefig(file_path)
    plt.show()


def main():
    X_test, y_test = load_data()
    model = load_model(f"{MODELS_DIR}/water_leak_detection_model.keras")
    y_pred_prob, y_pred = evaluate_model(model, X_test, y_test)
    plot_confusion_matrix(y_test, y_pred)
    plot_roc_curve(y_test, y_pred_prob)


if __name__ == "__main__":
    main()
