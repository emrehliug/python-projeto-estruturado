import os

import pandas as pd


def load_data(file_path: str, dataframe: pd.DataFrame) -> None:
    """Metodo responsavel por carregar os dados em um excel no diretorio especifico.

    Args:
        file_path (str): caminho do arquivo excel a ser carregado.
        dataframe (pd.DataFrame): DataFrame que contem os dados carregados do excel.
    Returns: none
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f'The file {file_path} does not exist.')

    if dataframe.empty:
        raise ValueError('The loaded DataFrame is empty.')

    excel_path = os.path.join(file_path, 'consolidated_data.xlsx')

    # Save the DataFrame to an Excel file
    try:
        dataframe.to_excel(excel_path, index=False)
        print(f'Data successfully loaded to {file_path}')
    except Exception as e:
        raise RuntimeError(
            f'An error occurred while saving the DataFrame: {e}'
        )
