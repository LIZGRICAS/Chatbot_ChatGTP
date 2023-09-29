import os
import openai
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key

#funcion
def analizar_sentimientos(texto):
    prompt = f"Por favor, analizar el sentimiento predominante en el siguiente texto: '{texto}'. El sentimiento es:"
    respuesta = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        n=1,
        temperature=0.5,
        max_tokens=100
    )
    return respuesta.choices[0].text.strip()

#dinámica del chat

texto_para_analizar = input("Ingresa un texto")
sentimiento = analizar_sentimientos(texto_para_analizar)
print(sentimiento)
