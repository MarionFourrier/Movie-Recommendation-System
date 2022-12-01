# Import libraries
import pandas as pd
import streamlit as st
from st_aggrid import AgGrid

# Import des modules :
import clean_dataframe as clean
import machine_learning as ml

# Import des tables :
link_df_machine_learning = f"{clean.directory_aurelien}df_machine_learning.csv"
df_film_selection = pd.read_csv(link_df_machine_learning,
                                sep=",",
                                header=0,
                                usecols=['title', 'tconst', 'startYear'])



##########
# 1. Build streamlit structure
##########

# A. General dashboard parameters
# -----------

# To run the file from project Python, write the following command in terminal:
# streamlit run "script_machine_learning\\main_machine_learning.py"

# Streamlit page configuration
st.set_page_config(page_title="CineCreuse - N°1 sur les films",
                   layout='wide',
                   page_icon=':cinema:')

# Picture and dashboard title
st.title("Plateforme de recommandation de films")
st.image(clean.dashboard_img)



# Dataframe for film selection
df_film_selection['titleYear'] = df_film_selection['title'] + ' - ' + df_film_selection['startYear'].astype(str)
list_film_selection = df_film_selection['titleYear'].tolist()
list_film_selection.insert(0, '')

# Select movie for recommandation
film_selection_input = st.selectbox('Sélectionnez un film', list_film_selection)

##########
# 2. Display results
##########

# If no movie selection, pass
if film_selection_input == '':
    pass
else:
    # Find back the tconst from movie selection
    film_selection_tconst = df_film_selection.loc[df_film_selection['titleYear'] == film_selection_input,
                                              ['tconst']]

    # extract tconst value
    film_selection_tconst = film_selection_tconst.iloc[0, 0]

    st.subheader("CineCreuse vous suggère les films suivants, bon visionnage :")

    # Display result calling machine learning function with film selected as argument
    list_recommandation = ml.syst_reco(film_selection_tconst)
    AgGrid(list_recommandation, fit_columns_on_grid_load=True)

