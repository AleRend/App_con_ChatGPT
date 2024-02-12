import streamlit as st

# Título de la aplicación
st.title("Conversor Universal")

# Lista de categorías y sus subcategorías de conversiones
categories = {
    "Temperatura": ["Celsius a Fahrenheit", "Fahrenheit a Celsius", "Celsius a Kelvin", "Kelvin a Celsius"],
    "Longitud": ["Pies a Metros", "Metros a Pies", "Pulgadas a Centímetros", "Centímetros a Pulgadas"],
    "Peso/Masa": ["Libras a Kilogramos", "Kilogramos a Libras", "Onzas a Gramos", "Gramos a Onzas"],
    "Volumen": ["Galones a Litros", "Litros a Galones", "Pulgadas cúbicas a Centímetros cúbicos", "Centímetros cúbicos a Pulgadas cúbicas"],
    "Tiempo": ["Horas a Minutos", "Minutos a Segundos", "Días a Horas", "Semanas a Días"],
    "Velocidad": ["Millas por hora a Kilómetros por hora", "Kilómetros por hora a Metros por segundo", "Nudos a Millas por hora", "Metros por segundo a Pies por segundo"],
    "Área": ["Metros cuadrados a Pies cuadrados", "Pies cuadrados a Metros cuadrados", "Kilómetros cuadrados a Millas cuadradas", "Millas cuadradas a Kilómetros cuadrados"],
    "Energía": ["Julios a Calorías", "Calorías a Kilojulios", "Kilovatios-hora a Megajulios", "Megajulios a Kilovatios-hora"],
    "Presión": ["Pascales a Atmósferas", "Atmósferas a Pascales", "Barras a Libras por pulgada cuadrada", "Libras por pulgada cuadrada a Bares"],
    "Tamaño de datos": ["Megabytes a Gigabytes", "Gigabytes a Terabytes", "Kilobytes a Megabytes", "Terabytes a Petabytes"]
}

# Selección de la categoría principal
main_category = st.sidebar.selectbox("Seleccione una categoría principal:", list(categories.keys()))

# Selección de la subcategoría
sub_category = st.sidebar.selectbox(f"Seleccione una subcategoría de {main_category}:", categories[main_category])

# Entrada de usuario para la cantidad a convertir
input_value = st.sidebar.number_input("Ingrese la cantidad a convertir:", step=0.01)

# Realizar la conversión
conversion_option = sub_category.split(" a ")
from_unit = conversion_option[0]
to_unit = conversion_option[-1]

# Realizar la conversión
if from_unit == "Celsius":
    if to_unit == "Fahrenheit":
        result = input_value * 9/5 + 32
    elif to_unit == "Kelvin":
        result = input_value + 273.15
    else:
        result = input_value
elif from_unit == "Fahrenheit":
    if to_unit == "Celsius":
        result = (input_value - 32) * 5/9
    elif to_unit == "Kelvin":
        result = (input_value - 32) * 5/9 + 273.15
    else:
        result = input_value
elif from_unit == "Kelvin":
    if to_unit == "Celsius":
        result = input_value - 273.15
    elif to_unit == "Fahrenheit":
        result = (input_value - 273.15) * 9/5 + 32
    else:
        result = input_value
elif from_unit == "Pies":
    if to_unit == "Metros":
        result = input_value * 0.3048
    elif to_unit == "Pulgadas":
        result = input_value * 12
    else:
        result = input_value
elif from_unit == "Metros":
    if to_unit == "Pies":
        result = input_value / 0.3048
    elif to_unit == "Pulgadas":
        result = input_value * 39.3701
    else:
        result = input_value
elif from_unit == "Pulgadas":
    if to_unit == "Pies":
        result = input_value / 12
    elif to_unit == "Metros":
        result = input_value * 0.0254
    else:
        result = input_value
elif from_unit == "Libras":
    if to_unit == "Kilogramos":
        result = input_value * 0.453592
    elif to_unit == "Onzas":
        result = input_value * 16
    else:
        result = input_value
elif from_unit == "Kilogramos":
    if to_unit == "Libras":
        result = input_value / 0.453592
    elif to_unit == "Onzas":
        result = input_value * 35.274
    else:
        result = input_value
elif from_unit == "Onzas":
    if to_unit == "Libras":
        result = input_value / 16
    elif to_unit == "Kilogramos":
        result = input_value / 35.274
    else:
        result = input_value
elif from_unit == "Galones":
    if to_unit == "Litros":
        result = input_value * 3.78541
    elif to_unit == "Pulgadas cúbicas":
        result = input_value * 231
    else:
        result = input_value
elif from_unit == "Litros":
    if to_unit == "Galones":
        result = input_value / 3.78541
    elif to_unit == "Pulgadas cúbicas":
        result = input_value * 61023.7
    else:
        result = input_value
elif from_unit == "Pulgadas cúbicas":
    if to_unit == "Galones":
        result = input_value / 231
    elif to_unit == "Litros":
        result = input_value / 61023.7
    else:
        result = input_value
elif from_unit == "Horas":
    if to_unit == "Minutos":
        result = input_value * 60
    elif to_unit == "Días":
        result = input_value / 24
    elif to_unit == "Semanas":
        result = input_value / 168
    else:
        result = input_value
elif from_unit == "Minutos":
    if to_unit == "Horas":
        result = input_value / 60
    elif to_unit == "Segundos":
        result = input_value * 60
    elif to_unit == "Días":
        result = input_value / 1440
    else:
        result = input_value
elif from_unit == "Días":
    if to_unit == "Horas":
        result = input_value * 24
    elif to_unit == "Minutos":
        result = input_value * 1440
    elif to_unit == "Semanas":
        result = input_value / 7
    else:
        result = input_value
elif from_unit == "Semanas":
    if to_unit == "Horas":
        result = input_value * 168
    elif to_unit == "Minutos":
        result = input_value * 10080
    elif to_unit == "Días":
        result = input_value * 7
    else:
        result = input_value
elif from_unit == "Millas por hora":
    if to_unit == "Kilómetros por hora":
        result = input_value * 1.60934
    elif to_unit == "Nudos":
        result = input_value * 0.868976
    elif to_unit == "Metros por segundo":
        result = input_value * 0.44704
    else:
        result = input_value
elif from_unit == "Kilómetros por hora":
    if to_unit == "Millas por hora":
        result = input_value / 1.60934
    elif to_unit == "Nudos":
        result = input_value / 1.852
    elif to_unit == "Metros por segundo":
        result = input_value / 3.6
    else:
        result = input_value
elif from_unit == "Nudos":
    if to_unit == "Millas por hora":
        result = input_value * 1.15078
    elif to_unit == "Kilómetros por hora":
        result = input_value * 1.852
    elif to_unit == "Metros por segundo":
        result = input_value * 0.514444
    else:
        result = input_value
elif from_unit == "Metros por segundo":
    if to_unit == "Millas por hora":
        result = input_value * 2.23694
    elif to_unit == "Kilómetros por hora":
        result = input_value * 3.6
    elif to_unit == "Nudos":
        result = input_value * 1.94384
    else:
        result = input_value
elif from_unit == "Metros cuadrados":
    if to_unit == "Pies cuadrados":
        result = input_value * 10.7639
    elif to_unit == "Kilómetros cuadrados":
        result = input_value / 1000000
    elif to_unit == "Millas cuadradas":
        result = input_value / 2589988.11
    else:
        result = input_value
elif from_unit == "Pies cuadrados":
    if to_unit == "Metros cuadrados":
        result = input_value / 10.7639
    elif to_unit == "Kilómetros cuadrados":
        result = input_value / 10763907.6
    elif to_unit == "Millas cuadradas":
        result = input_value / 27878399.2
    else:
        result = input_value
elif from_unit == "Kilómetros cuadrados":
    if to_unit == "Metros cuadrados":
        result = input_value * 1000000
    elif to_unit == "Pies cuadrados":
        result = input_value * 10763907.6
    elif to_unit == "Millas cuadradas":
        result = input_value * 0.386102
    else:
        result = input_value
elif from_unit == "Millas cuadradas":
    if to_unit == "Metros cuadrados":
        result = input_value * 2589988.11
    elif to_unit == "Pies cuadrados":
        result = input_value * 27878399.2
    elif to_unit == "Kilómetros cuadrados":
        result = input_value * 2.58999
    else:
        result = input_value
elif from_unit == "Julios":
    if to_unit == "Calorías":
        result = input_value * 0.239006
    elif to_unit == "Kilojulios":
        result = input_value / 1000
    elif to_unit == "Megajulios":
        result = input_value / 1000000
    else:
        result = input_value
elif from_unit == "Calorías":
    if to_unit == "Julios":
        result = input_value * 4.184
    elif to_unit == "Kilojulios":
        result = input_value / 239.006
    elif to_unit == "Megajulios":
        result = input_value / 239000
    else:
        result = input_value
elif from_unit == "Kilovatios-hora":
    if to_unit == "Julios":
        result = input_value * 3600000
    elif to_unit == "Calorías":
        result = input_value * 859845.227859
    elif to_unit == "Megajulios":
        result = input_value * 3.6
    else:
        result = input_value
elif from_unit == "Megajulios":
    if to_unit == "Julios":
        result = input_value * 1000000
    elif to_unit == "Calorías":
        result = input_value * 238845.896627495
    elif to_unit == "Kilovatios-hora":
        result = input_value / 3.6
    else:
        result = input_value
elif from_unit == "Pascales":
    if to_unit == "Atmósferas":
        result = input_value * 0.00000986923
    elif to_unit == "Bares":
        result = input_value * 0.00001
    elif to_unit == "Libras por pulgada cuadrada":
        result = input_value * 0.000145038
    else:
        result = input_value
elif from_unit == "Atmósferas":
    if to_unit == "Pascales":
        result = input_value / 0.00000986923
    elif to_unit == "Bares":
        result = input_value * 1.01325
    elif to_unit == "Libras por pulgada cuadrada":
        result = input_value * 14.6959
    else:
        result = input_value
elif from_unit == "Bares":
    if to_unit == "Pascales":
        result = input_value / 0.00001
    elif to_unit == "Atmósferas":
        result = input_value / 1.01325
    elif to_unit == "Libras por pulgada cuadrada":
        result = input_value * 14.5038
    else:
        result = input_value
elif from_unit == "Libras por pulgada cuadrada":
    if to_unit == "Pascales":
        result = input_value / 0.000145038
    elif to_unit == "Atmósferas":
        result = input_value / 14.6959
    elif to_unit == "Bares":
        result = input_value / 14.5038
    else:
        result = input_value
elif from_unit == "Megabytes":
    if to_unit == "Gigabytes":
        result = input_value / 1024
    elif to_unit == "Terabytes":
        result = input_value / (1024 ** 2)
    elif to_unit == "Kilobytes":
        result = input_value * 1024
    else:
        result = input_value
elif from_unit == "Gigabytes":
    if to_unit == "Megabytes":
        result = input_value * 1024
    elif to_unit == "Terabytes":
        result = input_value / 1024
    elif to_unit == "Petabytes":
        result = input_value / (1024 ** 2)
    else:
        result = input_value
elif from_unit == "Terabytes":
    if to_unit == "Megabytes":
        result = input_value * (1024 ** 2)
    elif to_unit == "Gigabytes":
        result = input_value * 1024
    elif to_unit == "Petabytes":
        result = input_value / 1024
    else:
        result = input_value
elif from_unit == "Kilobytes":
    if to_unit == "Megabytes":
        result = input_value / 1024
    elif to_unit == "Gigabytes":
        result = input_value / (1024 ** 2)
    elif to_unit == "Terabytes":
        result = input_value / (1024 ** 3)
    else:
        result = input_value

# Mostrar el resultado centrado
st.write("Resultado:", result)
