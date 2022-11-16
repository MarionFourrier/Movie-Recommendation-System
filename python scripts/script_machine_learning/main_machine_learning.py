# Import libraries
import streamlit as st
from st_aggrid import AgGrid

# Import module
import creation_df_machine_learning as dfml

##########
# 1. Build streamlit structure
##########

# A. General dashboard parameters
# -----------

# To run the file from project Python, write the following command in terminal:
# streamlit run "python scripts\\script_machine_learning\\main_machine_learning.py"

# Streamlit page configuration
st.set_page_config(page_title="DataFilm - Plateforme de recommandation",
                   layout='wide',
                   page_icon=':cinema:')

# Picture and dashboard title
st.title("Plateforme de recommandation de films")



# Dataframe for film selection

list_film_selection = dfml.df_film_selection
list_film_selection['titleYear'] = list_film_selection['title'] + ' - ' + list_film_selection['startYear'].astype(str)
list_film_selection = list_film_selection['titleYear'].tolist()
list_film_selection.insert(0, '')

film_selection_input = st.selectbox('Sélectionnez un film', list_film_selection)

