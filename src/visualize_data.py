import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from config import RAW_DATA_DIR, ASSETS_DIR


def plot_heatmap(data, filename):
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(
        data.transpose(), cmap="viridis", cbar_kws={"label": "Water Usage (liters)"}
    )
    plt.title("Heatmap of Daily Water Usage by Category")
    plt.xlabel("Date")
    plt.ylabel("Categories")

    # Manually set the x-ticks and x-tick labels to only the first day of each month
    ax.set_xticks([i for i in range(len(data.index)) if data.index[i].day == 1])
    ax.set_xticklabels(
        [date.strftime("%Y-%m-%d") for date in data.index if date.day == 1]
    )
    plt.xticks(rotation=45)  # Rotate x-tick labels to prevent overlap

    plt.tight_layout()
    plt.savefig(f"{ASSETS_DIR}/{filename}")
    plt.close()  # Close the figure after saving to free up memory


def load_data(file_path):
    data = pd.read_csv(file_path, index_col="Date", parse_dates=["Date"])
    return data


def visualize():
    data = load_data(f"{RAW_DATA_DIR}/multidimensional_simulated_water_usage.csv")
    plot_heatmap(data, "heatmap_daily_water_usage.png")


if __name__ == "__main__":
    visualize()
