# Axe 2 => L'équipe de réalisation
# Responsible => Marion

# Import libraries
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Import modules
import functions_dashboard as fd
import clean_dataframe as clean

# Import des dataframe utilisés
df_title_principals_clean = clean.df_title_principals_clean
df_title_name_basics_clean = clean.df_name_basics_clean
df_title_ratings_clean = clean.df_title_rating_clean


### Exploration de la donnée
# Nb de valeurs par categorie de métier sur title principals
clean.df_title_principals_clean['category'].value_counts()

### Nettoyage des datasets
## df_title_basics_clean
# Suppression des colonnes inutiles
df_title_principals_clean = df_title_principals_clean.drop(columns = ['job', 'characters'])
# Sélection des lignes qui nous intéressent : director, writer, composer
df_writer = df_title_principals_clean.loc[df_title_principals_clean['category'] == 'writer']
df_director = df_title_principals_clean.loc[df_title_principals_clean['category'] == 'director']
df_composer = df_title_principals_clean.loc[df_title_principals_clean['category'] == 'composer']




### Top 10 meilleurs directors
## Merge des tables
df_writer_name = df_writer.merge(df_title_name_basics_clean,
                                 how = 'left',
                                 left_on='nconst',
                                 right_on='nconst')
df_writer_name_ratings = df_writer_name.merge(df_title_ratings_clean,
                                              how = 'left',
                                              left_on='tconst',
                                              right_on='tconst')
# Drop rows with nans
df_writer_name_ratings = df_writer_name_ratings.dropna()
# Drop unuseful columns
df_writer_name_ratings = df_writer_name_ratings.drop(columns = ['tconst', 'category']).reset_index()
# Drop column 'index' with the old index
df_writer_name_ratings = df_writer_name_ratings.drop(columns = 'index')
# Sort by nconst
df_writer_name_ratings = df_writer_name_ratings.sort_values(by='nconst')

# Group by writer in function of average ratings et average nb of votes
df_writer_name_ratings_grouped = df_writer_name_ratings.groupby(['primaryName']).mean()
# Reset index
df_writer_name_ratings_grouped = df_writer_name_ratings_grouped.reset_index()

## Top 10 meilleurs writers par note moyenne : que des inconnus, pas terrible
# Classer par note moyenne, puis nb votes
df_writer_name_ratings_grouped = df_writer_name_ratings_grouped.sort_values(by = ['averageRating', 'numVotes'],
                                                                            ascending = False)
# Sélection 10 premiers
top_10_best_writer_by_average_rating = df_writer_name_ratings_grouped.iloc[:10,0]
# Reset index et numéros de classement dans une colonne
top_10_best_writer_by_average_rating = top_10_best_writer_by_average_rating.reset_index()
top_10_best_writer_by_average_rating = top_10_best_writer_by_average_rating.drop(columns = 'index')
top_10_best_writer_by_average_rating['classement'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Top 10 meilleurs writers par nb votes, les plus populaires : mieux, dommage qu'on puisse pas mettre pour quoi ils sont connus ('KnownForTitles')
# Classer par nb votes
df_writer_name_ratings_grouped = df_writer_name_ratings_grouped.sort_values(by = ['numVotes'],
                                                                            ascending = False)
# Sélection 10 premiers
top_10_best_writer_by_num_votes = df_writer_name_ratings_grouped.iloc[:10,0]
# Reset index et numéros de classement dans une colonne
top_10_best_writer_by_num_votes = top_10_best_writer_by_num_votes.reset_index()
top_10_best_writer_by_num_votes = top_10_best_writer_by_num_votes.drop(columns = 'index')
top_10_best_writer_by_num_votes['classement'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]




### Top 10 meilleurs directors
## Merge des tables
df_director_name = df_director.merge(df_title_name_basics_clean,
                                     how = 'left',
                                     left_on='nconst',
                                     right_on='nconst')
df_director_name_ratings = df_director_name.merge(df_title_ratings_clean,
                                                  how = 'left',
                                                  left_on='tconst',
                                                  right_on='tconst')
# Drop rows with nans
df_director_name_ratings = df_director_name_ratings.dropna()
# Drop unuseful columns
df_director_name_ratings = df_director_name_ratings.drop(columns = ['tconst', 'category']).reset_index()
# Drop column 'index' with the old index
df_director_name_ratings = df_director_name_ratings.drop(columns = 'index')
# Sort by nconst
df_director_name_ratings = df_director_name_ratings.sort_values(by='nconst')

# Group by writer in function of average ratings et average nb of votes
df_director_name_ratings_grouped = df_director_name_ratings.groupby(['primaryName']).mean()
# Reset index
df_director_name_ratings_grouped = df_director_name_ratings_grouped.reset_index()

## Top 10 meilleurs writers par note moyenne : que des inconnus, pas terrible
# Classer par note moyenne, puis nb votes
df_director_name_ratings_grouped = df_director_name_ratings_grouped.sort_values(by = ['averageRating', 'numVotes'],
                                                                                ascending = False)
# Sélection 10 premiers
top_10_best_director_by_average_rating = df_director_name_ratings_grouped.iloc[:10,0]
# Reset index et numéros de classement dans une colonne
top_10_best_director_by_average_rating = top_10_best_director_by_average_rating.reset_index()
top_10_best_director_by_average_rating = top_10_best_director_by_average_rating.drop(columns = 'index')
top_10_best_director_by_average_rating['classement'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Top 10 meilleurs writers par nb votes, les plus populaires : mieux, dommage qu'on puisse pas mettre pour quoi ils sont connus ('KnownForTitles')
# Classer par nb votes
df_director_name_ratings_grouped = df_director_name_ratings_grouped.sort_values(by = ['numVotes'],
                                                                                ascending = False)
# Sélection 10 premiers
top_10_best_director_by_num_votes = df_director_name_ratings_grouped.iloc[:10,0]
# Reset index et numéros de classement dans une colonne
top_10_best_director_by_num_votes = top_10_best_director_by_num_votes.reset_index()
top_10_best_director_by_num_votes = top_10_best_director_by_num_votes.drop(columns = 'index')
top_10_best_director_by_num_votes['classement'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]



### Top 10 meilleurs composer
## Merge des tables
df_composer_name = df_composer.merge(df_title_name_basics_clean,
                                     how = 'left',
                                     left_on='nconst',
                                     right_on='nconst')
df_composer_name_ratings = df_composer_name.merge(df_title_ratings_clean,
                                                  how = 'left',
                                                  left_on='tconst',
                                                  right_on='tconst')
# Drop rows with nans
df_composer_name_ratings = df_composer_name_ratings.dropna()
# Drop unuseful columns
df_composer_name_ratings = df_composer_name_ratings.drop(columns = ['tconst', 'category']).reset_index()
# Drop column 'index' with the old index
df_composer_name_ratings = df_composer_name_ratings.drop(columns = 'index')
# Sort by nconst
df_composer_name_ratings = df_composer_name_ratings.sort_values(by='nconst')

# Group by writer in function of average ratings et average nb of votes
df_composer_name_ratings_grouped = df_composer_name_ratings.groupby(['primaryName']).mean()
# Reset index
df_composer_name_ratings_grouped = df_composer_name_ratings_grouped.reset_index()

## Top 10 meilleurs writers par note moyenne : que des inconnus, pas terrible
# Classer par note moyenne, puis nb votes
df_composer_name_ratings_grouped = df_composer_name_ratings_grouped.sort_values(by = ['averageRating', 'numVotes'],
                                                                                ascending = False)
# Sélection 10 premiers
top_10_best_composer_by_average_rating = df_composer_name_ratings_grouped.iloc[:10,0]
# Reset index et numéros de classement dans une colonne
top_10_best_composer_by_average_rating = top_10_best_composer_by_average_rating.reset_index()
top_10_best_composer_by_average_rating = top_10_best_composer_by_average_rating.drop(columns = 'index')
top_10_best_composer_by_average_rating['classement'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

## Top 10 meilleurs writers par nb votes, les plus populaires : mieux, dommage qu'on puisse pas mettre pour quoi ils sont connus ('KnownForTitles')
# Classer par nb votes
df_composer_name_ratings_grouped = df_composer_name_ratings_grouped.sort_values(by = ['numVotes'],
                                                                                ascending = False)
# Sélection 10 premiers
top_10_best_composer_by_num_votes = df_composer_name_ratings_grouped.iloc[:10,0]
# Reset index et numéros de classement dans une colonne
top_10_best_composer_by_num_votes = top_10_best_composer_by_num_votes.reset_index()
top_10_best_composer_by_num_votes = top_10_best_composer_by_num_votes.drop(columns = 'index')
top_10_best_composer_by_num_votes['classement'] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]