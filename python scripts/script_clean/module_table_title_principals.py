import functions_clean as fc
import module_table_titlebasics as mttb
import constant as ct


def title_principals(link):

    """
    Cleaning of the title_principals table

    :param link: link of the title_principals table
    :return: dataframe title_principals cleaned
    """

    # Load of title_principals table in a DF, which is df_to_clean
    df_title_principals = fc.read_database(link, "\t")

    # Apply of clean_rows function
    df_title_principals_clean = fc.clean_rows(df_title_principals, mttb.title_basics_clean, 'tconst')

    # Drop of superfluous columns from title_principals_clean
    df_title_principals_clean.drop('ordering', axis=1, inplace=True)
    df_title_principals_clean.drop('job', axis=1, inplace=True)

    # Reset index and drop of old index
    df_title_principals_clean.reset_index(inplace=True)
    df_title_principals_clean.drop('index', axis=1, inplace=True)

    return df_title_principals_clean

# Function's cleaning title principals calling
df_title_principals_clean = title_principals(ct.link_title_principals)

# Export csv file from df_title_principals_clean
df_title_principals_clean.to_csv (f"{ct.directory_aurelien}title_principals_clean.csv", sep = ",", index = False)