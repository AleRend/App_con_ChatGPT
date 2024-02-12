import streamlit as st

# Título de la aplicación
st.title("Conversor de Temperatura y Longitud")

# Opciones para la conversión de temperatura
temp_option = st.selectbox(
    "Seleccione una conversión de temperatura:",
    ("Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius")
)

# Opciones para la conversión de longitud
length_option = st.selectbox(
    "Seleccione una conversión de longitud:",
    ("Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas")
)

# Entrada de usuario para la temperatura o longitud a convertir
input_value = st.number_input("Ingrese el valor a convertir:", step=0.01)

# Realizar la conversión
if temp_option == "Celsius a Fahrenheit":
    result = input_value * 9/5 + 32
elif temp_option == "Fahrenheit a Celsius":
    result = (input_value - 32) * 5/9
elif temp_option == "Celsius a Kelvin":
    result = input_value + 273.15
elif temp_option == "Kelvin a Celsius":
    result = input_value - 273.15
elif length_option == "Pies a Metros":
    result = input_value * 0.3048
elif length_option == "Metros a Pies":
    result = input_value / 0.3048
elif length_option == "Pulgadas a Centímetros":
    result = input_value * 2.54
elif length_option == "Centímetros a Pulgadas":
    result = input_value / 2.54

# Mostrar el resultado
st.write("Resultado:", result)
