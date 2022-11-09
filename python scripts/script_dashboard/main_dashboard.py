# Import libraries
import streamlit as st

# Import modules
import KPI_aur
import KPI_mar
import KPI_ale
import KPI_moh

# 1. Build streamlit structure
# To run the file from project Python, write the following command in terminal:
# streamlit run "script_dashboard\\main_dashboard.py"

st.title("plateforme d'analyse de films")

# Input streamlit radio widget with list of different genre
genre = st.radio(
    "Sélectionner votre genre",
    ('US', 'Europe', 'Japan'))

# Define first dashboard part
st.header("Axe 1")
# Define several tabs within first dashboard part
tab1_ax1, tab2_ax1 = st.tabs(["Année", "Durée"])

# Define second dashboard part
st.header("Axe 2")
# Define several tabs within streamlit app
tab1_ax2, tab2_ax2 = st.tabs(["tab1_ax2", "tab2_ax2"])

# Define third dashboard part
st.header("Axe 3")
# Define several tabs within streamlit app
tab1_ax3, tab2_ax3 = st.tabs(["tab1_ax3", "tab2_ax3"])

# Define fourth dashboard part
st.header("Axe 4")
# Define several tabs within streamlit app
tab1_ax4, tab2_ax4 = st.tabs(["tab1_ax4", "tab2_ax4"])

# 1. Attach chart (seaborn, plotly.express)

with tab1_ax1:
    # Analyse nb movies per year distribution
    fig = KPI_aur.histogram_year()

    # Display figure on streamlit app by simply calling it
    fig
