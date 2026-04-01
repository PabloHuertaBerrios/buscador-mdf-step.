import streamlit as st

# Configuración de la página
st.set_page_config(page_title="Buscador MDF STEP", page_icon="💻", layout="wide")

# Título corporativo
st.title("💻 BUSCADOR MDF STEP C.I")
st.markdown("*Gerencia: Supply Chain | Departamento: Logística Internacional*")
st.markdown("---")

# Mensaje de éxito temporal
st.success("🎉 ¡Felicitaciones Pablo! La página web está viva y funcionando en internet.")

# Cajas de prueba para que veas cómo se verá
col1, col2 = st.columns(2)
with col1:
    st.text_area("📋 Pegue las PO(s) aquí:", height=150)
    st.button("🔍 Buscar PO")
with col2:
    st.text_area("📦 Pegue los SKU(s) aquí:", height=150)
    st.button("🔍 Buscar SKU")
