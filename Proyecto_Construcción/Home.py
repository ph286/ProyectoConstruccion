import tkinter as tk
from AgregarPalabra import AgregarPalabra
from AreaPDF import abrir_area_pdf
from AreaDefinicion import abrir_area_definicion

# Función para crear una nueva instancia de AgregarPalabraVentana
def abrir_ventana_agregar_palabra(archivo, titulo):
    AgregarPalabra(archivo, titulo)
    
# Función para cerrar la aplicación
def salir():
    root.destroy()

# Crear la ventana principal
root = tk.Tk()
root.title("Bienvenido")

# Definir el tamaño de la ventana
ancho = 400
alto = 300

# Obtener el tamaño de la pantalla
pantalla_ancho = root.winfo_screenwidth()
pantalla_alto = root.winfo_screenheight()

# Calcular la posición centrada
posicion_x = (pantalla_ancho // 2) - (ancho // 2)
posicion_y = (pantalla_alto // 2) - (alto // 2)

# Establecer la geometría de la ventana
root.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")

# Barra de menú
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Menú "Opciones"
menu_opciones = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

feedback=tk.Menu(barra_menu,tearoff=0)
feedback.add_command(label="Apéndices", command=lambda: abrir_ventana_agregar_palabra('Compendios/listado_apendices.txt', "Agregar palabra a Apéndices"))
feedback.add_command(label="Palabras clave", command=lambda: abrir_ventana_agregar_palabra('listado_palabras_clave.txt', "Agregar palabra a Palabras Clave"))
feedback.add_command(label="Corpus", command=lambda: abrir_ventana_agregar_palabra('corpus_descartes.txt', "Agregar palabra a Corpus"))
feedback.add_command(label="Palabras a omitir", command=lambda: abrir_ventana_agregar_palabra('listado_palabras_omitir.txt', "Agregar palabra a Palabras a Omitir"))
feedback.add_command(label="Caracteres especiales", command=lambda: abrir_ventana_agregar_palabra('listado_caracteres.txt', "Agregar palabra a Caracteres especiales"))
menu_opciones.add_cascade(label="Feedback", menu=feedback)

menu_opciones.add_command(label="Salir", command=salir)

# Etiqueta de bienvenida
label_bienvenido = tk.Label(root, text="BIENVENIDO", font=("Arial", 24))
label_bienvenido.pack(pady=30)

# Botón para cargar PDF
boton_cargar_pdf = tk.Button(root, text="CARGAR PDF", font=("Arial", 14), command=abrir_area_pdf)
boton_cargar_pdf.pack(pady=10)

# Botón para buscar
boton_buscar = tk.Button(root, text="BUSCAR", font=("Arial", 14), command=abrir_area_definicion)
boton_buscar.pack(pady=10)

# Ejecutar el bucle principal de la aplicación
root.mainloop()
