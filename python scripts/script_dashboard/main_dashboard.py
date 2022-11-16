# Import libraries
import streamlit as st
from st_aggrid import AgGrid
import seaborn as sns
import matplotlib.pyplot as plt

# Import modules
import clean_dataframe as clean
import KPI_aur
import KPI_mar
import KPI_ale
import KPI_moh

##########
# 1. Build streamlit structure
##########

# A. General dashboard parameters
# -----------

# To run the file from project Python, write the following command in terminal:
# streamlit run "python scripts\\script_dashboard\\main_dashboard.py"

# Streamlit page configuration
st.set_page_config(page_title="DataFilm - Plateforme de recommandation",
                   layout='wide',
                   page_icon=':cinema:')

# Picture and dashboard title
st.image(clean.dashboard_img)
st.title("Plateforme d'analyse de films")

# Implement selection widgets in sidebar
starting_year = st.sidebar. number_input('Choisissez une année de départ',
                                          min_value=KPI_aur.df_movies_year_run_ratings["startYear"].min(),
                                          max_value=KPI_aur.df_movies_year_run_ratings["startYear"].max())

ending_year = st.sidebar.number_input('Choisissez une année de fin',
                                      min_value=starting_year,
                                      max_value=KPI_aur.df_movies_year_run_ratings["startYear"].max(),
                                      value=KPI_aur.df_movies_year_run_ratings["startYear"].max())



start_votes, end_votes = st.sidebar.select_slider(
        'Selectionnez un nombre de votes ',
        options=range(KPI_aur.df_movies_year_run_ratings["numVotes"].min(),
                      KPI_aur.df_movies_year_run_ratings["numVotes"].max()+2),
            #KPI_aur.df_movies_year_run_ratings["numVotes"].sort_values(),
        value=(KPI_aur.df_movies_year_run_ratings["numVotes"].min(),
               KPI_aur.df_movies_year_run_ratings["numVotes"].max()+1)
)

# B. Define first dashboard part
# ----------

st.header("Année de sortie et durée")
# Define several tabs within first dashboard part
tab1_ax1, tab2_ax1, tab3_ax1, tab4_ax1, tab5_ax1 = st.tabs(["Nombre films",
                                                            "Durée",
                                                            "Durée par notation",
                                                            "Top 20",
                                                            "Notation et votes"])

# C. Define second dashboard part
# ----------

st.header("Genre")
# Define several tabs within streamlit app
tab1_ax2, tab2_ax2, tab3_ax2 = st.tabs(["Nombre de films",
                                        "Notation",
                                        "Durée"])

# D. Define third dashboard part
# -----------

st.header("Axe 3")
# Define several tabs within streamlit app
tab1_ax3, tab2_ax3 = st.tabs(["tab1_ax3", "tab2_ax3"])

# E. Define fourth dashboard part
# ----------

st.header("Axe 4")
# Define several tabs within streamlit app
tab1_ax4, tab2_ax4 = st.tabs(["tab1_ax4", "tab2_ax4"])

##########
# 2. Attach chart (seaborn, plotly.express)
##########

# A. 1st axe => Date de sortie et durée
# -----------

# Analyse nb movies per year distribution
with tab1_ax1:
    fig_tab1_ax1 = KPI_aur.histogram_year()
    # Display figure on streamlit app by simply calling it through plotly_chart object
    # Allowing to set use_container_width parameter to display on full width
    st.plotly_chart(fig_tab1_ax1, use_container_width=True)

# Analyse average length over decades
with tab2_ax1:
    fig_tab2_ax1 = KPI_aur.average_length()
    st.plotly_chart(fig_tab2_ax1, use_container_width=True)

# Analyse average length over decades based on rating category
with tab3_ax1:
    fig_tab3_ax1 = KPI_aur.average_length_rating()
    st.plotly_chart(fig_tab3_ax1, use_container_width=True)

# Analyse average length over decades based on rating category
with tab4_ax1:
    fig_tab4_ax1 = KPI_aur.top_20_year(starting_year,
                                       ending_year,
                                       [elem for elem in range(start_votes, end_votes)])
    AgGrid(fig_tab4_ax1,
           fit_columns_on_grid_load=True)

# Analyse rating according to number of votes
with tab5_ax1:
    fig_tab5_ax1 = KPI_aur.rate_numVote(starting_year,
                                        ending_year,
                                        [elem for elem in range(start_votes, end_votes)])

    st.plotly_chart(fig_tab5_ax1, use_container_width=True)


# B. 2nd axe => Genre
# -----------

# Analyse nb movies per genre
with tab1_ax2:
    fig_tab1_ax2 = KPI_moh.nombre_film_type2()
    st.plotly_chart(fig_tab1_ax2, use_container_width=True)

with tab2_ax2:
    fig_tab2_ax2 = KPI_moh.genre_mieux_notes2()
    st.plotly_chart(fig_tab2_ax2, use_container_width=True)

with tab3_ax2:
    fig_tab3_ax2 = KPI_moh.duree_film_genre2()
    st.plotly_chart(fig_tab3_ax2, use_container_width=True)

