import os

from pipeline.extract import extract_data
from pipeline.load import load_data
from pipeline.transform import transform_data


def main():
    # Define the file path for the Excel file
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path_input = os.path.join(BASE_DIR, 'data', 'input')
    file_path_output = os.path.join(BASE_DIR, 'data', 'output')

    # Extract data from the Excel file
    dataframe = extract_data(file_path_input)

    # Transform the extracted data
    transformed_data = transform_data(dataframe)

    # Load the transformed data into an Excel file
    load_data(file_path_output, transformed_data)


if __name__ == '__main__':
    main()
