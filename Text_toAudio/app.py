import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
from openai import OpenAI

# Cargar variables de entorno
load_dotenv(find_dotenv(), override=True)
# Entorno Local
apiKey = os.environ.get('OPENAI_API_KEY')
#apiKey=
st.write("🔐 API Key cargada:", apiKey is not None)
client = OpenAI(api_key=apiKey)


# UI en Streamlit
st.title("🎙️ Generador de Audio con OpenAI")

# Entrada de texto
text = st.text_area("Ingrese el texto:", height=200)

# Selección de voz
voices = ["alloy", "echo", "fable", "onyx", "nova", "shimmer"]
voice = st.selectbox("Seleccione la voz:", voices)

# Botón para generar audio
if st.button("Generar Audio"):
    if text:
        response = client.audio.speech.create(
            model="tts-1",
            voice=voice,
            input=text
        )

        # Guardar el archivo de audio
        audio_path = "audio.mp3"
        with open(audio_path, "wb") as output_file:
            for chunk in response.iter_bytes():
                if chunk:
                    output_file.write(chunk)

        st.success(f"✅ Audio generado y guardado en `{audio_path}`")

        # Reproducir el audio
        audio_file = open(audio_path, "rb")
        audio_bytes = audio_file.read()
        st.audio(audio_bytes, format="audio/mp3")
    else:
        st.error("❗ Por favor, ingrese un texto.")
