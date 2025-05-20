import pandas as pd
import os

def load_data():
    # Adjust path to point to 'data/data'
    base_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'data')

    files = {
        'Benin': 'benin-malanville.csv',
        'Sierra Leone': 'sierraleone-bumbuna.csv',
        'Togo': 'togo-dapaong_qc.csv',
    }

    data = {}
    for country, filename in files.items():
        file_path = os.path.join(base_path, filename)
        try:
            df = pd.read_csv(file_path)
            df['Country'] = country
            data[country] = df
        except Exception as e:
            print(f"❌ Could not load {filename}: {e}")

    return data

def get_combined_dataframe(data_dict):
    if not data_dict:
        raise ValueError("❌ No data loaded. Check your file paths.")
    return pd.concat(data_dict.values(), ignore_index=True)
