import pandas as pd

def process_data(data: pd.DataFrame, option: str) -> pd.DataFrame:
    if option != "All":
        data = data.loc[data['Sensor'] == option]
    return data

def transform_data(data: pd.DataFrame) -> pd.DataFrame:
    value_transformation = {
        "Temperature": lambda x: x + 273.15,
        "Humidity": lambda x: x / 100,
        "CO2": lambda x: x + 23
    }
    processed_data = []
    for _, row in data.iterrows():
        row['Value'] = value_transformation[row['Sensor']](row['Value'])
        processed_data.append(row)
    return pd.DataFrame(data=processed_data)
