import spacy
import pandas as pd

# Cargar el modelo de lenguaje en español de Spacy
nlp = spacy.load("es_core_news_sm")

archivo_palabras = "contextos_definitorios.txt"
archivo_descartes = "listado_descartes_corpus.txt"
archivo_texto = "TextoExtraido/oraciones_con_palabras.txt"
archivo_csv = "TextoExtraido/definiciones.csv"

# Leer palabras descartadas y convertirlas a minúsculas
with open(archivo_descartes, "r", encoding="utf-8") as archivo_descartes:
    palabras_descartes = set(archivo_descartes.read().lower().splitlines())

# Función para dividir el texto en oraciones
def dividir_en_oraciones(texto):
    oraciones = []
    inicio = 0
    for i, char in enumerate(texto):
        if char in ['.', '!', '?']:
            oracion = texto[inicio:i+1]
            oraciones.append(oracion.strip())
            inicio = i+1
    return oraciones

# Función para verificar si un sustantivo es válido
def es_sustantivo_valido(palabra):
    return len(palabra) > 1 and palabra.isalnum()

# Función para extraer sustantivos, adjetivos y preposiciones propias de una oración
def extraer_sustantivo_adjetivo_preposicion_propio(oracion):
    doc = nlp(oracion)
    conceptos = []
    concepto_actual = ""
    ultima_pos = ""
    
    for token in doc:
        if token.text.startswith("(") and token.text.endswith(")"):
            continue
        if token.text.lower() in palabras_descartes or not es_sustantivo_valido(token.text.lower()):
            continue 
        if token.pos_ in ["NOUN", "ADJ", "PROPN"]:
            if ultima_pos in ["NOUN", "ADJ", "PROPN"]:
                concepto_actual += " " + token.text
            else:
                concepto_actual = token.text
            ultima_pos = token.pos_
        elif token.pos_ == "ADP":
            if ultima_pos in ["NOUN", "PROPN"]:
                concepto_actual += " " + token.text
        else:
            if concepto_actual:
                conceptos.append(concepto_actual.strip())
                break  
            concepto_actual = ""
            ultima_pos = ""
    
    return conceptos

# Leer las palabras de contexto desde un archivo de texto
with open(archivo_palabras, "r", encoding="utf-8") as archivo_palabras:
    palabras = archivo_palabras.read().splitlines()

# Leer el texto desde un archivo de texto
with open(archivo_texto, "r", encoding="utf-8") as archivo_texto:
    texto = archivo_texto.read()

# Reemplazar saltos de línea por espacios
texto = texto.replace('\n', ' ')

# Dividir el texto en oraciones
oraciones = dividir_en_oraciones(texto)

conceptos_y_definiciones = []

# Iterar sobre cada palabra de contexto
for palabra in palabras:
    # Iterar sobre cada oración en el texto
    for oracion in oraciones:
        if palabra in oracion:
            definicion = oracion.split(palabra)[-1].strip()
            conceptos = extraer_sustantivo_adjetivo_preposicion_propio(oracion)
            for concepto in conceptos:
                conceptos_y_definiciones.append({"Concepto": concepto, "Definicion": definicion})

# Crear un DataFrame de pandas con los conceptos y definiciones
df = pd.DataFrame(conceptos_y_definiciones)

# Escribir el DataFrame en un archivo CSV
df.to_csv(archivo_csv, index=False, encoding="utf-8")