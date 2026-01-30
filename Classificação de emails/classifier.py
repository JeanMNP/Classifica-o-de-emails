# classifier.py
import os
import re
from transformers import pipeline 

#Carregar pipeline de classificação 
classifier = pipeline("text-classification", model="pysentimiento/robertuito-sentiment-analysis")


def preprocess_text(text: str) -> str:
    text = text.lower()
    return text.strip()


def classify_email(text: str) -> str:
    result = classifier(text)[0]
    label = result["label"]  # Exemplo: "POS", "NEU", "NEG"

    if label in ["POS", "NEU"]:
        return "Produtivo"
    else:  # NEG
        return "Improdutivo"



def generate_response(category: str, email_text: str) -> str:
    if category == "Produtivo":

        return "Responderei assim que possivel"
    else:
        return "Agradecemos sua mensagem! Desejamos um ótimo dia."
