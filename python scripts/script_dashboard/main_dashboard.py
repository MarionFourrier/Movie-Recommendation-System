# Import libraries
import streamlit as st

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
st.image(clean.dashboard_img)

st.title("plateforme d'analyse de films")

# Input streamlit radio widget with list of different genre
genre = st.radio(
    "Sélectionner votre genre",
    ('Action', 'Aventure', 'Horror'))


# B. Define first dashboard part
# ----------

st.header("Année de sortie")
# Define several tabs within first dashboard part
tab1_ax1, tab2_ax1, tab3_ax1, tab4_ax1, tab5_ax1 = st.tabs(["Nombre films",
                                                            "Durée",
                                                            "Durée par notation",
                                                            "Top 20",
                                                            "Notation et votes"])

# C. Define second dashboard part
# ----------

st.header("Axe 2")
# Define several tabs within streamlit app
tab1_ax2, tab2_ax2 = st.tabs(["tab1_ax2", "tab2_ax2"])

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

# A. 1st axe
# -----------

# Analyse nb movies per year distribution
with tab1_ax1:
    fig_tab1_ax1 = KPI_aur.histogram_year()
    # Display figure on streamlit app by simply calling it
    fig_tab1_ax1

# Analyse average length over decades
with tab2_ax1:
    fig_tab2_ax1 = KPI_aur.average_length()
    fig_tab2_ax1

# Analyse average length over decades based on rating category
with tab3_ax1:
    fig_tab3_ax1 = KPI_aur.average_length_rating()
    fig_tab3_ax1

# Analyse average length over decades based on rating category
with tab4_ax1:
    col1_tab4_ax1, col2_tab4_ax1 = st.columns(2)

    with col1_tab4_ax1:
        starting_year = st.number_input('Choisissez une année de départ',
                                        min_value=KPI_aur.df_movies_year_run_ratings["startYear"].min(),
                                        max_value=KPI_aur.df_movies_year_run_ratings["startYear"].max())

    with col2_tab4_ax1:
        ending_year = st.number_input('Choisissez une année de fin',
                                      min_value=starting_year,
                                      max_value=KPI_aur.df_movies_year_run_ratings["startYear"].max(),
                                      value=KPI_aur.df_movies_year_run_ratings["startYear"].max())


    start_votes, end_votes = st.select_slider(
        'Selectionnez un nombre de vote',
        options=KPI_aur.df_movies_year_run_ratings["numVotes"].sort_values(),
        value=(KPI_aur.df_movies_year_run_ratings["numVotes"].min(),
               KPI_aur.df_movies_year_run_ratings["numVotes"].max())
    )

    fig_tab4_ax1 = KPI_aur.top_20_year(starting_year,
                                       ending_year,
                                       [elem for elem in range(start_votes, end_votes)])
    st.dataframe(fig_tab4_ax1)

# Analyse rating according to number of votes
with tab5_ax1:
    col1_tab5_ax1, col2_tab5_ax1 = st.columns(2)

    with col1_tab5_ax1:
        starting_year2 = st.number_input('Choisissez une année de départ ',
                                        min_value=KPI_aur.df_movies_year_run_ratings["startYear"].min(),
                                        max_value=KPI_aur.df_movies_year_run_ratings["startYear"].max())

    with col2_tab5_ax1:
        ending_year2 = st.number_input('Choisissez une année de fin ',
                                      min_value=starting_year,
                                      max_value=KPI_aur.df_movies_year_run_ratings["startYear"].max(),
                                      value=KPI_aur.df_movies_year_run_ratings["startYear"].max())


    start_votes2, end_votes2 = st.select_slider(
        'Selectionnez un nombre de vote ',
        options=KPI_aur.df_movies_year_run_ratings["numVotes"].sort_values(),
        value=(KPI_aur.df_movies_year_run_ratings["numVotes"].min(),
               KPI_aur.df_movies_year_run_ratings["numVotes"].max())
    )

    fig_tab5_ax1 = KPI_aur.rate_numVote(starting_year2,
                                        ending_year2,
                                        [elem for elem in range(start_votes2, end_votes2)])

