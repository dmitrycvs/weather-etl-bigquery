import pandas as pd


def transform_data(df):
    df.drop_duplicates(inplace=True)
    df["last_updated"] = pd.to_datetime(df["last_updated"])

    return df

df = pd.read_csv("datasets/extracted/GlobalWeatherRepository.csv")
df = transform_data(df)
df.to_csv('datasets/GlobalWeatherRepository.csv', index=False)