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

# Créer nouveau df :
# Boucle :
    # Créer mini df par film
    # Dans chacun de ces df, créer une ligne avec tconst et la somme des caractéristiques de genres

# Boucle : pour chaque ligne df :
    # Si tconst = tconst ligne-1 :
        # Additionner les colonnes genres
        # Supprimer ???
