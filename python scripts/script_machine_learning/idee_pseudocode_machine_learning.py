# Création d'un dataframe avec les infos qu'on voudra utiliser pour l'algo (une ligne par film) :
    # tconst
    # Nom film : prendre titre de film français dans title_akas
    # Date sortie
    # Genre : get dummies

# Préparation du dataframe :
    # Vérifier qu'il n'y ait pas de nan
    # Vérifier qu'il n'y ait pas de doublons
    # Numériser les données (encoder ? normalisation ?... comment traiter les membres du casting ? Nlp ?)

# Définition d'une fonction qui prend en argument le nom d'un ou plusieurs films :
  # Input
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

CONSEIL :
--> Aller voir live Coding sur plus proches voisins 