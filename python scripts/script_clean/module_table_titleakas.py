# Import of the functions, libraries, modules
import functions_clean as fc
import module_table_titlebasics as mttb
import constant as ct


# Function that cleans the dataframe
def title_akas(link):

    """
    Clean-up of the table title_ratings
    :param link: link of the original dataframe
    :return: cleaned dataframe
    """

    # Read entire database using custom function from functions clean module
    title_akas = fc.read_database(link, '\t')

    # Select rows that are also in title_basics_clean
    title_akas_clean = title_akas.loc[title_akas['titleId'].isin(mttb.title_basics_clean['tconst'])]
    title_akas_clean.reset_index(inplace=True)
    title_akas_clean = title_akas_clean.drop(columns='index')

    # Keep only required columns
    title_akas_clean = title_akas_clean.drop(columns=['types', 'attributes', 'language'])

    return title_akas_clean


# Function's calling
title_akas_clean = title_akas(ct.link_title_akas)

# Export of the cleaned-up dataframe to a csv file
title_akas_clean.to_csv(f'{ct.directory_aurelien}title_akas_clean.csv',
                        sep=",",
                        index=False)
