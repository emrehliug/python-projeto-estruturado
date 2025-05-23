import os 
import glob
import pandas as pd

from typing import List



def extract(path: str) -> List[pd.DataFrame]:
    """
    Função para extrarir os arquivos de um diretório
    e enviar para um dataframe
    Args:
        path (str): caminho do diretório
    Returns:
        df (DataFrame): dataframe com os dados extraídos
    """
    try:
        # Verifica se o diretório existe
        if not os.path.exists(path):
            raise FileNotFoundError(f"Directory {path} does not exist.")

        # Verifica se o tipo de arquivo é válido
        if file_type not in ['csv', 'json', 'xlsx']:
            raise ValueError("file_type must be 'csv' or 'json'")

        # Define o tipo de arquivo
        file_type = os.path.splitext(path)[1]

        # Cria uma lista com os arquivos do diretório
        files = glob.glob(os.path.join(path, f"*.{file_type}"))

        # Cria uma lista para armazenar os dataframes
        df_list = []

        # Loop para ler os arquivos e enviar para o dataframe
        for file in files:
            if file_type == 'csv':
                df = pd.read_csv(file)
            elif file_type == 'json':
                df = pd.read_json(file)
            elif file_type == 'xlsx':
                df = pd.read_excel(file)
            df_list.append(df)

        return df_list
    
    except Exception as e:
        raise Exception(f"Erro na extração de arquivos, msg exeception: {e}")


if __name__ == "__main__":
    # Testa a função
    path = "../data/input/"
    df_list = extract(path)
    for df in df_list:
        print(df.head())