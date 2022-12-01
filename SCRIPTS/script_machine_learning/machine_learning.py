##########
# IMPORT DES LIBRAIRIES ET MODULES :
##########

import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import NearestNeighbors
import clean_dataframe as c


##########
# IMPORT DES DATAFRAMES ET PREPARATION DES DONNEES
##########

# Import dataframe
link_df_machine_learning = f"{c.directory_aurelien}df_machine_learning.csv"
df_machine_learning = pd.read_csv(link_df_machine_learning)
link_title_genre_clean = f"{c.directory_aurelien}title_genre_clean.csv"
df_title_genre_clean = pd.read_csv(link_title_genre_clean)

# Adaptation df_machine_learning
df_machine_learning.drop(columns = ['Unnamed: 0', 'Unknown', 'Adult'], inplace=True)

# Adaptation df_title_genre_clean
df_title_genre_clean['genres'] = df_title_genre_clean['genres'].apply(lambda x: x+" ")
df_title_genre_clean = df_title_genre_clean.groupby('tconst').sum()


##########
# DÉFINITION D'UNE FONCTION DE RECOMMANDATION DE FILMS :
##########

def syst_reco(entree):
    """
    Fonction qui recherche les 5 plus proches voisins de l'entree
    :param entree: entree utilisateur = un film sous forme de 'tconst'
    :return: dataframe avec liste de 5 films recommandés, leur année de sortie, leur genre ?
    """

    # Sélection des X(date sortie et genre)
    X = df_machine_learning.select_dtypes('number').drop(columns=['averageRating', 'numVotes'])

    ## Standardisation des X
    # Entrainement du modèle
    scaler = StandardScaler().fit(X)
    # Transformation de la donnée
    X_scaled = scaler.transform(X)

    # Localisation du film d'entree dans le dataframe
    ligne_entree = df_machine_learning.loc[df_machine_learning['tconst'] == entree]
    ligne_entree = ligne_entree.index
    ligne_entree = ligne_entree[0]

    # Données à comparer
    ligne_entree = X_scaled[[ligne_entree]]

    ## Recherche des plus proches voisins
    # Instanciation et entrainement du modèle (kNN)
    modelKNN = NearestNeighbors(n_neighbors=6, ).fit(X_scaled)
    # Recherche du/des voisins les plus proches de(s) l'entrée(s)
    neighbors_distance, neighbors_index = modelKNN.kneighbors(ligne_entree)
    # Sélection de l'index du plus proche voisin
    result_index = list(neighbors_index[0, 1:])
    # Récupération de la ligne du film plus proche
    result = pd.DataFrame()
    for n in result_index:
        serie = df_machine_learning.loc[n]
        serie = pd.DataFrame(serie)
        serie = serie.T
        result = pd.concat([result, serie])
    ## Merge entre result et df_title_genre_clean sur les tconst de sortie du ML :
    sortie = pd.merge(result,
                      df_title_genre_clean,
                      how='left',
                      left_on='tconst',
                      right_on='tconst')
    ## Suppression des colonnes inutiles :
    sortie = sortie[['title', 'startYear', 'averageRating', 'numVotes', 'genres']]
    return sortie

"""
# Test
entree = 'tt0010969'
result = syst_reco(entree)
"""

"""
AXES D'AMELIORATION :
	1) Nlp/mining/decision tree pour acteurs, equie de tournage : decision tree après le knn sur casting
	2) Rajouter poids 
	3) Idée de sentiments par genre, clustering : regrouper les genres par rapport à une émotion 
	4) Entrer plusieurs films, créer un film fictif avec moyenne des films entrés : plusieurs films d'entrées
	5) Websraper l'affiche du film de sortie
	6) L'utilisateur renseigne un ordre d'importance sur les critères de recherche (genre, année...) : input poids
	7) KPI : les rendre encore plus dynamiques
	8) Optimisation du code : temps de traitement, mais comme on a du fonctionner en local et chacun séparemment (on est pas sur git)...

QUESTIONS :
- SCALER LES DONNEES
- WEIGHTS GENRES 
- SORTIR LES GENRES DES FILMS DE SORTIE
"""

"""
### ESSAIS : A CONSERVER EN CAS DE MODIFICATION POUR TESTER LA FONCTION LIGNE PAR LIGNE

# Sélection des X(date sortie et genre)
X = df_machine_learning.select_dtypes('number').drop(columns=['averageRating', 'numVotes'])

## Standardisation des X
# Entrainement du modèle
scaler = StandardScaler().fit(X)
# Transformation de la donnée
X_scaled = scaler.transform(X)
# Diminution du poids de 'startYear'
#X_scaled[:, 0] = X_scaled[:, 0] / 2

# L'atlantide
entree = 'tt0010969'
# Fast and furious
fast_and_furious = df_machine_learning.loc[df_machine_learning['title'].str.contains('Fast and Furious')]
entree = 'tt0232500'
# Frere des ours
frere_des_ours = df_machine_learning.loc[df_machine_learning['title'].str.contains('Frère des ours')]
entree = 'tt0328880'

# Localisation du film d'entree dans le dataframe
ligne_entree = df_machine_learning.loc[df_machine_learning['tconst'] == entree]
ligne_entree = ligne_entree.index
ligne_entree = ligne_entree[0]

# Données à comparer
ligne_entree = X_scaled[[ligne_entree]]

## Recherche des plus proches voisins
# Instanciation et entrainement du modèle (kNN)
modelKNN = NearestNeighbors(n_neighbors=6, ).fit(X_scaled)
# Recherche du/des voisins les plus proches de(s) l'entrée(s)
neighbors_distance, neighbors_index = modelKNN.kneighbors(ligne_entree)
# Sélection de l'index du plus proche voisin
result_index = list(neighbors_index[0, 1:])
# Récupération de la ligne du film plus proche
result = pd.DataFrame()
for n in result_index:
    serie = df_machine_learning.loc[n]
    serie = pd.DataFrame(serie)
    serie = serie.T
    result = pd.concat([result, serie])
"""