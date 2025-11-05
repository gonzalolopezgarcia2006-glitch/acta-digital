import streamlit as st

st.set_page_config(page_title="Acta Digital", page_icon="✍️")

st.title("✍️ Mi Acta Digital")
st.write("Esta es mi primera app web desplegada con Streamlit.")

# Ejemplo de campos
tema = st.text_input("Tema de la reunión:")
asistentes = st.text_area("Asistentes (uno por línea):")
acuerdos = st.text_area("Acuerdos y notas:")

if st.button("Generar Acta"):
    st.subheader("Acta Generada")
    st.write(f"**Tema:** {tema}")
    st.write("**Asistentes:**")
    st.code(asistentes)
    st.write("**Acuerdos:**")
    st.code(acuerdos)
