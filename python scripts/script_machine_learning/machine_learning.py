# Import des librairies :
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.neighbors import NearestNeighbors
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

# Import des modules :
import creation_df_machine_learning as cdfml

# Import des tables :
df_machine_learning = cdfml.df_machine_learning

# Entrée.s utilisateur sur le main, via Streamlit
entree = 'Fast and furious'

# Définition d'une fonction qui prend en argument le/les entrées utilisateurs :
def syst_reco(entree):
    """
    Fonction qui recherche les plus proches voisins des entrées dans le df_machine_learning
    :param entree: entree utilisateur = un ou plusieurs titres de films
    :return: dataframe avec liste de films recommandés, leur année de sortie, leur genre ?
    """
    # Localisation du/des film.s dans le dataframe
    ligne_entree = df_machine_learning.loc[df_machine_learning['title'].str.contains(entree, case=False)]
    ligne_entree = ligne_entree.select_dtypes('number').drop(columns=['averageRating', 'numVotes'])
    # Sélection des X(date sortie et genre) et y(tconst)
    X = df_machine_learning.select_dtypes('number').drop(columns=['averageRating', 'numVotes'])
    # Instanciation et entrainement du modèle (kNN)
    modelKNN = NearestNeighbors(n_neighbors=2).fit(X)
    # Recherche du/des voisins les plus proches de(s) l'entrée(s)
    neighbors_distance, neighbors_index = modelKNN.kneighbors(ligne_entree)
    # Transformation de l'array récupéré avec l'index des prédictions sous forme de liste
    result_index = list(neighbors_index[1])
    # Récupération des noms des films prédits dans le dataframe de base, à partir de la liste précédemment récupérée (le(s) titre(s) ou autres informations qu'on veut afficher en sortie)
    sortie = df_machine_learning.loc[result_index]
    # Return
    return sortie

if entree not in df_machine_learning['title']:
    print('Ce film n\'est pas dans notre base de donnée, essaye avec un autre !')

### ESSAIS :

syst_reco('Frère des ours')
syst_reco('Le dîner de cons') # pas dans la liste, sort erreur
syst_reco('Harry Potter')
a = syst_reco('peur')
b = syst_reco('magie')
syst_reco('titanic')
syst_reco('fast and furious')
syst_reco('La cité de la peur')
syst_reco('noël')
syst_reco('persepolis')
syst_reco('inception')

entree = 'Harry Potter'
# Localisation du/des film.s dans le dataframe
ligne_entree = df_machine_learning.loc[df_machine_learning['title'].str.contains(entree, case=False)]
ligne_entree = ligne_entree.select_dtypes('number').drop(columns=['averageRating', 'numVotes'])
# Sélection des X(date sortie et genre) et y(tconst)
X = df_machine_learning.select_dtypes('number').drop(columns=['averageRating', 'numVotes'])
# Instanciation et entrainement du modèle (kNN)
modelKNN = NearestNeighbors(n_neighbors=2).fit(X)
# Recherche du/des voisins les plus proches de(s) l'entrée(s)
neighbors_distance, neighbors_index = modelKNN.kneighbors(ligne_entree)
# Transformation de l'array récupéré avec l'index des prédictions sous forme de liste
result_index = list(neighbors_index[1])
# Récupération des noms des films prédits dans le dataframe de base, à partir de la liste précédemment récupérée (le(s) titre(s) ou autres informations qu'on veut afficher en sortie)
sortie = df_machine_learning.loc[result_index]


  # Filtre films de sortie avec numVotes(3è quartile ou moyenne) et rating(sup 5)
  # Retourner les films (ou autres informations à propos de ces films)

# Définition d'une fonction qui prend en argument le nom d'un ou plusieurs films :
  # Localisation du/des films dans le dataframe
  # Sélection des X(date sortie et genre) et y(tconst)
  # Train split test
  # Instanciation du modèle (kNN)
  # Entrainement du modèle
  # Amélioration du modèle (métriques et ajustements)
  # Recherche du/des voisins les plus proches de(s) l'entrée(s)
  # Transformation de l'array récupéré avec l'index des prédictions sous forme de liste
  # Récupération des noms des films prédits dans le dataframe de base, à partir de la liste précédemment récupérée (le(s) titre(s) ou autres informations qu'on veut afficher en sortie)
  # Filtre films de sortie avec numVotes(3è quartile ou moyenne) et rating(sup 5)
  # Retourner les films (ou autres informations à propos de ces films)

# Intégration à Streamlit
   # Vérifier que l'input corresponde bien à un titre de notre BDD (split puis str.contains ?)

"""
ALGO :
	1) Chercher knn par date sortie et genre 
	2) Analyser précision, métrique, affiner modèle, regarder ce qui sort en terme acteur et réal
	3) Essayer nuage de mots, mining sur mots...
	   OU décision tree

AXES D'AMELIORATION :
	1) Nlp/mining/decision tree pour acteurs
	2) Rajouter réalisateur 
	3) Rajouter poids 
	4) Notations : filtre films de sortie avec numVotes(3è quartile ou moyenne) et rating(sup 5)
	5) Idée de sentiments par genre, clustering... ? 
	6) Entrer plusieurs films, créer un film fictif avec moyenne des films entrés, 
	7) Si jamais film entré n'est pas compris dans la database, le signifier et demander de rentrer un nouveau film

CONSEIL :
--> Aller voir live Coding sur plus proches voisins 
"""