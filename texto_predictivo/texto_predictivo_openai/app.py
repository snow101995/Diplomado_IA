import streamlit as st
from langchain_openai import ChatOpenAI
import os

# Cargar API KEY
openai_api_key = st.secrets.get("OPENAI_API_KEY", os.getenv("OPENAI_API_KEY"))
llm = ChatOpenAI(model="gpt-4", openai_api_key=openai_api_key)

st.title("🧠 Completador de Texto Predictivo")
st.write("Escribe el inicio de una palabra o frase, y el modelo te sugerirá posibles continuaciones.")

# Entrada de texto del usuario
input_text = st.text_input("Escribe algo... (por ejemplo: pa, elef, compu):", max_chars=30)

# Si hay texto ingresado, procesar
if input_text:
    prompt = (
        f"Actúa como un sistema de autocompletado. "
        f"El usuario ha comenzado a escribir '{input_text}' "
        f"y tú debes sugerir 5 posibles palabras o frases completas que comiencen así. "
        f"Solo responde con una lista separada por comas."
    )

    response = llm.invoke(prompt)
    suggestions = [s.strip() for s in response.content.split(",")]

    st.subheader("🔮 Sugerencias de completado:")
    for i, word in enumerate(suggestions, 1):
        st.write(f"{i}. {word}")
