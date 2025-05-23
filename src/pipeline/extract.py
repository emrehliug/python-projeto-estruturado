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
            raise FileNotFoundError(f"Diretorio {path} não existe.")

        get_filespath_in_dir = os.listdir(path)
        if(len(set(get_filespath_in_dir)) == 0):
            raise ValueError("O diretório não contém arquivos. Verifique se o diretório está vazio.")
        
        list_file_types = []
        
        for file in get_filespath_in_dir:
            list_file_types.append(file.split(".")[-1])

        distinct_file_types = set(list_file_types)
        
        # Cria uma lista para armazenar os dataframes
        df_list = []
        
        for file_type in distinct_file_types:
            if file_type not in ['csv', 'json', 'xlsx']:
                raise ValueError("O diretório contém arquivo do tipo invalido. Os tipos válidos são: csv, json e xlsx.")
            
            # Cria uma lista com os arquivos do diretório que possuem o tipo de arquivo desejado
            files = glob.glob(os.path.join(path, f"*.{file_type}"))

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
    path = r"C:\Users\gliminha\Desktop\Workspace\python-projeto-estruturado\data\input"
    
    df_list = extract(path)
    for df in df_list:
        print(df.head())