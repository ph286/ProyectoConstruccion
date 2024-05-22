import re

def cargar_palabras_desde_archivo(ruta_archivo):
    """
    Carga palabras desde un archivo de texto y las devuelve como una lista.

    Args:
        ruta_archivo (str): Ruta del archivo de texto.

    Returns:
        list: Lista de palabras cargadas desde el archivo.
    """
    try:
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            palabras = [line.strip('" \n') for line in archivo]
        return palabras
    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo en la ruta: {ruta_archivo}")
        return []

def generar_patron_omitidas(palabras):
    """
    Genera un patrón para omitir palabras específicas en un texto.

    Args:
        palabras (list): Lista de palabras a omitir.

    Returns:
        re.Pattern: Patrón compilado para omitir las palabras.
    """
    # Escapar los caracteres especiales en las palabras antes de unir el patrón
    palabras_escaped = [re.escape(palabra) for palabra in palabras]
    patron = r'\b(?:' + '|'.join(palabras_escaped) + r')\b'
    return re.compile(patron, re.IGNORECASE | re.UNICODE)

def omitir_numeros(texto):
    """
    Omitir números en el texto, excepto aquellos seguidos de "cm".

    Args:
        texto (str): Texto de entrada.

    Returns:
        str: Texto con los números omitidos, excepto los seguidos de "cm".
    """
    def reemplazar(match):
        numero = match.group(0)
        if not numero.endswith(" cm"):
            return ""
        return numero

    return re.sub(r'\d+-\d+(?!\s*cm)', reemplazar, texto)

def limpiar_texto(contenido, palabras_clave, palabras_omitidas, caracteres_sin_valor, apendices):
    """
    Limpia el texto eliminando párrafos con palabras clave, palabras omitidas, caracteres sin valor,
    apéndices y números no seguidos de "cm".

    Args:
        contenido (str): Texto de entrada.
        palabras_clave (list): Lista de palabras clave.
        palabras_omitidas (list): Lista de palabras a omitir.
        caracteres_sin_valor (list): Lista de caracteres sin valor.
        apendices (list): Lista de apéndices.

    Returns:
        str: Texto limpio.
    """
    contenido_modificado = []
    for parrafo in contenido.split('\n\n'):
        if not any(palabra_clave in parrafo.lower() for palabra_clave in palabras_clave):
            contenido_modificado.append(parrafo)

    contenido = '\n\n'.join(contenido_modificado)
    patron_omitidas = generar_patron_omitidas(palabras_omitidas)
    contenido = re.sub(patron_omitidas, '', contenido)
    for caracter in caracteres_sin_valor:
        contenido = contenido.replace(caracter, '')
    for apendice in apendices:
        contenido = re.sub(r'\([^)]*' + re.escape(apendice) + r'[^)]*\)', '', contenido)
    contenido = omitir_numeros(contenido)
    return contenido

def procesar_archivo(archivo_entrada, archivo_salida, palabras_clave, palabras_omitidas, caracteres_sin_valor, apendices):
    """
    Procesa un archivo de texto, aplica limpieza y escribe el resultado en otro archivo.

    Args:
        archivo_entrada (str): Ruta del archivo de entrada.
        archivo_salida (str): Ruta del archivo de salida.
        palabras_clave (list): Lista de palabras clave.
        palabras_omitidas (list): Lista de palabras a omitir.
        caracteres_sin_valor (list): Lista de caracteres sin valor.
        apendices (list): Lista de apéndices.
    """
    try:
        with open(archivo_entrada, 'r', encoding='utf-8') as archivo_entrada:
            contenido = archivo_entrada.read()
        contenido_modificado = limpiar_texto(contenido, palabras_clave, palabras_omitidas, caracteres_sin_valor, apendices)
        with open(archivo_salida, 'w', encoding='utf-8') as archivo_salida:
            archivo_salida.write(contenido_modificado)
        print("Archivo copiado y palabras/caracteres sin valor/apéndices/numeros/párrafos con palabras clave omitidos exitosamente.")

    except FileNotFoundError:
        print(f"No se pudo encontrar el archivo en la ruta: {archivo_entrada}")

    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")

ruta_archivo_texto = "TextoExtraido/texto_extraido.txt"
ruta_archivo_salida = "TextoExtraido/texto_modificado.txt"
ruta_palabras_clave = "listado_palabras_clave.txt"
ruta_palabras_omitidas = "listado_palabras_a_omitir.txt"
ruta_caracteres_sin_valor = "listado_caracteres.txt"
ruta_apendices = "listado_apendices.txt"

palabras_clave = cargar_palabras_desde_archivo(ruta_palabras_clave)
palabras_omitidas = cargar_palabras_desde_archivo(ruta_palabras_omitidas)
caracteres_sin_valor = cargar_palabras_desde_archivo(ruta_caracteres_sin_valor)
apendices = cargar_palabras_desde_archivo(ruta_apendices)

procesar_archivo(ruta_archivo_texto, ruta_archivo_salida, palabras_clave, palabras_omitidas, caracteres_sin_valor, apendices)