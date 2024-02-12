import streamlit as st

def main():
    st.title("Conversor Universal")

    category = st.sidebar.selectbox("Selecciona una categoría:", [
        "Temperatura",
        "Longitud",
        "Peso/Masa",
        "Volumen",
        "Tiempo",
        "Velocidad",
        "Área",
        "Energía",
        "Presión",
        "Tamaño de datos"
    ])

    if category == "Temperatura":
        temperature_converter()
    elif category == "Longitud":
        length_converter()
    elif category == "Peso/Masa":
        weight_converter()
    elif category == "Volumen":
        volume_converter()
    elif category == "Tiempo":
        time_converter()
    elif category == "Velocidad":
        speed_converter()
    elif category == "Área":
        area_converter()
    elif category == "Energía":
        energy_converter()
    elif category == "Presión":
        pressure_converter()
    elif category == "Tamaño de datos":
        data_size_converter()

def temperature_converter():
    st.subheader("Conversiones de temperatura")
    temp_from = st.selectbox("Desde:", ["Celsius", "Fahrenheit", "Kelvin"])
    temp_to = st.selectbox("A:", ["Celsius", "Fahrenheit", "Kelvin"])
    temp_input = st.number_input("Ingrese el valor a convertir:")
    converted_temp = convert_temperature(temp_input, temp_from, temp_to)
    st.write(f"{temp_input} {temp_from} equivale a {converted_temp:.2f} {temp_to}")

def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value + 459.67) * 5/9
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value * 9/5) - 459.67

def length_converter():
    st.subheader("Conversiones de longitud")
    length_from = st.selectbox("Desde:", ["Pies", "Metros", "Pulgadas", "Centímetros"])
    length_to = st.selectbox("A:", ["Pies", "Metros", "Pulgadas", "Centímetros"])
    length_input = st.number_input("Ingrese el valor a convertir:")
    converted_length = convert_length(length_input, length_from, length_to)
    st.write(f"{length_input} {length_from} equivale a {converted_length:.2f} {length_to}")

def convert_length(value, from_unit, to_unit):
    conversion_factors = {
        "Pies": {"Metros": 0.3048, "Pulgadas": 12, "Centímetros": 30.48},
        "Metros": {"Pies": 3.28084, "Pulgadas": 39.3701, "Centímetros": 100},
        "Pulgadas": {"Pies": 0.0833333, "Metros": 0.0254, "Centímetros": 2.54},
        "Centímetros": {"Pies": 0.0328084, "Metros": 0.01, "Pulgadas": 0.393701}
    }
    return value * conversion_factors[from_unit][to_unit]

def weight_converter():
    st.subheader("Conversiones de peso/masa")
    # Completa con la implementación de la conversión de peso/masa

def volume_converter():
    st.subheader("Conversiones de volumen")
    # Completa con la implementación de la conversión de volumen

def time_converter():
    st.subheader("Conversiones de tiempo")
    # Completa con la implementación de la conversión de tiempo

def speed_converter():
    st.subheader("Conversiones de velocidad")
    # Completa con la implementación de la conversión de velocidad

def area_converter():
    st.subheader("Conversiones de área")
    # Completa con la implementación de la conversión de área

def energy_converter():
    st.subheader("Conversiones de energía")
    # Completa con la implementación de la conversión de energía

def pressure_converter():
    st.subheader("Conversiones de presión")
    # Completa con la implementación de la conversión de presión

def data_size_converter():
    st.subheader("Conversiones de tamaño de datos")
    # Completa con la implementación de la conversión de tamaño de datos

if __name__ == "__main__":
    main()
