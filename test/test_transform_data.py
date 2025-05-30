import pandas as pd

data = {'A': [1, 2, 3, 4, 5], 'B': [5, 4, 3, 2, 1], 'C': [10, 20, 30, 40, 50]}
data2 = {
    'A': [6, 7, 8, 9, 10],
    'B': [10, 9, 8, 7, 6],
    'C': [60, 70, 80, 90, 100],
}
data3 = {
    'A': [11, 12, 13, 14, 15],
    'B': [15, 14, 13, 12, 11],
    'C': [110, 120, 130, 140, 150],
}


def test_transform_data():
    from src.pipeline.transform import transform_data

    # Arrange
    arrange_of_dfs = [
        pd.DataFrame(data),
        pd.DataFrame(data2),
        pd.DataFrame(data3),
    ]

    # Act
    df_consolidate = transform_data(arrange_of_dfs)
    result = df_consolidate

    # Assert
    assert isinstance(result, pd.DataFrame), 'Result should be a DataFrame'
    assert len(result) > 1, 'Result should contain more than one row'


def test_transform_data_empty_list():
    from src.pipeline.transform import transform_data

    # Arrange
    arrange_of_dfs = []

    # Act
    result = transform_data(arrange_of_dfs)

    # Assert
    assert isinstance(
        result, pd.DataFrame
    ), 'Result should be a DataFrame even if input is empty'
    assert result.empty, 'Result should be empty for empty input'


def test_transform_data_single_dataframe():
    from src.pipeline.transform import transform_data

    # Arrange
    arrange_of_dfs = [pd.DataFrame(data)]

    # Act
    result = transform_data(arrange_of_dfs)

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert result.equals(
        pd.DataFrame(data)
    ), 'Result should be equal to the single input DataFrame'


def test_transform_data_with_nan():
    import numpy as np

    from src.pipeline.transform import transform_data

    # Arrange
    data_with_nan = {
        'A': [1, np.nan, 3],
        'B': [4, 5, np.nan],
        'C': [np.nan, 7, 8],
    }
    arrange_of_dfs = [pd.DataFrame(data), pd.DataFrame(data_with_nan)]

    # Act
    result = transform_data(arrange_of_dfs)

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert result.isnull().any().any(), 'Result should contain NaN values'


def test_transform_data_different_columns():
    from src.pipeline.transform import transform_data

    # Arrange
    data_diff = {'A': [1, 2], 'D': [9, 10]}
    arrange_of_dfs = [pd.DataFrame(data), pd.DataFrame(data_diff)]

    # Act
    result = transform_data(arrange_of_dfs)

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert (
        'D' in result.columns
    ), 'Result should contain all columns from all input DataFrames'
    assert (
        'B' in result.columns
    ), 'Result should contain all columns from all input DataFrames'
