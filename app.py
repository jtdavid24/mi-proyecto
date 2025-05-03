import streamlit as st
import pandas as pd
import plotly.express as px

# Cargar el dataset
df = pd.read_csv('vehicles_us.csv')


# Encabezado
st.header("Análisis de Vehículos en Venta en EE.UU.")

# Botón para mostrar histograma
if st.button("Mostrar histograma de precios"):
    fig = px.histogram(df, x="price", nbins=50,
                       title="Distribución de Precios de Vehículos")
    st.plotly_chart(fig)
    st.write(
        "Este histograma muestra cómo se distribuyen los precios de los vehículos.")


# Botón para mostrar gráfico de dispersión
if st.button("Mostrar dispersión Año vs Precio"):
    fig2 = px.scatter(df, x="model_year", y="price",
                      title="Año del Modelo vs Precio", opacity=0.5)
    st.plotly_chart(fig2)
    st.write("Este gráfico muestra cómo varían los precios según el año del modelo.")
