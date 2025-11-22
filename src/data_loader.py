import pandas as pd
from pathlib import Path

def load_raw_data(filepath):
    """
    Loads raw data from a CSV file.
    
    Args:
        filepath (Path): Path to the CSV file.
    
    Returns:
        pd.DataFrame: Loaded data.
    """
    print(f"... Loading data from: {filepath}")
    return pd.read_csv(filepath)

def save_processed_data(df, filepath):
    """
    Saves the DataFrame to a CSV file without the index.
    
    Args:
        df (pd.DataFrame): Data to save.
        filepath (Path): Destination path.
    """
    # Create parent directory if it doesn't exist
    filepath.parent.mkdir(parents=True, exist_ok=True)
    
    # Save to CSV, index=False prevents writing row numbers
    df.to_csv(filepath, index=False)
    
    print(f"--> Success: Data saved to: {filepath}")