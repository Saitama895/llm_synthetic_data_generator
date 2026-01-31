import os
import json
import pandas as pd

# Function's to save data as JSON and CSV files

def save_json(data, file_path):
    """
    Save Dataset to a JSON file
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def save_csv(data, file_path):
    """
    Save Dataset to a CSV file
    """
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False, encoding="utf8")