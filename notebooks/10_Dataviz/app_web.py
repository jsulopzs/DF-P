import pandas as pd
import plotly.express as px

import streamlit as st
st.title('Mi pagina web')

df = pd.read_csv('data/gapminder.csv')
df


fig = px.scatter(
    data_frame=df, x="gdpPercap", y="lifeExp",
    size="pop", color="continent", hover_name="country",
    animation_frame="year", animation_group="country",
    log_x=True, size_max=55, range_x=[100,100000], range_y=[25,90]
)

fig