import pandas as pd


def read_csv_gdrive(url, separator):

    """
    Read csv kind files from google drive directory

    :param url: url to access csv file
    :param separator: separator to apply
    :return: dataframe
    """
    file_id = url.split('/')[-2]
    dwn_url = 'https://drive.google.com/uc?id=' + file_id
    df_csv_gdrive = pd.read_csv(
        dwn_url,
        # First line is header
        header=0,
        sep=separator
    )

    return df_csv_gdrive


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

