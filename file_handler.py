import os
import pandas as pd

def list_csv_files(data_folder):
    """
    Recursively list all .csv files inside the given data folder,
    returning their relative paths.
    """
    csv_files = []

    for root, _, files in os.walk(data_folder):
        for file in files:
            if file.endswith(".csv"):
                relative_path = os.path.relpath(os.path.join(root, file), data_folder)
                csv_files.append(relative_path)

    return csv_files


def preview_csv(file_path, num_rows=5):
    """
    Loads and previews the first few rows of a CSV file.
    Primarily used for debugging or initial exploration.
    """
    try:
        df = pd.read_csv(file_path, nrows=num_rows)
        print(f"\nPreviewing: {file_path}")
        print("Columns:", list(df.columns))
        print("\nSample Data:")
        print(df.head())
    except Exception as e:
        print(f"Error loading {file_path}: {e}")
