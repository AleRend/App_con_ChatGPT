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
    global users_df  # Mover la declaración global aquí
    if username in users_df["username"].values:
        user_row = users_df.loc[users_df["username"] == username]
        if user_row["password"].values[0] == password:
            return True
    return False

# Función para registrar un nuevo usuario
def register(username, password):
    global users_df  # Mover la declaración global aquí
    if username not in users_df["username"].values:
        new_user = pd.DataFrame({"username": [username], "password": [password], "calories": [0]})
        users_df = pd.concat([users_df, new_user], ignore_index=True)
        return True
    return False

# Función para obtener las calorías de un usuario
def get_calories(username):
    global users_df  # Mover la declaración global aquí
    return users_df.loc[users_df["username"] == username, "calories"].values[0]

# Función para registrar calorías consumidas
def log_calories(username, calories):
    global users_df  # Mover la declaración global aquí
    users_df.loc[users_df["username"] == username, "calories"] += calories

# Resto del código...
