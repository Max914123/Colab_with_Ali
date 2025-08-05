# 📈 BTC Price Predictions

A collaborative Python project for predicting Bitcoin (BTC) prices using time series analysis and LSTM deep learning models. Designed for team collaboration, modular development, and extensibility.

---

## 🚀 Project Goals

- Preprocess historical BTC data
- Engineer features (lags, MAs, indicators)
- Train LSTM and baseline models
- Evaluate and visualize prediction performance
- Support collaboration via GitHub and Docker

---

## 🗂️ Folder Structure

```
time-series-project/
│
├── data/                   # Raw and processed data files
├── notebooks/              # Jupyter Notebooks (exploration & visualization)
├── src/                    # Source code modules
│   ├── preprocessing.py    # Data loading and feature engineering
│   ├── modeling.py         # Model training and prediction (LSTM, etc.)
│   └── evaluation.py       # Metrics and visualization
├── tests/                  # Unit tests
├── main.py                 # Main runner script
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker configuration
├── .gitignore              # Git ignored files
└── README.md               # Project documentation
```

---

## 👥 Team Collaboration

| Developer | Task Branch              | Responsibilities                       |
|-----------|--------------------------|----------------------------------------|
| You       | `feature/preprocessing`  | Data cleaning, feature engineering     |
| Mohammad  | `feature/modeling`       | Model training and prediction (LSTM)   |
| Mohammad  | `feature/evaluation`     | Evaluation metrics and plots           |

### 🧪 Workflow

```bash
# Create a new feature branch
git checkout -b feature/my-task

# Stage and commit changes
git add .
git commit -m "Add preprocessing step"

# Push to GitHub
git push origin feature/my-task

# Create a Pull Request into 'dev' branch
```

---

## ⚙️ Setup Instructions

### 📌 Option 1: Using Virtual Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # or .\venv\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt

# Run the pipeline
python main.py
```

### 📌 Option 2: Using Docker

```bash
# Build Docker image
docker build -t btc-predictor .

# Run container
docker run -p 5000:5000 btc-predictor
```

---

## 🔧 Requirements

- Python 3.8+
- TensorFlow / Keras
- Pandas / NumPy
- Scikit-learn
- Matplotlib / Seaborn

Install them via:

```bash
pip install -r requirements.txt
```

---

## 📊 UML Overview

> Project structure is based on the following UML class diagram:

![UML Diagram](docs/uml-btc-predict.png)  
*Note: You can generate this using PlantUML*

---

## 📈 Sample Features

- Lag features: `close_t-1`, `close_t-2`, ...
- Moving Averages: `MA_7`, `MA_30`
- Technical Indicators: `RSI`, `MACD`, etc.

---

## 📉 Evaluation Metrics

- RMSE (Root Mean Squared Error)
- MAE (Mean Absolute Error)
- MAPE (Mean Absolute Percentage Error)

---

## 🤝 License

MIT License – feel free to use, modify, and contribute.

---

## 👨‍💻 Authors

- **You** – Cybersecurity & ML Engineer  
- **Your Brother** – Optical/Photonics Engineer & Data Analyst

---
