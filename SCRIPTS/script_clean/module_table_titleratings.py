# Import of the functions, libraries, modules
import functions_clean as fc
import pandas as pd
import module_table_titlebasics as mttb
import constant as c

# Import of the dataframe
link_title_ratings = 'https://datasets.imdbws.com/title.ratings.tsv.gz'

# Fonction that cleans the dataframe
def title_ratings(link):

    """
    Clean-up of the table title_ratings
    :param link: link of the original dataframe
    :return: cleaned dataframe
    """

    # Read entire database using custom function from functions clean module
    title_ratings = fc.read_database(link, '\t')

    # Select rows that are also in title_basics_clean
    title_ratings_clean = fc.clean_rows(title_ratings, mttb.title_basics_clean, 'tconst')

    # Return the cleaned up dataframe
    return title_ratings_clean

# Function's calling
title_ratings_clean = title_ratings(link_title_ratings)

# Export of the cleaned-up dataframe to a csv file
title_ratings_clean.to_csv(f'{c.directory_aurelien}title_ratings_clean.csv',
                           sep=",",
                           index=False)


