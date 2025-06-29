import streamlit as st
from langchain_openai import ChatOpenAI
import os

# ===== CARGAR API KEY =====
api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
llm = ChatOpenAI(model="gpt-4o", openai_api_key=api_key)

# ===== INTERFAZ =====
st.title("🧠 Autocompletador de Texto")
st.markdown("Empieza a escribir una palabra o frase y te sugeriremos posibles completaciones.")

user_input = st.text_input("🔤 Escribe aquí:", "")

# ===== FUNCIÓN DE AUTOCOMPLETADO =====
def generar_sugerencias(prefijo):
    prompt = (
        f"Actúa como un modelo de autocompletado. Dado el prefijo '{prefijo}', "
        f"genera 5 posibles completaciones de palabras o frases que comiencen así. "
        f"Responde solo con las sugerencias separadas por comas, sin explicaciones."
    )
    try:
        response = llm.invoke(prompt)
        return [s.strip() for s in response.content.split(",")]
    except Exception as e:
        st.error(f"❌ Error al obtener sugerencias: {e}")
        return []

# ===== LÓGICA DE LA APP =====
if len(user_input) >= 2:
    with st.spinner("Pensando..."):
        sugerencias = generar_sugerencias(user_input)
        if sugerencias:
            seleccion = st.selectbox("🔮 Sugerencias:", sugerencias)
            st.success(f"✅ Seleccionaste: {seleccion}")
else:
    st.info("💡 Escribe al menos 2 letras para ver sugerencias.")

