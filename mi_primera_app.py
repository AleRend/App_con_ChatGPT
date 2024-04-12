import streamlit as st

def main():
    st.title("Calculadora Sencilla")

    num1 = st.number_input("Ingresa el primer número:", step=1)
    num2 = st.number_input("Ingresa el segundo número:", step=1)

    operation = st.selectbox("Selecciona la operación:", ["Suma", "Resta", "Multiplicación", "División"])

    if st.button("Calcular"):
        result = calculate(num1, num2, operation)
        st.success(f"El resultado de {num1} {operation.lower()} {num2} es: {result}")

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

if __name__ == "__main__":
    main()
