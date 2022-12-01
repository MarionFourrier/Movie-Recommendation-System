# Axe => Movies per year

# Import libraries
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import seaborn as sns
import matplotlib.pyplot as plt
import sys

# Import modules
import clean_dataframe as clean
import functions_dashboard as fd

##########
# 1. Data_selection
##########

# A. Movies per year
# ----------

# get size of dataframe to be used
print(sys.getsizeof(clean.df_title_basics_clean))

# Retreive dataframe title basic from module clean dataframe
df_movies_year = clean.df_title_basics_clean.loc[clean.df_title_basics_clean["startYear"] != 0]

# # Create pivot table
# pt_movies_year = df_movies_year.pivot_table(values=["tconst"],
#                                 index="startYear",
#                                 # Indicate aggregation operation to apply per value through a dictionary
#                                 aggfunc={"tconst": np.sum})

# Group by year
# Index=False to keep grouped by field as a column and not a parameter
gb_movies_year = df_movies_year.groupby(
    by=["startYear"],
    as_index=False)\
    .agg(count_movies=("tconst", "count"))

# Sort per year (not necessary as already done in group by)
gb_movies_year.sort_values("startYear",
                           ascending=True,
                           inplace=True)

# Declare conversion parameter dictionary
convert_dict = {"startYear": str}

# Change Data type in dataframe based on conversion dictionary
gb_movies_year = gb_movies_year.astype(convert_dict)

# B. Average length per year
# ----------
# Delete movies with runtime at 0
df_movies_year_run = df_movies_year.loc[clean.df_title_basics_clean["runtimeMinutes"] != 0]

# Create a new column to get decade with pd.cut (new column is category type)
bins_decade = [1919, 1929, 1939, 1949, 1959, 1969, 1979, 1989, 1999, 2009, 2019, np.inf]
df_movies_year_run["decade"] = pd.cut(df_movies_year_run['startYear'], bins_decade)

# Group by decade with average length
# Index=False to keep grouped by field as a column and not a parameter
gb_movies_lenght = df_movies_year_run.groupby(
    by=["decade"],
    as_index=False)\
    .agg(average_length=("runtimeMinutes", "mean"))

# Rename the decade column
decade_list = ["1920-1929",
               "1930-1939",
               "1940-1949",
               "1950-1959",
               "1960-1969",
               "1970-1979",
               "1980-1989",
               "1990-1999",
               "2000-2009",
               "2010-2019",
               "2020-2022"]

gb_movies_lenght["decade"] = decade_list

# C. Average length per year and rating
# ----------
# Merge with title rating
# Keep only values in both dataframe with how='inner' parameter
df_movies_year_run_ratings = pd.merge(df_movies_year_run,
                                      clean.df_title_rating_clean,
                                      how='inner',
                                      on='tconst'
                                      )

# Describe distribution of numVotes columns
print(df_movies_year_run_ratings['numVotes'].describe())

# Select data only from 3rd quartile => 389 votes
df_movies_year_run_ratings = df_movies_year_run_ratings.loc[df_movies_year_run_ratings["numVotes"] >= 389]

# Create a new column to get rating category with pd.cut (new column is category type)
bins_rating = [0, 2.5, 5.0, 7.5, np.inf]
df_movies_year_run_ratings["ratingCategory"] = pd.cut(df_movies_year_run_ratings['averageRating'], bins_rating)

# Group by decade/ratingCategory with average length
# Index=False to keep grouped by field as a column and not a parameter
# Observed=True only shows observed values for categorical grouper => Avoid length differences between index and values
gb_movies_length_rating = df_movies_year_run_ratings.groupby(
    by=["decade", "ratingCategory"],
    observed=True,
    as_index=False)\
    .agg(average_length=("runtimeMinutes", "mean"))

# Rename the decade and ratingCategory columns
# Declare dictionary for conversion on decade
decade_dict = {"(1919.0, 1929.0]": "1920-1929",
               "(1929.0, 1939.0]": "1930-1939",
               "(1939.0, 1949.0]": "1940-1949",
               "(1949.0, 1959.0]": "1950-1959",
               "(1959.0, 1969.0]": "1960-1969",
               "(1969.0, 1979.0]": "1970-1979",
               "(1979.0, 1989.0]": "1980-1989",
               "(1989.0, 1999.0]": "1990-1999",
               "(1999.0, 2009.0]": "2000-2009",
               "(2009.0, 2019.0]": "2010-2019",
               "(2019.0, inf]": "2020-2022"}

# Replace decade category by dictionary values => convert type from categorical to string
gb_movies_length_rating.decade = gb_movies_length_rating.decade.astype(str).replace(decade_dict)

# Declare dictionary for conversion on ratingCategory
rating_dict = {"(0.0, 2.5]": "en-dessous de 2,5",
               "(2.5, 5.0]": "de 2,5 à 4,9",
               "(5.0, 7.5]": "de 5,0 à 7,4",
               "(7.5, inf]": "au-dessus de 7,5"}

# Map rating category by dictionary values => convert type from categorical to string
gb_movies_length_rating["ratingCategory"] = gb_movies_length_rating["ratingCategory"].astype(str).map(rating_dict)

##########
# 2. Charts
##########

# A. Number of movies per year
# ----------


def histogram_year():

    """
    No argument, return histogram with number of movies per year
    :return:
    """
    fig = px.histogram(
        gb_movies_year,
        x="startYear",
        y="count_movies",
        barmode="group",
        # Selection of aggregation function
        histfunc='sum',
        labels={"startYear": "Années",
                "sum of Films (k unité)": "test",
                "count_movies": "Films (k unité)"},
        title="Nombre de films par année")

    fig.update_xaxes(
        # Adjust x axis line parameters
        showline=True,
        linewidth=2,
        linecolor='darkblue'
    )

    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='darkblue'
    )

    fig.update_traces(
        # Adjust bar colors
        marker_color='darkblue'
    )

    fig.update_layout(
        # Adjust space between bar
        bargap=0.3,
        # Adjust x and Y positioning
        title_x=0.5,
        title_y=0.95,
        # Set backgroud color
        plot_bgcolor='rgb(255,255,255)',
        yaxis_title="Nombre de films"
    )

    return fig

# to include in main at consolidation stage
# fig_year = histogram_year()
# fig_year.show()

# B. Average length
# ----------


def average_length():
    """
    No argument, return chart with average film lenght through time
    :return:
    """
    fig = px.line(
        gb_movies_lenght,
        x="decade",
        y="average_length",
        range_y=[0, 140],
        markers=True,
        labels={"decade": "Années",
        "average_length": "durée (min)"},
        title="Evolution durée moyenne des films")

    fig.update_xaxes(
        # Adjust x axis line parameters
        showline=True,
        linewidth=2,
        linecolor='darkblue'
    )

    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='darkblue'
    )

    fig.update_traces(
        # Adjust line parameters
        marker_color='darkblue',
        marker_line_width=1.5)

    fig.update_layout(
        # Adjust x and Y positioning
        title_x=0.5,
        title_y=0.95,
        # Set backgroud color
        plot_bgcolor='rgb(255,255,255)'
    )

    return fig

# to include in main at consolidation stage
# fig_average_length = average_length()
# fig_average_length.show()

# C. Average length rating
# ----------


def average_length_rating():
    """
    No argument, return chart with average film length according to rating category through time
    :return:
    """
    fig = px.line(
        gb_movies_length_rating,
        x="decade",
        y="average_length",
        color='ratingCategory',
        range_y=[0, 140],
        markers=True,
        labels={"decade": "Années",
                "average_length": "Durée (min)",
                "ratingCategory": "Notation"
                },
        category_orders={"ratingCategory": ["au-dessus de 7,5",
                                            "de 5,0 à 7,4",
                                            "de 2,5 à 4,9",
                                            "en-dessous de 2,5"]},
        title="Durée moyenne des films en fonction de leur notation (25% les plus notés)")

    fig.update_xaxes(
        # Adjust x axis line parameters
        showline=True,
        linewidth=2,
        linecolor='darkblue'
    )

    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='darkblue'
    )

    fig.update_traces(
        # Adjust line parameters
        marker_line_width=0)

    fig.update_layout(
        # Adjust x and Y positioning
        title_x=0.5,
        title_y=0.95,
        # Change legend title
        legend_title_text="Notation moyenne",
        # Set backgroud color
        plot_bgcolor='rgb(255,255,255)'
    )

    return fig

# to include in main at consolidation stage
# fig_average_length_rating = average_length_rating()
# fig_average_length_rating.show()


# D. Top 10 rating
# ----------


def top_20_year(starting_year, ending_year, list_votes, list_genre):
    """
    Return the top 10 based on ratings
    :param starting_year: starting point of selection
    :param ending_year: ending point of selection
    :param list_votes: selection on number of votes
    :param list_genre: selection on genre
    :return: dataframe with 10 best rated movies on the period
    """
    # Keep only needed columns
    df_top_20 = df_movies_year_run_ratings.loc[:, ["tconst",
                                                   "startYear",
                                                   "runtimeMinutes",
                                                   "averageRating",
                                                   "numVotes"]]

    # Merge with title_akas to get french title
    df_top_20 = pd.merge(df_top_20,
                         clean.df_title_akas_clean,
                         how='inner',
                         left_on='tconst',
                         right_on='titleId')

    # Keep only line with a French title
    df_top_20 = df_top_20.loc[df_top_20["region"] == "FR"]

    # Merge with title genre clean
    df_top_20 = pd.merge(df_top_20,
                         clean.df_title_genre_clean,
                         how='inner',
                         on='tconst')

    # Filter on selected genre
    if len(list_genre) == 0:
        pass
    else:
        df_top_20 = df_top_20.loc[df_top_20["genres"].isin(list_genre)]

    # Drop duplicates
    df_top_20.drop_duplicates(subset=["tconst"],
                             inplace=True,
                             ignore_index=True)

    # Keep only needed columns
    df_top_20 = df_top_20.loc[:, ["title",
                                  "startYear",
                                  "runtimeMinutes",
                                  "averageRating",
                                  "numVotes"]]

    # Filter on selected years
    df_top_20 = df_top_20.loc[(df_top_20["startYear"] >= starting_year) &
                              (df_top_20["startYear"] <= ending_year)]

    # Filter based on number of votes selected by the user
    df_top_20 = df_top_20.loc[df_top_20["numVotes"].isin(list_votes)]

    # sort in descending order according to rating and number of vote in second
    df_top_20.sort_values(["averageRating", "numVotes"],
                          ascending=False,
                          inplace=True)

    # Keep only 20 first lines
    df_top_20 = df_top_20.iloc[:20]

    # Reset index and delete former one
    df_top_20.reset_index(inplace=True,
                          drop=True
                          )

    # Add one to the index to start from 1 instead of 0
    df_top_20.index += 1

    # Rename columns title
    df_top_20.rename(columns={"title": "Titre",
                              "startYear": "Année",
                              "runtimeMinutes": "Durée (min)",
                              "averageRating": "Note moyenne",
                              "numVotes": "Votes"},
                     inplace=True)

    return df_top_20

# to include in main at consolidation stage
# df_top_20_year = top_20_year(2000, 2022, [elem for elem in range(389, 2000000)])

# E. Scatter plot rating with number of votes
# ----------


def rate_numVote(starting_year, ending_year, list_votes, list_genre):
    """
    Return scatter plot of rates according to number of votes
    :param starting_year: starting point of selection
    :param ending_year: ending point of selection
    :param list_votes: selection on number of votes
    :param list_genre: selection on genre
    :return: scatter plot
    """

    # Merge with title genre clean
    df_rate_numVote = pd.merge(df_movies_year_run_ratings,
                               clean.df_title_genre_clean,
                               how='inner',
                               on='tconst')

    # Filter on selected genre
    if len(list_genre) == 0:
        pass
    else:
        df_rate_numVote = df_rate_numVote.loc[df_rate_numVote["genres"].isin(list_genre)]

    # Drop duplicates
    df_rate_numVote.drop_duplicates(subset=["tconst"],
                                    inplace=True,
                                    ignore_index=True)

    # Keep only needed columns
    df_rate_numVote = df_rate_numVote.loc[:, ["primaryTitle",
                                              "startYear",
                                              "averageRating",
                                              "numVotes"]]

    # Filter on selected years
    df_rate_numVote = df_rate_numVote.loc[(df_rate_numVote["startYear"] >= starting_year) &
                                          (df_rate_numVote["startYear"] <= ending_year)]

    # Filter based on number of votes selected by the user
    df_rate_numVote = df_rate_numVote.loc[df_rate_numVote["numVotes"].isin(list_votes)]

    fig = px.scatter(
        df_rate_numVote,
        x="averageRating",
        y="numVotes",
        labels={"averageRating": "Note",
                "numVotes": "Nombre de votes",
                "startYear": "Année"},
        title="Note par rapport au nombre de votes exprimés")

    fig.update_xaxes(
        # Adjust x axis line parameters
        showline=True,
        linewidth=2,
        linecolor='darkblue'
    )

    fig.update_yaxes(
        showgrid=True,
        gridwidth=1,
        gridcolor='darkblue'
    )

    fig.update_traces(
        # Adjust line parameters
        marker_color='darkblue')

    fig.update_layout(
        # Adjust x and Y positioning
        title_x=0.5,
        title_y=0.95,
        # Set backgroud color
        plot_bgcolor='rgb(255,255,255)'
    )

    return fig

# to include in main at consolidation stage
# fig_rate_Vote = rate_numVote(2000, 2020, [elem for elem in range (400,1000)])
# fig_rate_Vote.show()

