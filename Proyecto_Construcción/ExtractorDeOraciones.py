archivo_palabras = "contextos_definitorios.txt"
archivo_texto = "TextoExtraido/texto_modificado.txt"
archivo_salida = "TextoExtraido/oraciones_con_palabras.txt"

def dividir_en_oraciones(texto):
    oraciones = []
    inicio = 0
    for i, char in enumerate(texto):
        if char in ['.', '!', '?', ':']:
            oracion = texto[inicio:i+1]
            oraciones.append(oracion.strip())
            inicio = i+1
    return oraciones

with open(archivo_palabras, "r", encoding="utf-8") as archivo_palabras:
    palabras = archivo_palabras.read().splitlines()

with open(archivo_texto, "r", encoding="utf-8") as archivo_texto:
    texto = archivo_texto.read()

texto = texto.replace('\n', ' ')

oraciones = dividir_en_oraciones(texto)

oraciones_con_palabras = []

for palabra in palabras:
    for oracion in oraciones:
        if palabra in oracion:
            oraciones_con_palabras.append(oracion)

with open(archivo_salida, "w", encoding="utf-8") as archivo_salida:
    for i, oracion in enumerate(oraciones_con_palabras):
        if oracion.strip():  
            archivo_salida.write(oracion.strip() + ".\n" if i < len(oraciones_con_palabras) - 1 else oracion.strip() + " ")