# Axe 3 => Acteurs & Actrices
# Responsible => Alexandre

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

# A. Top 10 actors
# ----------

def top10_actors (starting_year, ending_year, list_votes) :
    """
    Return horizontal histogram with the top10 actors
    :param starting_year: starting point of selection
    :param ending_year: ending point of selection
    :param list_votes: selection on number of votes
    :return: dataframe with 10 actress in best rated movies
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

    # Supprimer les toutes lignes où category n'est pas 'actor'
    df_title_basics_ratings_clean_principals_actors = df_title_basics_ratings_clean_principals[
        (df_title_basics_ratings_clean_principals['category'] == 'actor')]

    # Réarrangement des colonnes
    df_title_basics_ratings_clean_principals_actors = df_title_basics_ratings_clean_principals_actors[['nconst',
                                                                                                       'category',
                                                                                                       'job',
                                                                                                       'tconst',
                                                                                                       'primaryTitle',
                                                                                                       'startYear',
                                                                                                       'averageRating',
                                                                                                       'numVotes']]

    # Merge de 'df_title_basics_ratings_clean_principals_actors_actress' ET 'table_name_basics'
    df_title_basics_ratings_clean_principals_actors_nameBasics = pd.merge (df_title_basics_ratings_clean_principals_actors,
                                                                           clean.df_name_basics_clean,
                                                                           how='left',
                                                                           left_on='nconst',
                                                                           right_on='nconst')

    # Réarrangement des colonnes
    df_actors_by_ratings = df_title_basics_ratings_clean_principals_actors_nameBasics[['primaryName',
                                                                                       'primaryTitle',
                                                                                       'startYear',
                                                                                       'averageRating',
                                                                                       'numVotes']]

    df_actors_by_ratings_grouped = df_actors_by_ratings.groupby(['primaryName']).mean()
    df_actors_by_ratings_grouped = df_actors_by_ratings_grouped.reset_index()

    # Modification du type 'startYear' en int
    df_actors_by_ratings_grouped = df_actors_by_ratings_grouped.astype({'startYear': int})

    # Modification du type 'numVotes' en int
    df_actors_by_ratings_grouped = df_actors_by_ratings_grouped.astype({'numVotes': int})

    # sort in descending order according to rating and number of vote in second
    df_actors_by_ratings_grouped.sort_values(['averageRating', 'numVotes'],
                                             ascending=False,
                                             inplace=True)

    # Keep only 10 first lines
    df_just_actors = df_actors_by_ratings_grouped.iloc[:10]

    fig = px.bar(data_frame=df_just_actors,
                 y='primaryName',
                 x='averageRating',
                 labels={"primaryName": "Acteur",
                         'averageRating': "Note"},
                 title="Top 10 des acteurs",
                 text_auto=True,
                 color="averageRating",
                 color_continuous_scale=[(0, "blue"), (1, "darkblue")])

    fig.update_traces(
        # Adjust bar colors
        # marker_color='darkblue',
        texttemplate="%{x:.2f}")

    fig.update_yaxes(categoryorder="total ascending")

    fig.update_layout(
        # Adjust space between bar
        bargap=0.3,
        # Adjust x and y positioning
        title_x=0.5,
        title_y=0.95,
        # Set background color
        plot_bgcolor='rgb(255,255,255)',
        xaxis_title="Notes",
        yaxis_title="Acteurs"
    )

    return fig


# B. Top 10 actress
# ----------

def top10_actress (starting_year, ending_year, list_votes) :
    """
    Return horizontal histogram with the top10 actress
    :param starting_year: starting point of selection
    :param ending_year: ending point of selection
    :param list_votes: selection on number of votes
    :return: dataframe with 10 actress in best rated movies
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

    # Supprimer les toutes lignes où category n'est pas 'actress'
    df_title_basics_ratings_clean_principals_actress = df_title_basics_ratings_clean_principals[
        (df_title_basics_ratings_clean_principals['category'] == 'actress')]

    # Réarrangement des colonnes
    df_title_basics_ratings_clean_principals_actress = df_title_basics_ratings_clean_principals_actress[
        ['nconst',
         'category',
         'job',
         'tconst',
         'primaryTitle',
         'startYear',
         'averageRating',
         'numVotes']]

    # Merge de 'df_title_basics_ratings_clean_principals_actress' ET 'table_name_basics'
    df_title_basics_ratings_clean_principals_actress_nameBasics = pd.merge (df_title_basics_ratings_clean_principals_actress,
                                                                                   clean.df_name_basics_clean,
                                                                                   how='left',
                                                                                   left_on='nconst',
                                                                                   right_on='nconst')

    # Réarrangement des colonnes
    df_actress_by_ratings = df_title_basics_ratings_clean_principals_actress_nameBasics[['primaryName',
                                                                                         'primaryTitle',
                                                                                         'startYear',
                                                                                         'averageRating',
                                                                                         'numVotes']]
############
    df_actress_by_ratings_grouped = df_actress_by_ratings.groupby(['primaryName']).mean()
    df_actress_by_ratings_grouped = df_actress_by_ratings_grouped.reset_index()


    # Modification du type 'startYear' en int
    df_actress_by_ratings_grouped = df_actress_by_ratings_grouped.astype({'startYear': int})

    # Modification du type 'numVotes' en int
    df_actress_by_ratings_grouped = df_actress_by_ratings_grouped.astype({'numVotes': int})

    # sort in descending order according to rating and number of vote in second
    df_actress_by_ratings_grouped.sort_values(['averageRating', 'numVotes'],
                                             ascending=False,
                                             inplace=True)

    # Keep only 10 first lines
    df_just_actress = df_actress_by_ratings_grouped.iloc[:10]

    fig = px.bar(data_frame=df_just_actress,
                 y='primaryName',
                 x='averageRating',
                 labels={"primaryName": "Actrices",
                         'averageRating': "Note"},
                 title="Top 10 des actrices",
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
        yaxis_title="Actrices"
    )

    return fig


# C. Proportion acteurs / actrices
# ------------

def proportion_act(starting_year, ending_year, list_votes):

    # Merge de table_title_ratings et table_title_basics
    df_title_basics_ratings = pd.merge(clean.df_title_basics_clean,
                                           clean.df_title_rating_clean,
                                           how='left',
                                           left_on='tconst',
                                           right_on='tconst')

    # Suppression des films sans note
    df_title_basics_ratings_clean = df_title_basics_ratings.loc[
        df_title_basics_ratings['averageRating'].isna() == False]

    # Garder que les titres entre les bornes starting_year et ending_year
    df_title_basics_ratings_clean = df_title_basics_ratings_clean[
            (df_title_basics_ratings_clean['startYear'] >= starting_year) &
            (df_title_basics_ratings_clean['startYear'] <= ending_year)]

    # Filter based on number of votes selected by the user
    df_title_basics_ratings_clean = df_title_basics_ratings_clean.loc[
            df_title_basics_ratings_clean['numVotes'].isin(list_votes)]

    # Merge de 'table_title_basics_ratings_clean' ET 'table_title_principals'
    df_title_basics_ratings_clean_principals = pd.merge(df_title_basics_ratings_clean,
                                                            clean.df_title_principals_clean,
                                                            how='left',
                                                            left_on='tconst',
                                                            right_on='tconst')

    # Supprimer les toutes lignes où category n'est pas 'actors' ou 'actress'
    df_title_basics_ratings_clean_principals_prop = df_title_basics_ratings_clean_principals[
            (df_title_basics_ratings_clean_principals['category'] == 'actor') |
            (df_title_basics_ratings_clean_principals['category'] == 'actress')]

    # Réarrangement des colonnes
    df_title_basics_ratings_clean_principals_prop = df_title_basics_ratings_clean_principals_prop[
            ['nconst',
             'category',
             'tconst',
             'startYear',
             'averageRating',
             'numVotes']]

    # Merge de 'df_title_basics_ratings_clean_principals_actress' ET 'table_name_basics'
    df_title_basics_ratings_clean_principals_prop_nameBasics = pd.merge(
            df_title_basics_ratings_clean_principals_prop,
            clean.df_name_basics_clean,
            how='left',
            left_on='nconst',
            right_on='nconst')

    # Réarrangement des colonnes
    df_prop_by_ratings = df_title_basics_ratings_clean_principals_prop_nameBasics[['primaryName',
                                                                                       'category',
                                                                                       'tconst',
                                                                                       'startYear',
                                                                                       'averageRating',
                                                                                       'numVotes']]

    # Modification du type 'startYear' en int
    df_prop_by_ratings_clean = df_prop_by_ratings.astype({'startYear': int})

    # Modification du type 'numVotes' en int
    df_prop_by_ratings_clean = df_prop_by_ratings.astype({'numVotes': int})

    fig = px.pie(data_frame = df_prop_by_ratings_clean,
                 values = df_prop_by_ratings['category'].value_counts (),
                 names = df_prop_by_ratings['category'].value_counts ().index,
                 title = "Proportion acteurs / actrices",
                 labels={'actor': 'Acteurs',
                         'actress': 'Actrices'})

    fig.update_traces(
        textposition='inside',
        textinfo='percent+label',
        showlegend=False,
        textfont_size=15,
        marker=dict(colors=['darkblue', 'pink'],
                    line=dict(color='#000000', width=1)))

    fig.update_layout(
        title_x=0.5,
    )

    return fig
