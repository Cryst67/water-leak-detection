import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from config import PROCESSED_DATA_DIR, ASSETS_DIR


def load_data():
    X_train = pd.read_csv(f"{PROCESSED_DATA_DIR}/X_train.csv", index_col=0)
    X_test = pd.read_csv(f"{PROCESSED_DATA_DIR}/X_test.csv", index_col=0)
    return X_train, X_test


def apply_pca(X_train, n_components=None):
    if n_components is None:
        pca = PCA(0.95)  # retain 95% of variance
    else:
        pca = PCA(n_components=n_components)
    X_train_pca = pca.fit_transform(X_train)
    return pca, X_train_pca


def plot_explained_variance(pca, save_path):
    plt.figure(figsize=(8, 4))
    plt.plot(np.cumsum(pca.explained_variance_ratio_))
    plt.xlabel("Number of Components")
    plt.ylabel("Cumulative Explained Variance")
    plt.title("Explained Variance by PCA Components")
    plt.grid(True)
    plt.savefig(save_path)  # Save the figure to the specified path
    plt.show()


def main():
    X_train, X_test = load_data()
    pca, X_train_pca = apply_pca(X_train)
    plot_explained_variance(pca, f"{ASSETS_DIR}/cumulative_explained_variance.png")
    # You might also want to transform X_test and save both transformed datasets:
    X_test_pca = pca.transform(X_test)
    pd.DataFrame(X_train_pca).to_csv(f"{PROCESSED_DATA_DIR}/X_train_pca.csv")
    pd.DataFrame(X_test_pca).to_csv(f"{PROCESSED_DATA_DIR}/X_test_pca.csv")


if __name__ == "__main__":
    main()
