import streamlit as st

st.title("Aplicación de Conversiones")

# Conversiones de temperatura
st.header("Conversiones de temperatura")
celsius = st.number_input("Ingrese grados Celsius")
fahrenheit = celsius * 9/5 + 32
st.write(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")

# Conversiones de longitud
st.header("Conversiones de longitud")
metros = st.number_input("Ingrese metros")
pies = metros * 3.28084
st.write(f"{metros} metros equivalen a {pies} pies")

# Conversiones de peso/masa
st.header("Conversiones de peso/masa")
libras = st.number_input("Ingrese libras")
kilogramos = libras * 0.453592
st.write(f"{libras} libras equivalen a {kilogramos} kilogramos")

# Conversiones de volumen
st.header("Conversiones de volumen")
litros = st.number_input("Ingrese litros")
galones = litros * 0.264172
st.write(f"{litros} litros equivalen a {galones} galones")

# Conversiones de tiempo
st.header("Conversiones de tiempo")
horas = st.number_input("Ingrese horas")
minutos = horas * 60
st.write(f"{horas} horas equivalen a {minutos} minutos")

# Conversiones de velocidad
st.header("Conversiones de velocidad")
millas_por_hora = st.number_input("Ingrese millas por hora")
kilometros_por_hora = millas_por_hora * 1.60934
st.write(f"{millas_por_hora} millas por hora equivalen a {kilometros_por_hora} kilómetros por hora")

# Conversiones de área
st.header("Conversiones de área")
metros_cuadrados = st.number_input("Ingrese metros cuadrados")
pies_cuadrados = metros_cuadrados * 10.7639
st.write(f"{metros_cuadrados} metros cuadrados equivalen a {pies_cuadrados} pies cuadrados")

# Conversiones de energía
st.header("Conversiones de energía")
julios = st.number_input("Ingrese julios")
calorias = julios * 0.000239006
st.write(f"{julios} julios equivalen a {calorias} calorías")

# Conversiones de presión
st.header("Conversiones de presión")
pascales = st.number_input("Ingrese pascales")
atmosferas = pascales * 0.00000986923
st.write(f"{pascales} pascales equivalen a {atmosferas} atmósferas")

# Conversiones de tamaño de datos
st.header("Conversiones de tamaño de datos")
megabytes = st.number_input("Ingrese megabytes")
gigabytes = megabytes * 0.001
st.write(f"{megabytes} megabytes equivalen a {gigabytes} gigabytes")
