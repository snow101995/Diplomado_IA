import streamlit as st
from langchain_openai import ChatOpenAI
import os

# Cargar API Key
api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
llm = ChatOpenAI(model="gpt-4o", openai_api_key=api_key)

# Título
st.title("🧠 Autocompletador Texto")

# Entrada de texto sin necesidad de Enter
user_input = st.text_input("Empieza a escribir una palabra o frase...", "")

# Solo si hay más de 2 letras
if len(user_input) >= 2:
    with st.spinner("Pensando..."):
        prompt = (
            f"Dado el prefijo '{user_input}', sugiéreme 5 posibles completaciones "
            f"de palabras o frases que comiencen así. Respóndelas separadas por comas."
        )
        response = llm.invoke(prompt)
        suggestions = [s.strip() for s in response.content.split(",")]

        seleccion = st.selectbox("🔮 Sugerencias:", suggestions)
        st.success(f"Seleccionaste: {seleccion}")
else:
    st.info("Empieza a escribir para ver sugerencias...")
