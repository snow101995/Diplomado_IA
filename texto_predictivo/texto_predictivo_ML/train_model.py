# entrenar_modelo.py
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
import pandas as pd

# Corpus de ejemplo (puedes usar un dataset real con más palabras)
palabras = [
    "pato", "papa", "papel", "pared", "parque", "pasto", "pelota", "perro", "persona", "pantalla",
    "computadora", "comida", "cometa", "correr", "caminar", "carro", "casa", "cámara", "canción"
]

df = pd.DataFrame(palabras, columns=["palabra"])

# Vectorizamos las palabras
vectorizer = CountVectorizer(analyzer='char_wb', ngram_range=(2, 4))
X = vectorizer.fit_transform(df["palabra"])
y = df["palabra"]

# Entrenamos un modelo de clasificación (logistic regression)
model = LogisticRegression()
model.fit(X, y)

# Guardamos modelo y vectorizador
joblib.dump(model, "modelo_predictivo.pkl")
joblib.dump(vectorizer, "vectorizador.pkl")
