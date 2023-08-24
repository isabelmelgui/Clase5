import streamlit as st
from PIL import Image

st.title("La aplicacion de Isabel")

st.header("En este espacio empiezo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo desarrollar backend y frontend")
image = Image.open('Plant2.png')

st.image(image, caption= 'Interfaces multimodales')


texto = st.text_input('shakira shakira', 'este es mi texto')
st.write('El texto escrito es', texto)
