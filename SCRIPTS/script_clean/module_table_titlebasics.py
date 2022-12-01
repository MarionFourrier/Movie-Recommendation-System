import functions_clean as fc
import constant as ct

# 1. Cleaning function for title_basics


def title_basics(link):
    """
    Return cleaned title basics dataframe
    :param link: link to csv file
    :return: dataframe
    """

    # Read entire database using custom function from functions clean module
    df_title_basics = fc.read_database(link, "\t")

    # Keep only movies using custom function
    df_title_basics_temp = fc.line_selections(df_title_basics, "titleType", "movie")

    # Replace null values
    df_title_basics_temp.loc[df_title_basics_temp["runtimeMinutes"] == "\\N", "runtimeMinutes"] = 0
    df_title_basics_temp.loc[df_title_basics_temp["startYear"] == "\\N", "startYear"] = 0

    # Declare conversion parameter dictionary
    convert_dict = {"runtimeMinutes": int,
                    "startYear": int,
                    "isAdult": int
                    }

    # Change Data type in dataframe based on conversion dictionary
    df_title_basics_temp = df_title_basics_temp.astype(convert_dict)

    # Keep only movies using custom function
    df_title_basics_temp = fc.line_selections(df_title_basics_temp, "isAdult", 0)

    # keep only required columns
    df_title_basics_temp = fc.column_selections(df_title_basics_temp,
                                                ["tconst",
                                                 "primaryTitle",
                                                 "startYear",
                                                 "runtimeMinutes",
                                                 "genres"])

    # Selection based on runtime
    df_title_basics_temp = df_title_basics_temp.loc[
        (df_title_basics_temp["runtimeMinutes"] == 0) |
        (df_title_basics_temp["runtimeMinutes"] >= 40) &
        (df_title_basics_temp["runtimeMinutes"] <= 420)]

    # Selection based on startYear
    df_title_basics_temp = df_title_basics_temp.loc[
        (df_title_basics_temp["startYear"] == 0) |
        (df_title_basics_temp["startYear"] >= 1920) &
        (df_title_basics_temp["startYear"] <= 2022)]

    # Final clean dataframe title_basics_clean
    df_title_basics_clean = fc.column_selections(df_title_basics_temp,
                                                ["tconst",
                                                 "primaryTitle",
                                                 "startYear",
                                                 "runtimeMinutes"])

    # Title genre table creation and final version
    # Create a new table on genres with several entries per movie
    df_title_genre_clean = fc.column_selections(df_title_basics_temp,
                                                ["tconst",
                                                 "genres"])

    # Classify lines without entries as unknown
    df_title_genre_clean = df_title_genre_clean.replace("\\N", "Unknown")

    # Split genres column and display one genre per line (one movie can have several genres)
    # Transform genres as a list type (expand must be false otherwise create as many columns as line with max elements
    df_title_genre_clean["genres"] = df_title_genre_clean.genres.str.split(",", expand=False)
    df_title_genre_clean = df_title_genre_clean.explode(column="genres",
                                                        # To restart index
                                                        ignore_index=True)

    return df_title_basics_clean, df_title_genre_clean


# 2. Generate clean dataframe through function
title_basics_clean, title_genre_clean = title_basics(ct.link_title_basics)

# 3. Declare clean csv list
clean_csv_list = ['title_basics_clean',
                  'title_genre_clean'
                  ]

# 4. Loop to copy clean dataframe to CSV
for elem in clean_csv_list:
    eval(elem).to_csv(
        f"{ct.directory_aurelien}{elem}.csv",
        sep=",",
        index=False
    )
