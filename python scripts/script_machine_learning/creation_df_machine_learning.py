# Création d'un dataframe avec les infos qu'on voudra utiliser pour l'algo (une ligne par film) :
    # tconst
    # Nom du film : prendre titre de film français dans title_akas
    # Date sortie : title_basics
    # Genre : title_genre

# Préparation du dataframe au machine learning :
    # Get dummies sur les genres

# Import des librairies et modules
import pandas as pd
import numpy as np
import clean_dataframe as cd

# Import des df
df_title_akas_clean = cd.df_title_akas_clean
df_title_basics_clean = cd.df_title_basics_clean
df_title_genre_clean = cd.df_title_genre_clean
df_title_rating_clean = cd.df_title_rating_clean


### Préparation de title_akas :
# Sélection uniquement des titres français
df_title_akas_FR = df_title_akas_clean.loc[df_title_akas_clean['region'] == 'FR']
# Suppression des colonnes inutiles
df_title_akas_FR = df_title_akas_FR.drop(columns = ['ordering', 'region', 'isOriginalTitle'])

### Préparation de la table title_basics
# Suppression des films de 0 min
df_title_basics_clean = df_title_basics_clean.loc[df_title_basics_clean['runtimeMinutes'] != 0]
# Suppression des colonnes 'runtimeMinutes', 'primaryTitle' :
df_title_basics_clean = df_title_basics_clean.drop(columns = ['runtimeMinutes', 'primaryTitle'])


### Création de la table pour le machine learning :
# Jointure title_akas et title_basics :
df_machine_learning = pd.merge(df_title_akas_FR,
                               df_title_basics_clean,
                               how = 'inner',
                               left_on = 'titleId',
                               right_on = 'tconst')
# Jointure à title_ratings :
df_machine_learning = pd.merge(df_machine_learning,
                               df_title_rating_clean,
                               how = 'inner',
                               left_on = 'tconst',
                               right_on = 'tconst')
# Suppression de la colonne 'titleId' :
df_machine_learning = df_machine_learning.drop(columns = 'titleId')

### Nettoyage de la donnée :
# Suppression des startYear = 0
df_machine_learning = df_machine_learning.loc[df_machine_learning['startYear'] != 0]
# Suppression des duplicates
df_machine_learning.duplicated(subset = 'tconst').sum()
df_machine_learning = df_machine_learning.drop_duplicates(subset = ['tconst'])


### Jointure de title_genre à df_machine_learning :
df_machine_learning = pd.merge(df_machine_learning,
                               df_title_genre_clean,
                               how = 'inner',
                               left_on = 'tconst',
                               right_on = 'tconst')


### Numérisation de la colonne genre :
df_machine_learning = pd.concat([df_machine_learning,
                                 df_machine_learning['genres'].str.get_dummies()],
                                axis = 1)
"""
# Créer nouveau df :
# Boucle :
    # Créer mini df par film
    # Dans chacun de ces df, créer une ligne avec tconst et la somme des caractéristiques de genres

# Boucle : pour chaque ligne df :
    # Si tconst = tconst ligne-1 :
        # Additionner les colonnes genres
        # Supprimer ???

# Get dummies sur title_genre :
#df_title_genre_clean = pd.concat([df_title_genre_clean,
                                 df_title_genre_clean['genres'].str.get_dummies()],
                                 axis = 1)

# Liste avec genres :
liste_genres = df_machine_learning.columns[6:]
liste_genres = list(liste_genres)

# Création df vide
# Boucle sur toutes les lignes du df :
    # Si tconst de la ligne = tconst de la ligne d'après :
        # Pour chaque colonne comprise dans la liste 'liste_genres' :
            # Additionner les items des colonnes de genre avec la ligne du dessous
    # Ajouter ligne au nouveau df

df_final = pd.DataFrame()
row = 0
for row in range (len(df_machine_learning)):
    if df_machine_learning.iloc[row, 1] == df_machine_learning.iloc[(row+1), 1]:
        for column in liste_genres:
            #df_machine_learning.loc[row, column].add(df_machine_learning.loc[(row+1), column])
            df_machine_learning.loc[row, column] = df_machine_learning.loc[row, column] + df_machine_learning.loc[(row+1), column]
    row += 1
    df_final.append(df_machine_learning.iloc[row, :])

df_machine_learning.iloc[row, column]
df_machine_learning.iloc[(row+1), 1]
df_machine_learning.iloc[row, 1]
for column in liste_genres:
    print(df_machine_learning.loc[row, column])
type(df_machine_learning.loc[row, column])
df_machine_learning.loc[row, :]
a = df_machine_learning.loc[row, 'tconst']
"""
#############################################################diminution de la DataFrame #######################################################################

####       netvoyage avec une note moyenne de vote plus que 5    ###

indexNames = df_machine_learning[ df_machine_learning['averageRating'] <= 5 ].index
indexNames
df_machine_learning.drop(index=indexNames,inplace = True)
df_machine_learning=df_machine_learning.reset_index( drop = True )
##################################################################

#    natvoyage avec une un nombre de vu plus que 389###################
indexNames2=df_machine_learning[df_machine_learning['numVotes']<=389].index
df_machine_learning.drop(index=indexNames2,inplace = True)
df_machine_learning=df_machine_learning.reset_index( drop = True )





####################################################################
'''
df_drop_mavhine_lerning = df_machine_learning[df_machine_learning[averegeRating]>=5]

df_total=df_machine_learning.iloc[0:1]
df_total.shape
#je supprime la colone 'genres' qu'on a plus besoin
df_total=df_total.drop(['genres'], axis=1)
df_total
#je boucke un code pour faire la fusion des colonne qui contienne 0ou 1
for i in df_machine_learning['tconst']:
    print(i)
    #création d'une DataFrame vide
    df_final = []
    #choisir un film avec tconst
    df_modif = df_machine_learning[df_machine_learning['tconst'] == i]
    # prendre un interval des valeurs qui nous intéresse, puis aditionner les ligne
    df_cumul = df_modif.values[: , 6:33].sum( axis = 0 )
    #la partie qui change pas , on prends une seuls ligne en cas ou il y a plusieurs par film
    df_static = df_modif.values[0:1 , 0:5]
    #convertir le array np en DataFrame
    df_cumul = pd.DataFrame( df_cumul )
    #transposer le DataFrame
    df_cumul = df_cumul.T
    #convertir la deuxième partir en DataFrame
    df_static = pd.DataFrame( df_static )
    #composer la ligne de film

    df_final = pd.concat( [df_static , df_cumul] , axis = 1 )
    #renommer les colonne
    df_final.set_axis( ['title' , 'tconst' , 'startYear' , 'averageRating' , 'numVotes' , 'Action' ,
                        'Adult' , 'Adventure' , 'Animation' , 'Biography' , 'Comedy' , 'Crime' ,
                        'Documentary' , 'Drama' , 'Family' , 'Fantasy' , 'Film-Noir' , 'History' ,
                        'Horror' , 'Music' , 'Musical' , 'Mystery' , 'News' , 'Reality-TV' ,
                        'Romance' , 'Sci-Fi' , 'Short' , 'Sport' , 'Thriller' , 'Unknown' , 'War' ,
                        'Western'] , axis = 'columns' , inplace = True )
    #composer le DataFrame Total
    df_total = pd.concat( [df_total , df_final] )
    df_total_sans_doublant=df_total.drop_duplicates()
    df_machine_learning_2=df_total_sans_doublant.reset_index(inplace = True)
'''
#################################################### Le même code avec NUMPY  ################################
df_final = []
df_modif = df_machine_learning[df_machine_learning['tconst'] == 'tt0010323']
df_cumul = df_modif.values[: , 6:33].sum( axis = 0 )
df_static = df_modif.values[0:1 , 0:5]
df_cumul = pd.DataFrame( df_cumul )
df_cumul = df_cumul.T
df_static = pd.DataFrame( df_static )

df_final = pd.concat( [df_static , df_cumul] , axis = 1 )
df_final.set_axis(['title', 'tconst', 'startYear', 'averageRating', 'numVotes', 'Action',
       'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
       'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History',
       'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV',
       'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'Unknown', 'War',
       'Western'], axis='columns', inplace=True)
df_total = pd.concat( [df_total, df_final])
##############################################################################################
df_modif = df_machine_learning[df_machine_learning['tconst'] == 'tt0010323']
df_cumul = df_modif.values[: , 6:33].sum( axis = 0 )
df_static = df_modif.values[0:1 , 0:5]
numpy_first=np.concatenate((df_static,df_cumul),axis=None)
for i in df_machine_learning['tconst']:
    print(i)
    df_modif = df_machine_learning[df_machine_learning['tconst'] == i]
    df_cumul = df_modif.values[: , 6:33].sum( axis = 0 )
    df_static = df_modif.values[0:1 , 0:5]
    ligne_film = np.concatenate( (df_static , df_cumul) , axis = None )

    numpy_first = np.column_stack((numpy_first , ligne_film))

array=numpy_first.T
df_machine_learning_clean=pd.DataFrame(array,columns =['title', 'tconst', 'startYear', 'averageRating', 'numVotes', 'Action',
       'Adult', 'Adventure', 'Animation', 'Biography', 'Comedy', 'Crime',
       'Documentary', 'Drama', 'Family', 'Fantasy', 'Film-Noir', 'History',
       'Horror', 'Music', 'Musical', 'Mystery', 'News', 'Reality-TV',
       'Romance', 'Sci-Fi', 'Short', 'Sport', 'Thriller', 'Unknown', 'War',
       'Western'] )
df_machine_learning_clean=df_machine_learning_clean.drop_duplicates()
df_machine_learning_clean=df_machine_learning_clean.reset_index(drop= True)
df_machine_learning_clean=.to_csv (f"{ct.directory_mohammed}title_machine_learning_clean.csv", sep = ",", index = False)