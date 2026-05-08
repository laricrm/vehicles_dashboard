import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Vehicles analysis')

# carregar dados
car_data = pd.read_csv('vehicles.csv')

# botão histograma
if st.button('Show histogram'):
    st.write('Odometer distribution')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# botão scatter
if st.button('Show dispersion chart'):
    st.write('Price vs Odometer')
    fig = px.scatter(car_data, 
                     x="odometer", 
                     y="price"
                     )
    st.plotly_chart(fig, use_container_width=True)