import streamlit as st

st.title("Aplicación de Conversiones")

# Conversiones de temperatura
st.header("Conversiones de temperatura")
with st.beta_expander("Conversiones de temperatura"):
    celsius = st.number_input("Celsius")
    fahrenheit = celsius * 9/5 + 32
    kelvin = celsius + 273.15
    st.write(f"{celsius} grados Celsius equivalen a {fahrenheit} grados Fahrenheit")
    st.write(f"{celsius} grados Celsius equivalen a {kelvin} grados Kelvin")

# Conversiones de longitud
st.header("Conversiones de longitud")
with st.beta_expander("Conversiones de longitud"):
    metros = st.number_input("Metros")
    pies = metros * 3.28084
    pulgadas = metros * 39.3701
    st.write(f"{metros} metros equivalen a {pies} pies")
    st.write(f"{metros} metros equivalen a {pulgadas} pulgadas")

# Conversiones de peso/masa
st.header("Conversiones de peso/masa")
with st.beta_expander("Conversiones de peso/masa"):
    libras = st.number_input("Libras")
    kilogramos = libras * 0.453592
    onzas = libras * 16
    st.write(f"{libras} libras equivalen a {kilogramos} kilogramos")
    st.write(f"{libras} libras equivalen a {onzas} onzas")

# Conversiones de volumen
st.header("Conversiones de volumen")
with st.beta_expander("Conversiones de volumen"):
    litros = st.number_input("Litros")
    galones = litros * 0.264172
    pulgadas_cubicas = litros * 61023.7
    st.write(f"{litros} litros equivalen a {galones} galones")
    st.write(f"{litros} litros equivalen a {pulgadas_cubicas} pulgadas cúbicas")

# Conversiones de tiempo
st.header("Conversiones de tiempo")
with st.beta_expander("Conversiones de tiempo"):
    horas = st.number_input("Horas")
    minutos = horas * 60
    dias = horas / 24
    st.write(f"{horas} horas equivalen a {minutos} minutos")
    st.write(f"{horas} horas equivalen a {dias} días")

# Conversiones de velocidad
st.header("Conversiones de velocidad")
with st.beta_expander("Conversiones de velocidad"):
    millas_por_hora = st.number_input("Millas por hora")
    kilometros_por_hora = millas_por_hora * 1.60934
    nudos = millas_por_hora * 0.868976
    st.write(f"{millas_por_hora} millas por hora equivalen a {kilometros_por_hora} kilómetros por hora")
    st.write(f"{millas_por_hora} millas por hora equivalen a {nudos} nudos")

# Conversiones de área
st.header("Conversiones de área")
with st.beta_expander("Conversiones de área"):
    metros_cuadrados = st.number_input("Metros cuadrados")
    pies_cuadrados = metros_cuadrados * 10.7639
    kilometros_cuadrados = metros_cuadrados / 1000000
    st.write(f"{metros_cuadrados} metros cuadrados equivalen a {pies_cuadrados} pies cuadrados")
    st.write(f"{metros_cuadrados} metros cuadrados equivalen a {kilometros_cuadrados} kilómetros cuadrados")

# Conversiones de energía
st.header("Conversiones de energía")
with st.beta_expander("Conversiones de energía"):
    julios = st.number_input("Julios")
    calorias = julios * 0.000239006
    kilovatios_hora = julios * 0.000000277778
    st.write(f"{julios} julios equivalen a {calorias} calorías")
    st.write(f"{julios} julios equivalen a {kilovatios_hora} kilovatios-hora")

# Conversiones de presión
st.header("Conversiones de presión")
with st.beta_expander("Conversiones de presión"):
    pascales = st.number_input("Pascales")
    atm = pascales * 0.00000986923
    bar = pascales * 0.00001
    st.write(f"{pascales} pascales equivalen a {atm} atmósferas")
    st.write(f"{pascales} pascales equivalen a {bar} bares")

# Conversiones de tamaño de datos
st.header("Conversiones de tamaño de datos")
with st.beta_expander("Conversiones de tamaño de datos"):
    megabytes = st.number_input("Megabytes")
    gigabytes = megabytes * 0.001
    kilobytes = megabytes * 1024
    terabytes = gigabytes * 0.001
    st.write(f"{megabytes} megabytes equivalen a {gigabytes} gigabytes")
    st.write(f"{megabytes} megabytes equivalen a {kilobytes} kilobytes")
    st.write(f"{gigabytes} gigabytes equivalen a {terabytes} terabytes")
```

Ahora cada categoría tiene una barra desplegable que puedes abrir para ver las conversiones específicas. Si necesitas más ayuda, ¡no dudes en preguntar!
