import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from src.preprocessing import Preprocessing


def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(base_dir, 'data', 'btcusd_1-min_data.csv')

    preprocessor = Preprocessing()

    print("Loading data...")
    df_raw = preprocessor.load_data(data_path)

    print("Cleaning data...")
    df_clean = preprocessor.clean_data(df_raw)

    print("Creating features...")
    df_features = preprocessor.create_features(df_clean)

    # ✅ Ensure the output directory exists
    output_dir = os.path.join(base_dir, 'data')
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.join(output_dir, 'btcusd_features.csv')
    df_features.to_csv(output_path, index=False)
    print(f"Saved feature-engineered data to: {output_path}")
