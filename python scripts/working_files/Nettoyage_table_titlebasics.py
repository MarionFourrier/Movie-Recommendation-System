import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# runfile ("python scripts\\table_titlebasics.py")

##########
# 1. First filter on movies categories and exclusion of adult content
##########


# Read entire database
df_title_basics = pd.read_csv(
    "https://datasets.imdbws.com/title.basics.tsv.gz",
    # First line is header
    header=0,
    sep="\t"
)

# Information on database
print(df_title_basics.info())
print("*"*50)

# Type analysis
pivot_title_basics_type = df_title_basics.pivot_table(values="tconst",
                                         index="titleType",
                                         aggfunc="count")
print(pivot_title_basics_type)
print("*"*50)

# Keep only movies
df_title_basics_temp = df_title_basics.loc[(df_title_basics["titleType"] == "movie")]

# isAdult category analysis
print(df_title_basics_temp["isAdult"].value_counts())
print("*"*50)

# Check adult movies content
df_titleBasics_adult = df_title_basics_temp.loc[(df_title_basics_temp["isAdult"] == 1)]

# Delete adult movies and keep only needed columns
# We don't keep "endYear" which is empty for all movies
df_title_basics_temp = df_title_basics_temp.loc[
    (df_title_basics_temp["isAdult"] == 0) | (df_title_basics_temp["isAdult"] == "0"),
    ["tconst", "primaryTitle", "startYear", "runtimeMinutes", "genres"]
]


df_title_basics_temp.loc[df_title_basics_temp["runtimeMinutes"] == "\\N", "runtimeMinutes"] = 0

# Declare conversion parameter dictionary
convert_dict = {"runtimeMinutes": int
                }

# Change Data type in dataframe based on convertion dictionary
df_title_basics_temp = df_title_basics_temp.astype(convert_dict)

print(df_title_basics_temp.dtypes)

##########
# 2. Remaining content analysis
##########


# Analyse nb movies according to runtime
# With Pivot
pivot_title_basics_runtime = df_title_basics_temp.pivot_table(
    values="tconst",
    index="runtimeMinutes",
    aggfunc="count")

# Result => we keep movies at 0 and between 40 and 420 minutes

"**********"

# Analyse nb movies per year distribution
# Using Plotly Express histogram
fig = px.histogram(
    df_title_basics_temp,
    x="startYear",
    y="tconst",
    barmode="group",
    # Selection of aggregation function
    histfunc='count',
    title="Movies distribution per year",
    # Display and format value labels
    text_auto="0.0f")

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

fig.show()

# Analyse of movies from 2023 onwards
# Slicing on dataframe
df_title_basics_2023 = df_title_basics_temp.loc[(df_title_basics_temp["startYear"] == "2023")]

# Result => we keep movies from 1920 to 2022

##########
# 3. Cleaning based on previous analysis
##########

# Selection based on runtime
df_title_basics_temp = df_title_basics_temp.loc[
    (df_title_basics_temp["runtimeMinutes"] == 0) |
    (df_title_basics_temp["runtimeMinutes"] >= 40) &
    (df_title_basics_temp["runtimeMinutes"] <= 420)]

# Replace null values in startYear
df_title_basics_temp.loc[df_title_basics_temp["startYear"] == "\\N", "startYear"] = 0

# Declare conversion parameter dictionary
convert_dict = {"startYear": int
                }

# Change Data type in dataframe based on convertion dictionary
df_title_basics_temp = df_title_basics_temp.astype(convert_dict)

# Selection based on runtime
df_title_basics_temp = df_title_basics_temp.loc[
    (df_title_basics_temp["startYear"] == 0) |
    (df_title_basics_temp["startYear"] >= 1920) &
    (df_title_basics_temp["startYear"] <= 2022)]

##########
# 4. Title basics final version
##########

# Create dataframe title_basics_clean and export CSV
title_basics_clean = df_title_basics_temp.loc[:,["tconst",
                                                 "primaryTitle",
                                                 "startYear",
                                                 "runtimeMinutes"]]

title_basics_clean.to_csv(
    "G:\\.shortcut-targets-by-id\\1ISrfbm7zzuVqO7_ibsR8dnoL6hna0X6B\\PROJET 2\\csv_clean\\title_basics_clean.csv",
    sep=","
)

##########
# 5. Title genre table creation and final version
##########

# Create a new table with genre with several entries per movie
title_genre_clean = df_title_basics_temp.loc[:, ["tconst", "genres"]]
# Classify lines without entries as unknown
title_genre_clean = title_genre_clean.replace("\\N", "Unknown")

# Split genres column and display one genre per line (one movie can have several genres)
# Transform genres as a list type (expand must be false otherwise create as many columns as line with max elements
title_genre_clean["genres"] = title_genre_clean.genres.str.split(",", expand=False)
title_genre_clean = title_genre_clean.explode(column="genres",
                                              ignore_index=True) # To restart index


# Export CSV
title_genre_clean.to_csv(
    "G:\\.shortcut-targets-by-id\\1ISrfbm7zzuVqO7_ibsR8dnoL6hna0X6B\\PROJET 2\\csv_clean\\title_genre_clean.csv",
    sep=","
)

