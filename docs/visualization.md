# Visualization

This document provides an overview of the visualization process for the Water Leak Detection Project. The corresponding Python script for this documentation can be found [here](../src/visualize_data.py).

## Overview

The `visualize_data.py` script is designed to generate visual representations of the simulated water usage data across multiple dimensions. These visualizations are crucial for understanding the distribution of water usage, identifying patterns, and detecting anomalies.

## Heatmap Visualization

The primary visualization provided by this script is a heatmap, which offers a color-coded view of water usage across various categories over time.

### Purpose

- **Identify Patterns**: The heatmap allows us to see patterns of usage across different days and categories at a glance.
- **Spot Anomalies**: By observing irregularities in the heatmap, such as unexpectedly high or low usage on certain days, we can identify potential anomalies.

### Implementation

The heatmap is generated using the Seaborn library, which is built on top of Matplotlib. It provides a high-level interface for drawing attractive and informative statistical graphics.

### Usage

To generate the heatmap, the script reads the multidimensional water usage data from a CSV file, transposes the data frame so that each category of usage becomes a row, and each row represents a day. The `sns.heatmap` function is then used to create the heatmap:

```python
sns.heatmap(data.transpose(), cmap="viridis", cbar_kws={"label": "Water Usage (liters)"})
```

### Features
- Color Map: The 'viridis' colormap is used, which offers excellent perceptibility of changes and is printer-friendly.
- Interactivity: Users can customize the appearance of the heatmap by adjusting the colormap, scaling, and other parameters within the script.

### File Output
The generated heatmap is saved as an image file in the assets directory. This file can be used in reports, presentations, or further analysis.

```python
plt.savefig(f"{ASSETS_DIR}/heatmap_daily_water_usage.png")
```