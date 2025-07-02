import streamlit as st

# Título de la aplicación
st.title('Beatriz se ríe de Streamlit')

# Texto de presentación
st.write('Pues, bienvenida a esta primera aplicación.')

# Entrada de texto
nombre = st.text_input('Dime tu nombre:')

# Mostrar saludo si el usuario escribe algo
if nombre:
    st.write(f'Hola, {nombre}! Eres genial.')

