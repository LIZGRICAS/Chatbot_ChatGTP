import os
import openai
import spacy
from dotenv import load_dotenv


load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')

openai.api_key = api_key

modelo = "text-davinci-002"
prompt = "¿cual es la capital de Francia"

respuesta = openai.Completion.create(
    #2 parametros obligatorios
    engine=modelo,
    prompt=prompt,
    #ajusta el numero de respuesta
    n=1,
    #nivel de respuesta mas o menos elebarada
    temperature=1,
    max_tokens=100
)

#Paso 3 respuesta generada
texto_generado = respuesta.choices[0].text.strip()
print(texto_generado)

print("***")

# biblioteca de analisis de texto
modelo_spacy = spacy.load("es_core_news_md")
analisis = modelo_spacy(texto_generado)

#ej 1
for ent in analisis.ents:
    print(ent.text, ent.label_)

#ej2
ubicacion = None
for ent in analisis.ents:
    if ent.label_=="LOC":
        ubicacion = ent
        break


