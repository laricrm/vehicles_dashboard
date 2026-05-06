import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Análise de Veículos')

# carregar dados
car_data = pd.read_csv('vehicles.csv')

# botão histograma
if st.button('Mostrar histograma'):
    st.write('Distribuição do odômetro')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)

# botão scatter
if st.button('Mostrar gráfico de dispersão'):
    st.write('Preço vs Odômetro')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)