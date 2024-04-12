import streamlit as st
import pandas as pd
import geopandas as gpd
import numpy as np

def main():
    st.title("Calculadora Sencilla con Pandas y GeoPandas")

    num1 = st.number_input("Ingresa el primer número:", step=1)
    num2 = st.number_input("Ingresa el segundo número:", step=1)

    operation = st.selectbox("Selecciona la operación:", ["Suma", "Resta", "Multiplicación", "División"])

    if st.button("Calcular"):
        result = calculate(num1, num2, operation)
        st.success("Resultado:")
        st.write(create_dataframe(result))

def calculate(num1, num2, operation):
    if operation == "Suma":
        return num1 + num2
    elif operation == "Resta":
        return num1 - num2
    elif operation == "Multiplicación":
        return num1 * num2
    elif operation == "División":
        if num2 == 0:
            return "Error: División por cero"
        else:
            return num1 / num2

def create_dataframe(result):
    data = {"Resultado": [result]}
    df = pd.DataFrame(data)
    
    # Creamos un DataFrame geoespacial con coordenadas aleatorias
    np.random.seed(0)
    points = gpd.GeoDataFrame(geometry=gpd.points_from_xy(np.random.uniform(-180, 180, 10), np.random.uniform(-90, 90, 10)))
    
    return df, points

if __name__ == "__main__":
    main()
