import streamlit as st
import pandas as pd

# Definir datos de usuarios (simulados)
users_data = {
    "username": ["user1", "user2"],
    "password": ["password1", "password2"],
    "calories": [0, 0]
}
users_df = pd.DataFrame(users_data)

# Función para el inicio de sesión
def login(username, password):
    if username in users_df["username"].values:
        user_row = users_df.loc[users_df["username"] == username]
        if user_row["password"].values[0] == password:
            return True
    return False

# Función para registrar un nuevo usuario
def register(username, password):
    if username not in users_df["username"].values:
        new_user = pd.DataFrame({"username": [username], "password": [password], "calories": [0]})
        global users_df
        users_df = pd.concat([users_df, new_user], ignore_index=True)
        return True
    return False


# Función para obtener las calorías de un usuario
def get_calories(username):
    return users_df.loc[users_df["username"] == username, "calories"].values[0]

# Función para registrar calorías consumidas
def log_calories(username, calories):
    users_df.loc[users_df["username"] == username, "calories"] += calories

# Página de inicio de sesión
def login_page():
    st.title("Inicio de Sesión")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Iniciar Sesión"):
        if login(username, password):
            st.success(f"Bienvenido, {username}!")
            return username
        else:
            st.error("Usuario o contraseña incorrectos")

# Página de registro
def register_page():
    st.title("Registro")
    username = st.text_input("Usuario")
    password = st.text_input("Contraseña", type="password")
    if st.button("Registrar"):
        if register(username, password):
            st.success("Usuario registrado correctamente")
        else:
            st.error("El usuario ya existe")

# Página principal
def main_page(username):
    st.title("Registro de Calorías")
    st.write(f"Bienvenido, {username}!")
    calories = st.number_input("Calorías consumidas hoy", value=0, step=1)
    if st.button("Registrar Calorías"):
        log_calories(username, calories)
        st.success("Calorías registradas correctamente")
    st.write(f"Total de calorías consumidas hoy: {get_calories(username)}")

# App
def main():
    st.sidebar.title("Menú")
    page = st.sidebar.selectbox("Selecciona una opción", ["Inicio de Sesión", "Registro"])

    if page == "Inicio de Sesión":
        username = login_page()
        if username:
            main_page(username)
    elif page == "Registro":
        register_page()

if __name__ == "__main__":
    main()
