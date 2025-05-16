import pandas as pd

# Load the dataset from a CSV file.
def load_data(file_path):
    return pd.read_csv(file_path)

# Clean the dataset by removing duplicates and encoding categorical variables.
def clean_data(df):
    df.drop_duplicates(inplace=True)
    for column in df.select_dtypes(include=['object']).columns:
        unique_values = df[column].unique()
        mapping = {value: i for i, value in enumerate(unique_values)}
        df[column] = df[column].map(mapping)
    return df

# Save the cleaned dataset to a CSV file.
def save_data(df, file_path):
    df.to_csv(file_path, index=False)