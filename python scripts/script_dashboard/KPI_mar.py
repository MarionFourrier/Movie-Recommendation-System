# Axe 3 => Equipe de réalisation
# Responsible => Marion

# Import libraries
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Import modules
import functions_dashboard as fd
import clean_dataframe as clean


##########
# 1. Data_selection
##########

# A. Top 10 directors
# ----------

def top10_directors (starting_year, ending_year, list_votes) :
    """
    Return horizontal histogram with the top10 productors
    :param starting_year: starting point of selection
    :param ending_year: ending point of selection
    :param list_votes: selection on number of votes
    :return: dataframe with 10 productors in best rated movies
    """

    # Merge de table_title_ratings et table_title_basics
    df_title_basics_ratings = pd.merge(clean.df_title_basics_clean,
                                       clean.df_title_rating_clean,
                                       how='left',
                                       left_on='tconst',
                                       right_on='tconst')

    # Suppression des films sans note
    df_title_basics_ratings_clean = df_title_basics_ratings.loc[df_title_basics_ratings['averageRating'].isna() == False]

    # Garder que les titres entre les bornes starting_year et ending_year
    df_title_basics_ratings_clean = df_title_basics_ratings_clean[(df_title_basics_ratings_clean['startYear'] >= starting_year) &
                                                                  (df_title_basics_ratings_clean['startYear'] <= ending_year)]

    # Filter based on number of votes selected by the user
    df_title_basics_ratings_clean = df_title_basics_ratings_clean.loc[df_title_basics_ratings_clean['numVotes'].isin(list_votes)]

    # Merge de 'table_title_basics_ratings_clean' ET 'table_title_principals'
    df_title_basics_ratings_clean_principals = pd.merge (df_title_basics_ratings_clean,
                                                        clean.df_title_principals_clean,
                                                        how = 'left',
                                                        left_on = 'tconst',
                                                        right_on = 'tconst')

    # Supprimer les toutes lignes où category n'est pas 'director'
    df_title_basics_ratings_clean_principals_directors = df_title_basics_ratings_clean_principals[
        (df_title_basics_ratings_clean_principals['category'] == 'director')]

    # Réarrangement des colonnes
    df_title_basics_ratings_clean_principals_directors = df_title_basics_ratings_clean_principals_directors[['nconst',
                                                                                                             'category',
                                                                                                             'job',
                                                                                                             'tconst',
                                                                                                             'primaryTitle',
                                                                                                             'startYear',
                                                                                                             'averageRating',
                                                                                                             'numVotes']]

    # Merge de 'df_title_basics_ratings_clean_principals_directors' ET 'table_name_basics'
    df_title_basics_ratings_clean_principals_directors_nameBasics = pd.merge (df_title_basics_ratings_clean_principals_directors,
                                                                              clean.df_name_basics_clean,
                                                                              how='left',
                                                                              left_on='nconst',
                                                                              right_on='nconst')

    # Réarrangement des colonnes
    df_directors_by_ratings = df_title_basics_ratings_clean_principals_directors_nameBasics[['primaryName',
                                                                                          'primaryTitle',
                                                                                          'startYear',
                                                                                          'averageRating',
                                                                                          'numVotes']]

    df_directors_by_ratings_grouped = df_directors_by_ratings.groupby(['primaryName']).mean()
    df_directors_by_ratings_grouped = df_directors_by_ratings_grouped.reset_index()

    # Modification du type 'startYear' en int
    df_directors_by_ratings_grouped = df_directors_by_ratings_grouped.astype({'startYear': int})

    # Modification du type 'numVotes' en int
    df_directors_by_ratings_grouped = df_directors_by_ratings_grouped.astype({'numVotes': int})

    # sort in descending order according to rating and number of vote in second
    df_directors_by_ratings_grouped.sort_values(['averageRating', 'numVotes'],
                                                 ascending=False,
                                                 inplace=True)

    # Keep only 10 first lines
    df_just_directors = df_directors_by_ratings_grouped.iloc[:10]

    fig = px.bar(data_frame=df_just_directors,
                 y='primaryName',
                 x='averageRating',
                 labels={"primaryName": "Réalisateur",
                         'averageRating': "Note"},
                 title="Top 10 des réalisateurs",
                 text_auto=True,
                 color="averageRating",
                 color_continuous_scale=[(0, "blue"), (1, "darkblue")])

    fig.update_yaxes(categoryorder="total ascending")

    fig.update_traces(
        # Adjust bar colors
        # marker_color='darkblue',
        texttemplate="%{x:.2f}")

    fig.update_layout(
        # Adjust space between bar
        bargap=0.3,
        # Adjust x and y positioning
        title_x=0.5,
        title_y=0.95,
        # Set background color
        plot_bgcolor='rgb(255,255,255)',
        xaxis_title="Notes",
        yaxis_title="Réalisateurs"
    )

    return fig


# B. Top 10 writers
# ----------

def top10_writers (starting_year, ending_year, list_votes) :
    """
    Return horizontal histogram with the top10 writers
    :param starting_year: starting point of selection
    :param ending_year: ending point of selection
    :param list_votes: selection on number of votes
    :return: dataframe with 10 writers in best rated movies
    """

    # Merge de table_title_ratings et table_title_basics
    df_title_basics_ratings = pd.merge(clean.df_title_basics_clean,
                                       clean.df_title_rating_clean,
                                       how='left',
                                       left_on='tconst',
                                       right_on='tconst')

    # Suppression des films sans note
    df_title_basics_ratings_clean = df_title_basics_ratings.loc[df_title_basics_ratings['averageRating'].isna() == False]

    # Garder que les titres entre les bornes starting_year et ending_year
    df_title_basics_ratings_clean = df_title_basics_ratings_clean[(df_title_basics_ratings_clean['startYear'] >= starting_year) &
                                                                  (df_title_basics_ratings_clean['startYear'] <= ending_year)]

    # Filter based on number of votes selected by the user
    df_title_basics_ratings_clean = df_title_basics_ratings_clean.loc[df_title_basics_ratings_clean['numVotes'].isin(list_votes)]

    # Merge de 'table_title_basics_ratings_clean' ET 'table_title_principals'
    df_title_basics_ratings_clean_principals = pd.merge (df_title_basics_ratings_clean,
                                                        clean.df_title_principals_clean,
                                                        how = 'left',
                                                        left_on = 'tconst',
                                                        right_on = 'tconst')

    # Supprimer les toutes lignes où category n'est pas 'writer'
    df_title_basics_ratings_clean_principals_writers = df_title_basics_ratings_clean_principals[
        (df_title_basics_ratings_clean_principals['category'] == 'writer')]

    # Réarrangement des colonnes
    df_title_basics_ratings_clean_principals_writers = df_title_basics_ratings_clean_principals_writers[['nconst',
                                                                                                         'category',
                                                                                                         'job',
                                                                                                         'tconst',
                                                                                                         'primaryTitle',
                                                                                                         'startYear',
                                                                                                         'averageRating',
                                                                                                         'numVotes']]

    # Merge de 'df_title_basics_ratings_clean_principals_writers' ET 'table_name_basics'
    df_title_basics_ratings_clean_principals_writers_nameBasics = pd.merge (df_title_basics_ratings_clean_principals_writers,
                                                                              clean.df_name_basics_clean,
                                                                              how='left',
                                                                              left_on='nconst',
                                                                              right_on='nconst')

    # Réarrangement des colonnes
    df_writers_by_ratings = df_title_basics_ratings_clean_principals_writers_nameBasics[['primaryName',
                                                                                          'primaryTitle',
                                                                                          'startYear',
                                                                                          'averageRating',
                                                                                          'numVotes']]

    df_writers_by_ratings_grouped = df_writers_by_ratings.groupby(['primaryName']).mean()
    df_writers_by_ratings_grouped = df_writers_by_ratings_grouped.reset_index()

    # Modification du type 'startYear' en int
    df_writers_by_ratings_grouped = df_writers_by_ratings_grouped.astype({'startYear': int})

    # Modification du type 'numVotes' en int
    df_writers_by_ratings_grouped = df_writers_by_ratings_grouped.astype({'numVotes': int})

    # sort in descending order according to rating and number of vote in second
    df_writers_by_ratings_grouped.sort_values(['averageRating', 'numVotes'],
                                                 ascending=False,
                                                 inplace=True)

    # Keep only 10 first lines
    df_just_writers = df_writers_by_ratings_grouped.iloc[:10]

    fig = px.bar(data_frame=df_just_writers,
                 y='primaryName',
                 x='averageRating',
                 labels={"primaryName": "Scénariste",
                         'averageRating': "Note"},
                 title="Top 10 des scénaristes",
                 text_auto=True,
                 color="averageRating",
                 color_continuous_scale=[(0, "blue"), (1, "darkblue")])

    fig.update_yaxes(categoryorder="total ascending")

    fig.update_traces(
        # Adjust bar colors
        # marker_color='darkblue',
        texttemplate="%{x:.2f}")

    fig.update_layout(
        # Adjust space between bar
        bargap=0.3,
        # Adjust x and y positioning
        title_x=0.5,
        title_y=0.95,
        # Set background color
        plot_bgcolor='rgb(255,255,255)',
        xaxis_title="Notes",
        yaxis_title="Scénaristes"
    )

    return fig


# C. Top 10 composers
# ----------

def top10_composers (starting_year, ending_year, list_votes) :
    """
    Return horizontal histogram with the top10 compositors
    :param starting_year: starting point of selection
    :param ending_year: ending point of selection
    :param list_votes: selection on number of votes
    :return: dataframe with 10 compositors in best rated movies
    """

    # Merge de table_title_ratings et table_title_basics
    df_title_basics_ratings = pd.merge(clean.df_title_basics_clean,
                                       clean.df_title_rating_clean,
                                       how='left',
                                       left_on='tconst',
                                       right_on='tconst')

    # Suppression des films sans note
    df_title_basics_ratings_clean = df_title_basics_ratings.loc[df_title_basics_ratings['averageRating'].isna() == False]

    # Garder que les titres entre les bornes starting_year et ending_year
    df_title_basics_ratings_clean = df_title_basics_ratings_clean[(df_title_basics_ratings_clean['startYear'] >= starting_year) &
                                                                  (df_title_basics_ratings_clean['startYear'] <= ending_year)]

    # Filter based on number of votes selected by the user
    df_title_basics_ratings_clean = df_title_basics_ratings_clean.loc[df_title_basics_ratings_clean['numVotes'].isin(list_votes)]

    # Merge de 'table_title_basics_ratings_clean' ET 'table_title_principals'
    df_title_basics_ratings_clean_principals = pd.merge (df_title_basics_ratings_clean,
                                                        clean.df_title_principals_clean,
                                                        how = 'left',
                                                        left_on = 'tconst',
                                                        right_on = 'tconst')

    # Supprimer les toutes lignes où category n'est pas 'composer'
    df_title_basics_ratings_clean_principals_composers = df_title_basics_ratings_clean_principals[
        (df_title_basics_ratings_clean_principals['category'] == 'composer')]

    # Réarrangement des colonnes
    df_title_basics_ratings_clean_principals_composers = df_title_basics_ratings_clean_principals_composers[['nconst',
                                                                                                             'category',
                                                                                                             'job',
                                                                                                             'tconst',
                                                                                                             'primaryTitle',
                                                                                                             'startYear',
                                                                                                             'averageRating',
                                                                                                             'numVotes']]

    # Merge de 'df_title_basics_ratings_clean_principals_writers' ET 'table_name_basics'
    df_title_basics_ratings_clean_principals_composers_nameBasics = pd.merge (df_title_basics_ratings_clean_principals_composers,
                                                                              clean.df_name_basics_clean,
                                                                              how='left',
                                                                              left_on='nconst',
                                                                              right_on='nconst')

    # Réarrangement des colonnes
    df_composers_by_ratings = df_title_basics_ratings_clean_principals_composers_nameBasics[['primaryName',
                                                                                             'primaryTitle',
                                                                                             'startYear',
                                                                                             'averageRating',
                                                                                             'numVotes']]

    df_composers_by_ratings_grouped = df_composers_by_ratings.groupby(['primaryName']).mean()
    df_composers_by_ratings_grouped = df_composers_by_ratings_grouped.reset_index()

    # Modification du type 'startYear' en int
    df_composers_by_ratings_grouped = df_composers_by_ratings_grouped.astype({'startYear': int})

    # Modification du type 'numVotes' en int
    df_composers_by_ratings_grouped = df_composers_by_ratings_grouped.astype({'numVotes': int})

    # sort in descending order according to rating and number of vote in second
    df_composers_by_ratings_grouped.sort_values(['averageRating', 'numVotes'],
                                                 ascending=False,
                                                 inplace=True)

    # Keep only 10 first lines
    df_just_composers = df_composers_by_ratings_grouped.iloc[:10]

    fig = px.bar(data_frame=df_just_composers,
                 y='primaryName',
                 x='averageRating',
                 labels={"primaryName": "Compositeur",
                         'averageRating': "Note"},
                 title="Top 10 des compositeurs",
                 text_auto=True,
                 color="averageRating",
                 color_continuous_scale=[(0, "blue"), (1, "darkblue")])

    fig.update_yaxes(categoryorder="total ascending")

    fig.update_traces(
        # Adjust bar colors
        # marker_color='darkblue',
        texttemplate="%{x:.2f}")

    fig.update_layout(
        # Adjust space between bar
        bargap=0.3,
        # Adjust x and y positioning
        title_x=0.5,
        title_y=0.95,
        # Set background color
        plot_bgcolor='rgb(255,255,255)',
        xaxis_title="Notes",
        yaxis_title="Compositeurs"
    )

    return fig