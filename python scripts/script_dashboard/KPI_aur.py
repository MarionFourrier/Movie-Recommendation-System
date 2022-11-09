# Axe 1 => Generic KPI
# Responsible => Aurelien

# Import libraries
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# Import modules
import functions_dashboard as fd
import clean_dataframe as clean


# 4. Data_selection

df_title_basics_year = clean.df_title_basics_clean.loc[clean.df_title_basics_clean["startYear"] != 0]

# Declare conversion parameter dictionary
convert_dict = {"startYear": str}

# Change Data type in dataframe based on conversion dictionary
df_title_basics_year = df_title_basics_year.astype(convert_dict)


def histogram_year():

    """
    No argument, return histogram with number of movies per year
    :return:
    """
    fig = px.histogram(
        df_title_basics_year,
        x="startYear",
        y="tconst",
        barmode="group",
        # Selection of aggregation function
        histfunc='count',
        title="Movies distribution per year")

    fig.update_traces(
        # Adjust bar colors
        marker_color='darkgreen',
        marker_line_width=1.5,
        opacity=0.6)

    fig.update_layout(
        # adjust space between bar
        bargap=0.5,
        title_x=0.5,
        title_y=0.95)

    return fig