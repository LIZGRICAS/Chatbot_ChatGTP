import os
import openai
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key


def clasificar_texto(texto):
    categorias = [
        "arte",
        "ciencia",
        "deportes",
        "economia",
        "educacion",
        "entretenimiento",
        "medio ambiente",
        "politica",
        "salud",
        "tecnologia"
    ]
    prompt = f"Por favor clasifica el siguiente texto '{texto}' en una de estas categorias:{','.join(categorias)}"
    respuesta = openai.Complice.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        temperature=0.5,
        max_tokens=50
    )
    return respuesta.choices[0].text.strip()

texto_para_clasificar = input("Ingresar un texto: ")
clasificacion = clasificar_texto(texto_para_clasificar)
print(clasificacion)
