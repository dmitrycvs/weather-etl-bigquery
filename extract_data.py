import os
import zipfile
import kaggle

DATASET_NAME = 'nelgiriyewithana/global-weather-repository'
SAVE_PATH = 'datasets'

KAGGLE_CONFIG_DIR = os.path.expanduser("~/.kaggle")
KAGGLE_JSON_PATH = os.path.join(KAGGLE_CONFIG_DIR, "kaggle.json")

if not os.path.exists(KAGGLE_JSON_PATH):
    raise FileNotFoundError('Kaggle API not found!')

os.makedirs(SAVE_PATH, exist_ok=True)
print(f"Downloading dataset: {DATASET_NAME}")
kaggle.api.dataset_download_files(DATASET_NAME, path=SAVE_PATH, unzip=False)

zip_files = [f for f in os.listdir(SAVE_PATH) if f.endswith(".zip")]
if not zip_files:
    raise FileNotFoundError("No ZIP file found in the dataset folder!")


zip_path = os.path.join(SAVE_PATH, zip_files[0])
extract_path = os.path.join(SAVE_PATH, "extracted")

os.makedirs(extract_path, exist_ok=True)
print(f"Extracting {zip_files[0]}...")
with zipfile.ZipFile(zip_path, "r") as zip_ref:
    zip_ref.extractall(extract_path)

print("Dataset downloaded and extracted successfully!")
