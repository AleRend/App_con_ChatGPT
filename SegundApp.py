import streamlit as st

# Título de la aplicación
st.title("Conversor de Temperatura y Longitud")

# Lista de opciones para la categoría principal
main_categories = ["Temperatura", "Longitud"]
main_category = st.sidebar.radio("Seleccione una categoría principal:", main_categories)

# Lista de opciones para la conversión de temperatura
temp_options = ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"]

# Lista de opciones para la conversión de longitud
length_options = ["Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas"]

# Selección dinámica de las opciones de conversión dependiendo de la categoría principal
if main_category == "Temperatura":
    options = temp_options
elif main_category == "Longitud":
    options = length_options

# Selección de la conversión
conversion_option = st.sidebar.selectbox("Seleccione una conversión:", options)

# Entrada de usuario para la temperatura o longitud a convertir
input_value = st.sidebar.number_input("Ingrese el valor a convertir:", step=0.01)

# Realizar la conversión
if conversion_option == "Celsius a Fahrenheit":
    result = input_value * 9/5 + 32
elif conversion_option == "Fahrenheit a Celsius":
    result = (input_value - 32) * 5/9
elif conversion_option == "Celsius a Kelvin":
    result = input_value + 273.15
elif conversion_option == "Kelvin a Celsius":
    result = input_value - 273.15
elif conversion_option == "Pies a Metros":
    result = input_value * 0.3048
elif conversion_option == "Metros a Pies":
    result = input_value / 0.3048
elif conversion_option == "Pulgadas a Centímetros":
    result = input_value * 2.54
elif conversion_option == "Centímetros a Pulgadas":
    result = input_value / 2.54

# Mostrar el resultado
st.write("Resultado:", result)
