import sys
import os
import matplotlib.pyplot as plt



sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from src.preprocessing import Preprocessing

def plot_features(df):
    plt.figure(figsize=(15, 20))

    # 1. Close price + Moving Averages
    plt.subplot(4, 1, 1)
    plt.plot(df['Timestamp'], df['Close'], label='Close', color='black', linewidth=1)
    if 'MA_7h' in df.columns:
        plt.plot(df['Timestamp'], df['MA_7h'], label='MA 7h', color='blue', alpha=0.7)
    if 'MA_30h' in df.columns:
        plt.plot(df['Timestamp'], df['MA_30h'], label='MA 30h', color='red', alpha=0.7)
    plt.title('Close Price and Moving Averages')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    # 2. RSI
    plt.subplot(4, 1, 2)
    plt.plot(df['Timestamp'], df['RSI_14'], label='RSI 14', color='purple')
    plt.axhline(70, color='red', linestyle='--', alpha=0.5)
    plt.axhline(30, color='green', linestyle='--', alpha=0.5)
    plt.title('Relative Strength Index (RSI)')
    plt.xlabel('Time')
    plt.ylabel('RSI')
    plt.legend()
    plt.grid(True)

    # 3. MACD
    plt.subplot(4, 1, 3)
    plt.plot(df['Timestamp'], df['MACD'], label='MACD', color='orange')
    plt.plot(df['Timestamp'], df['MACD_signal'], label='Signal Line', color='blue')
    plt.bar(df['Timestamp'], df['MACD_diff'], label='MACD Diff', color='gray', alpha=0.4)
    plt.title('MACD Indicator')
    plt.xlabel('Time')
    plt.ylabel('MACD')
    plt.legend()
    plt.grid(True)

    # 4. Lagged Close Prices
    plt.subplot(4, 1, 4)
    plt.plot(df['Timestamp'], df['Close'], label='Close', color='black')
    if 'close_t-1' in df.columns:
        plt.plot(df['Timestamp'], df['close_t-1'], label='Close t-1', color='orange')
    if 'close_t-2' in df.columns:
        plt.plot(df['Timestamp'], df['close_t-2'], label='Close t-2', color='green')
    if 'close_t-3' in df.columns:
        plt.plot(df['Timestamp'], df['close_t-3'], label='Close t-3', color='purple')
    plt.title('Lagged Close Prices')
    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.show()



def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))  # directory of main.py
    data_path = os.path.join(base_dir, 'data', 'data.txt')  # absolute path
    
    # Use this absolute path when loading data
    preprocessor = Preprocessing()
    
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

    output_path = os.path.join('C:\\Users\\alimoham\\Documents\\GitLearning\\Colab_with_Ali\\Colab_with_Ali\\data', 'btcusd_features.csv')
    df_features.to_csv(output_path, index=False)
    print(f"Saved feature-engineered data to: {output_path}")
    plot_features(df_features)


if __name__ == '__main__':
    main()
