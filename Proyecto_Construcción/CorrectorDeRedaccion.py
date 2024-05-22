import csv
import sys

# Ajustar el límite del tamaño de campo del CSV al tamaño máximo permitido del sistema operativo
csv.field_size_limit(sys.maxsize)

# Lista de palabras consideradas errores
errores = ["en", "de", "la", "por", "vía"]

# Rutas de los archivos CSV de entrada y salida
archivo_csv_entrada = "TextoExtraido/definiciones.csv"
archivo_csv_salida = "TextoExtraido/definiciones_mejoradas.csv"

# Función para mejorar la redacción de una fila del CSV
def mejorar_redaccion(entrada):
    concepto, definicion = entrada
    # Separar las palabras del concepto
    palabras_concepto = concepto.strip().split()
    # Eliminar la última palabra si está en la lista de errores
    if palabras_concepto[-1].lower() in errores:
        concepto = ' '.join(palabras_concepto[:-1])
    # Capitalizar el concepto y añadir un espacio al final
    concepto = concepto.capitalize() + " "
    # Separar las palabras de la definición
    palabras_definicion = definicion.strip().split()
    # Eliminar la primera letra de la definición si es una sola letra (y no es un número)
    if len(palabras_definicion) > 1 and len(palabras_definicion[0]) == 1 and not palabras_definicion[0].isnumeric():
        definicion = ' '.join(palabras_definicion[1:])
    # Formatear la definición con comillas dobles al inicio y al final
    definicion = f'"{definicion.strip()}"'
    return concepto, definicion

# Función principal del programa
def main():
    filas_mejoradas = []
    # Abrir el archivo CSV de entrada
    with open(archivo_csv_entrada, newline='', encoding='utf-8') as csvfile:
        lector_csv = csv.reader(csvfile)
        # Iterar sobre cada fila del archivo CSV
        for fila in lector_csv:
            # Mejorar la redacción de la fila y agregarla a la lista de filas mejoradas
            fila_mejorada = mejorar_redaccion(fila)
            filas_mejoradas.append(fila_mejorada)

    # Escribir las filas mejoradas en un nuevo archivo CSV
    with open(archivo_csv_salida, mode='w', newline='', encoding='utf-8') as csvfile:
        escritor_csv = csv.writer(csvfile)
        for fila in filas_mejoradas:
            escritor_csv.writerow(fila)

# Verificar si este script es el archivo principal que se está ejecutando
if __name__ == "__main__":
    # Llamar a la función principal
    main()