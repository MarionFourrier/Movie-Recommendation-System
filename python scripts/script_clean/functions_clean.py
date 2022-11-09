import pandas as pd


def read_database(link, separator):

    """
    Read csv kind files according to the link and separator

    :param link: link to access csv file
    :param separator: separator to apply
    :return: dataframe
    """
    df_csv = pd.read_csv(
        link,
        # First line is header
        header=0,
        sep=separator
    )

    return df_csv


def line_selections(df, column, criteria):

    """
    Return filtered dataframe according to a criteria on a given column

    :param df: dataframe to filter
    :param column: column on which to apply filter
    :param criteria: selection criteria
    :return: dataframe
    """
    df_filter = df.loc[df[column] == criteria]

    return df_filter


def column_selections(df, column_list: list):

    """
    Select columns from a dataframe

    :param df: dataframe to slice
    :param column_list: Columns to keep as a list
    :return: dataframe
    """
    df_slice = df.loc[:, column_list]

    return df_slice


def clean_rows(df_to_clean, df_reference, column):

    """
    Sélectionne lignes du df_to_clean en fonction d'une column dans df_de_reference.
    :param df_to_clean: dataframe to filter
    :param df_reference: dataframe used as a reference
    :param column: column on which to take values and operate filtering
    (must be present with same name in both dataframe)
    :return: df_clean (dataframe)
    """
    df_clean = df_to_clean.loc[df_to_clean[column].isin(df_reference[column])]
    df_clean.reset_index(inplace=True)
    df_clean = df_clean.drop(columns='index')

    return df_clean

