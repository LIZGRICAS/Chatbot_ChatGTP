import os
import openai
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key

def crear_contenido(tema, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Porfavor escribe un articulo corto sobre: {tema}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=temperatura,
        max_tokens=tokens
    )
    return respuesta.choices[0].text.strip()

def resumir_text(texto, tokens, temperatura, modelo="text-davinci-002"):
    prompt = f"Porfavor resume el siguiente texto: {texto}\n\n"
    respuesta = openai.Completion.create(
        engine=modelo,
        prompt=prompt,
        n=1,
        temperature=temperatura,
        max_tokens=tokens
    )
    return respuesta.choices[0].text.strip()

tema= input("Elija un tema para tu articulo: ")
tokens = int(input("Cuántos tokens máximos tendrá tu articulo:"))
temperatura = int(input("Del 1 al 10, que tan creativo quieres que sea tu articulo?:"))/10
articulo_creado = crear_contenido(tema, tokens, temperatura)
print(articulo_creado)