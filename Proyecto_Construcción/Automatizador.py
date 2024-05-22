import os
import subprocess
import shutil

class Main:
    def __init__(self):
        self.ruta_archivo_csv_salida = "TextoExtraido/definiciones_mejoradas.csv"
        self.ruta_carpeta_compendios = "Compendios"

    def ejecutar(self):
        self.extraer_pdf_a_texto()
        self.depurar_contenido()
        self.extraer_oraciones_con_palabras()
        self.extraer_definiciones()
        self.corregir_redaccion()
        self.limpiar_archivos()

    def extraer_pdf_a_texto(self):
        print("Ejecutando ExtractorDePDF.py...")
        subprocess.run(["python", "ExtractorDePDF.py"])
        print("ExtractorDePDF.py ejecutado exitosamente.")

    def depurar_contenido(self):
        print("Ejecutando DepuradorDeContenido.py...")
        subprocess.run(["python", "DepuradorDeContenido.py"])
        print("DepuradorDeContenido.py ejecutado exitosamente.")

    def extraer_oraciones_con_palabras(self):
        print("Ejecutando ExtractorDeOraciones.py...")
        subprocess.run(["python", "ExtractorDeOraciones.py"])
        print("ExtractorDeOraciones.py ejecutado exitosamente.")

    def extraer_definiciones(self):
        print("Ejecutando ExtractorDeDefiniciones.py...")
        subprocess.run(["python", "ExtractorDeDefiniciones.py"])
        print("ExtractorDeDefiniciones.py ejecutado exitosamente.")

    def corregir_redaccion(self):
        print("Ejecutando CorrectorDeRedaccion.py...")
        subprocess.run(["python", "CorrectorDeRedaccion.py"])
        print("CorrectorDeRedaccion.py ejecutado exitosamente.")

    def limpiar_archivos(self):
        # Crear la carpeta "Compendios" si no existe
        if not os.path.exists(self.ruta_carpeta_compendios):
            os.makedirs(self.ruta_carpeta_compendios)

        # Mover el archivo "definiciones_mejoradas.csv" a la carpeta "Compendios"
        shutil.move(self.ruta_archivo_csv_salida, os.path.join(self.ruta_carpeta_compendios, "definiciones_mejoradas.csv"))
        print(f"Archivo movido a la carpeta 'Compendios'")

        # Eliminar archivos restantes en "TextoExtraido"
        for archivo in os.listdir("TextoExtraido"):
            ruta_archivo = os.path.join("TextoExtraido", archivo)
            os.remove(ruta_archivo)
            print(f"Archivo eliminado: {ruta_archivo}")

# Instanciar y ejecutar la clase Main
if __name__ == "__main__":
    main = Main()
    main.ejecutar()
