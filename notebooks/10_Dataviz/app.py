import streamlit as st
import pandas as pd
import plotly.express as px
import os

file_directory = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(file_directory, 'data/gapminder.csv')
df = pd.read_csv(path)

st.set_page_config(layout='wide')

st.title('Data Application')

fig = px.scatter(
    data_frame=df, x="gdpPercap", y="lifeExp",
    size="pop", color="continent", hover_name="country",
    animation_frame="year", animation_group="country",
    log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90]
)

st.write('## Plot')
st.plotly_chart(fig)

st.write('## Table')
st.write(df)