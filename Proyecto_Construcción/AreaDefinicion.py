import tkinter as tk
from tkinter import ttk

# Diccionario para mapear cada opción a una ruta
rutas_compendios = {
    "Salud": "/ruta/a/carpeta/salud",
    "Ingenieria, manufactura y construcción": "/ruta/a/carpeta/ingenieria",
    "Educación": "/ruta/a/carpeta/educacion",
    "Ciencias sociales, administración y derecho": "/ruta/a/carpeta/ciencias_sociales",
    "Artes y humanidades": "/ruta/a/carpeta/artes_humanidades",
    "Agronomia y veterinaria": "/ruta/a/carpeta/agronomia",
    "Ciencias naturales, exactas y de la computacion": "/ruta/a/carpeta/ciencias_naturales"
}

ruta_seleccionada_definicion = None

def abrir_area_definicion():
    def seleccionar_ruta_definicion():
        global ruta_seleccionada_definicion
        opcion = combo.get()
        if opcion in rutas_compendios:
            ruta_seleccionada_definicion = rutas_compendios[opcion]
            print(f"Ruta seleccionada para Definicion: {ruta_seleccionada_definicion}")  # Solo para verificación
        else:
            ruta_seleccionada_definicion = None
            print("No se ha seleccionado una opción válida")

    area_definicion = tk.Toplevel()
    area_definicion.title("Selección de Compendio")
    area_definicion.geometry("500x200")
    
    # Etiqueta
    label = tk.Label(area_definicion, text="Seleccione el compendio deseado:", font=("Arial", 12))
    label.pack(pady=20)
    
    # Crear un combobox
    combo = ttk.Combobox(area_definicion, values=["Seleccione una opción"] + list(rutas_compendios.keys()), state="readonly")
    combo.pack(pady=10)
    
    # Establecer valor predeterminado
    combo.current(0)

    # Botón para confirmar la selección
    boton_confirmar = tk.Button(area_definicion, text="Confirmar", command=seleccionar_ruta_definicion)
    boton_confirmar.pack(pady=10)
