# Axe => Genre

# Import libraries
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Import modules
import functions_dashboard as fd
import clean_dataframe as clean
import pandas as pd
import clean_dataframe

def function_KPI_moh():
    df_title_genre_clean_kpi = clean.df_title_genre_clean
    df = pd.DataFrame( df_title_genre_clean_kpi )
    # Ecploration of the table

    df_groupe_genre = df.groupby( 'genres' ).count

    df_title_genre_clean_kpi.drop_duplicates()
    # Create table with group of kinds of films
    df_kind = df_title_genre_clean_kpi.groupby( by = 'genres' , axis = 0 ).count()

    # drop Unknown category

    df_drop_Unknown = df_title_genre_clean_kpi[df_title_genre_clean_kpi['genres'].str.contains( 'Unknown' ) == False]
    # final table : df_kind_clean represente  number of film by category
    df_kind_clean = df_drop_Unknown.groupby( by = 'genres' , axis = 0 ).count()

    df_kind_clean_rest_index = df_kind_clean.reset_index( drop = False ).sort_values( by = 'tconst' )  ###
    ####################################################################



    title_principal_clean = clean.df_title_basics_clean

    # creat a merge between title principal and title genre:
    princial_genre = title_principal_clean.merge( df_title_genre_clean_kpi , left_on = 'tconst' , right_on = 'tconst' ,
                                                  how = 'right' )


    #######################

    ###durée de films par années

    ###drop value =0
    film_per_years = princial_genre.groupby( by = 'startYear' ).mean()


    #############################################
    ###durées des film par genre
    #drop 'unknouw' values
    index_nul_drop = princial_genre[princial_genre['runtimeMinutes'] == 0].index

    princial_genre.drop( index_nul_drop , inplace = True )
    princial_genre= princial_genre[princial_genre['genres'].str.contains( 'Unknown' ) == False]
    film_duree = princial_genre.groupby( 'genres' ).mean().sort_values( by = 'runtimeMinutes' )
    film_par_durée=film_duree.sort_values( by = 'runtimeMinutes' )

    ########################################              ##

    ######################### Genres les mieux notés###############################################

    # download df_ratinf

    df_ratings = clean.df_title_rating_clean

    princial_genre_rating = princial_genre.merge( df_ratings , left_on = 'tconst' , right_on = 'tconst' ,
                                                  how = 'right' )

    value_isnull_merge = princial_genre_rating.isnull()
    value_isnull_merge
    value_isnull_merge[value_isnull_merge['genres'] == True]


    ############################    drop NaN          ################

    princial_genre_rating_2 = princial_genre_rating.dropna( inplace = False )
    princial_genre_rating_2.isnull().sum()
    princial_genre_rating_2.reset_index( inplace = True )
    princial_genre_rating_2.groupby( by = 'genres' ).mean()[['averageRating' , 'numVotes']].sort_values(
        'averageRating' , ascending = False )
    genre_mieux_noter = princial_genre_rating_2.groupby( by = 'genres' ).mean()[
        ['averageRating' , 'numVotes']].sort_values( 'averageRating' , ascending = False )
    ###########################bests films by category#########################
    genre_mieux_noter2 = princial_genre_rating_2
    #########section test code#########################################

    ##########################


    return   df_kind_clean_rest_index,genre_mieux_noter,film_par_durée, princial_genre_rating_2

film_par_types,genre_mieux_noter,film_par_durée, df_genre_KPI = function_KPI_moh()

# ax=sns.histplot(data=film_par_types, x="genres",y='tconst')
# ax.set(xlabel='Genres de Film',
#        ylabel='Total De Nombre De Film',
#        title='Nombre de Films par genre')
# plt.xticks(rotation=90)

def nombre_film_type():
    ax1 = sns.histplot( data = film_par_types , x = "genres" , y = 'tconst')
    ax1.set( xlabel = 'Genres' ,
            ylabel = 'Nombre de films' ,
            title = 'Nombre de films par genre' )
    plt.xticks( rotation = 90 )
    return ax1

###############################################      graph 2   ###################################################
# sns.set_theme(style="whitegrid")
# ax2=sns.barplot(data=genre_mieux_noter, y=genre_mieux_noter.index,x='averageRating',color='b')
# ax2.set(xlabel='La Note Moyenne',
#        ylabel='Genre De Films',
#        title='Les Genres Les Mieux Notés')
# plt.xticks(rotation=90)

def genre_mieux_notes():
    sns.set_theme( style = "whitegrid" )
    ax2 = sns.barplot( data = genre_mieux_noter , y = genre_mieux_noter.index , x = 'averageRating' , color = 'b' )
    ax2.set( xlabel = 'La Note Moyenne' ,
             ylabel = 'Genre De Films' ,
             title = 'Les Genres Les Mieux Notés' )
    plt.xticks( rotation = 90 )
    return ax2

# sns.set_theme( style = "whitegrid" )
# ax3 = sns.barplot( data = film_par_durée, y = film_par_durée.index , x = 'runtimeMinutes' , color = 'r' )
# ax3.set( xlabel = 'La Durée De Film Moyenne(minutes)' ,
#              ylabel = 'Genre De Films' ,
#              title = 'Durée De Film Par Genre' )
# plt.xticks( rotation = 90 )

def duree_film_genre():
    sns.set_theme( style = "whitegrid" )
    ax3 = sns.barplot( data = film_par_durée , y = film_par_durée.index , x = 'runtimeMinutes' , color = 'r' )
    ax3.set( xlabel = 'La Durée De Film Moyenne(minutes)' ,
             ylabel = 'Genre De Films' ,
             title = 'Durée De Film Par Genre' )
    plt.xticks( rotation = 90 )
    return ax3

##########
# Graph in plotly express (Aurelien)
##########


def nombre_film_type2():

    fig = px.histogram(
        film_par_types,
        x="genres",
        y="tconst",
        barmode="group",
        # Selection of aggregation function
        histfunc='sum',
        labels={"genres": "Genres",
                "count_movies": "Films (k unité)"},
        title="Nombre de films par genre")

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

# To check correct display
# fig_nombre_films = nombre_film_type2()
# fig_nombre_films.show()


def genre_mieux_notes2():

    fig = px.scatter(data_frame = genre_mieux_noter,
                     x= "averageRating",
                     y="numVotes",
                     # color_discrete_sequence=["#DC3912", "#E45756", "#EECA3B", "#54A24B", "#109618"],
                     size="numVotes",
                     size_max=25,
                     labels={"averageRating": "Note moyenne",
                             "numVotes": "Nombre de votes (moyenne)"},
                     text=genre_mieux_noter.index,
                     hover_name=genre_mieux_noter.index,
                     title="Notation moyenne par genre")

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
        marker_color='darkblue',
        textposition='bottom center',
        textfont_size=8
    )

    fig.update_layout(
        # Adjust x and Y positioning
        title_x=0.5,
        title_y=0.95,
        # Set backgroud color
        plot_bgcolor='rgb(255,255,255)',
        yaxis_title="Nombre de votes (moyenne)"
    )

    return fig

# To check correct display
# fig_genre_note = genre_mieux_notes2()
# fig_genre_note.show()

def duree_film_genre2():

    """
    No argument, return histogram with average length per genre
    :return:
    """
    fig = px.histogram(
        film_par_durée,
        x=film_par_durée.index,
        y="runtimeMinutes",
        barmode="group",
        # Selection of aggregation function
        histfunc='sum',
        labels={"genres": "Genres",
                "runtimeMinutes": "Durée moyenne (min)"},
        title="Durée moyenne par genre")

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
        yaxis_title="Durée moyenne (min)"
    )

    return fig

# To check correct display
# fig_genre_duree = duree_film_genre2()
# fig_genre_duree.show()
