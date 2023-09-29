import os
import openai
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key


def traducir_texto(texto, idioma):
    prompt = f"traduce el texto'{texto}' al {idioma}."
    respuesta = openai.Complice.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        temperature=0.5,
        max_tokens=1000
    )
    return respuesta.choices[0].text.strip()


mi_texto = input("escribe el texto que quieres traducir: ")
mi_idioma = input("A que idioma lo que quieres traducir: ")
traduccion = traducir_texto(mi_texto, mi_idioma)
print(traduccion)