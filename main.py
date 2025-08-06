import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from src.preprocessing import Preprocessing


def main():
    # Path to raw data CSV
    data_path = os.path.join('data', 'btcusd_1-min_data.csv')
    
    # Initialize preprocessing
    preprocessor = Preprocessing()

    print("Loading data...")
    df_raw = preprocessor.load_data(data_path)
    print(f"Raw data loaded: {df_raw.shape} rows")

    print("Cleaning data...")
    df_clean = preprocessor.clean_data(df_raw)
    print(f"Cleaned data: {df_clean.shape} rows")

    print("Creating features...")
    df_features = preprocessor.create_features(df_clean)
    print(f"Features created: {df_features.shape} rows")

    # Save the feature-engineered dataset for modeling
    output_path = os.path.join('data', 'btcusd_features.csv')
    df_features.to_csv(output_path, index=False)
    print(f"Feature-engineered data saved to {output_path}")

if __name__ == '__main__':
    main()
