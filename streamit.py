import pandas as pd
import streamlit as st
import seaborn as sns
st.title("analyse de correlation et de distribution")


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_weather = pd.read_csv(link)
genre=st.radio(
    "what your favorate movie genre",
    ('US','Europe','Japan'))

col_select=genre
df_weather[df_weather['continent'].str.contains(col_select)]
col='mpg'
viz_distri=sns.scatterplot(data=df_weather,x='year',y=col)
st.pyplot(viz_distri.figure)