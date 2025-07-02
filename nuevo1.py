import streamlit as st

# Título de la aplicación
st.title('Mi primera app con Streamlit')

# Texto de presentación
st.write('Bienvenido a esta aplicación sencilla.')

# Entrada de texto
nombre = st.text_input('Escribe tu nombre:')

# Mostrar saludo si el usuario escribe algo
if nombre:
    st.write(f'Hola, {nombre}! Encantado de saludarte.')

