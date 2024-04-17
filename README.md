# Water Leak Detection Project with PCA and Neural Networks

## Project Overview
In an effort to advance the capabilities of Internet of Things (IoT) systems in water leak detection, this project applies Principal Component Analysis (PCA) and Neural Networks (NNs) to simulated water flow data. The methodology is inspired by techniques used in financial time series analysis and adapted for residential water usage patterns. This project is developed for CSC-592: `Topics: Internet of Things`.

## Features
- Multidimensional data simulation for realistic water usage patterns.
- PCA for feature extraction and dimensionality reduction.
- Neural Network models for anomaly detection.
- Data preprocessing and transformation workflows.
- Analysis and visualization tools for interpreting PCA and NN results.

## Data Sources and Methodology

Simulated water usage data is modeled after statistics from the United States Environmental Protection Agency (EPA) regarding average family water use, adjusted for individual usage patterns. Special consideration is given to incorporating variability and anomalies that emulate realistic scenarios, such as leaks or conservation efforts. The paper "Anomaly Detection in Financial Time Series by PCA and NNs" provides the foundational techniques adapted for this project.

For detailed EPA statistics on water usage, visit [EPA - How We Use Water](https://www.epa.gov/watersense/how-we-use-water).

## Directory Structure
- `src/`: Contains all source scripts for the project stages, from data simulation to neural network implementation.
- `data/`: Holds the raw and processed data, including the simulated datasets and PCA-transformed files.
- `models/`: Stores the trained neural network models.
- `notebooks/`: Jupyter notebooks for exploratory data analysis and model evaluation.
- `docs/`: Documentation on the project's methodology, setup, and usage instructions.
- `assets/`: Generated plots and figures for visualization purposes.

## Getting Started

### Prerequisites
Ensure you have Python 3.x installed and the following packages:

```bash
pip install -r requirements.txt
```

### Running the Project
To simulate data, run:

```bash
python src/simulate_data.py
```

Follow the individual scripts in `src/` sequentially for preprocessing, PCA, NN training, and evaluation

## Future Work
- Explore the integration of LSTM networks for sequence prediction and anomaly detection.
- Evaluate cloud-based deployment for scalability and real-time data processing.
- Develop a user-friendly dashboard for real-time monitoring and alerts.

## Contributing
We welcome contributions to enhance the project's functionality and accuracy. Please submit pull requests for review.

## License
This project is open-sourced under the MIT License.

## Acknowledgements
Inspiration for this project's analytical techniques is drawn from the paper [Anomaly Detection in Financial Time Series by PCA and NNs](https://www.mdpi.com/1999-4893/15/10/385).