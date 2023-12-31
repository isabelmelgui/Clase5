import streamlit as st
from PIL import Image

st.title("La aplicacion de Isabel")

st.header("En este espacio empiezo a desarrollar mis aplicaciones para interfaces multimodales.")
st.write("Facilmente puedo desarrollar backend y frontend")
image = Image.open('Plant2.png')

st.image(image, caption= 'Interfaces multimodales')


texto = st.text_input('Escribe algo', 'este es mi texto')
st.write('El texto escrito es:', texto)

st.subheader("Ahora usemos 2 columnas")

col1, col2 = st.columns(2)

with col1:
  st.subheader("Esta es la primera columna")
  st.write("Las interfaces multimodales mejoran la experiencia del usuario")
  resp = st.checkbox('Estoy de acuerdo')
  if resp:
    st.write('correcto!')

with col2:
  st.subheader("Esta es la segunda columna")
  modo = st.radio("que modalidad es la principal en tu interfaz", ('visual','auditiva', 'tactil'))
  if modo == 'visual':
    st.write('la vista es fundamental para tu interfaz')
  if modo == 'auditiva':
     st.write('la audicion es fundamental para tu interfaz')
  if modo == 'tactil':
     st.write('El tacto es fundamental para tu interfaz')

st.subheader("uso de botones")
if st.button('Presiona el boton'):
  st.write('Gracias por presionar')
else:
  st.write('No has presionado aún')


st.subheader("selectbox")
in_mod= st.selectbox(
  "selecciona la modalidad",
  ("audio", "visual", "háptico"),
)
if in_mod == "audio":
  set_mod = "Reproducir audio"
elif in_mod == "visual":
  set_mod = "Reproducir video"
elif in_mod == "háptico":
  set_mod = "Activar vibración"
st.write("la acción es: ", set_mod)
    
with st.sidebar:
  st.subheader("configura la modalidad")
  mod_radio = st.radio (
    "Escoge la modalidad a usar",
    ("visual", "auditiva", "háptica")
  )
