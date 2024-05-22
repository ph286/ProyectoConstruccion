import tkinter as tk
from tkinter import filedialog, messagebox, Menu
from ExtractorDePDF import convertir_pdf_a_texto

# Variable global para almacenar la ruta del archivo PDF seleccionado
ruta_archivo_pdf = None

# Función para seleccionar el archivo PDF usando Tkinter
def seleccionar_archivo_pdf():
    global ruta_archivo_pdf
    ruta_archivo_pdf = filedialog.askopenfilename(filetypes=[("Archivos PDF", "*.pdf")])
    if ruta_archivo_pdf:
        etiqueta_archivo.config(text=f"Archivo seleccionado: {ruta_archivo_pdf}")
    else:
        messagebox.showinfo("Información", "No se seleccionó ningún archivo.")

# Función para cerrar la aplicación
def salir():
    root.destroy()

# Crear la interfaz gráfica
root = tk.Tk()
root.title("PROYECTO CONSTRUCCION")
root.geometry("500x200")

# Centrar la ventana en la pantalla
root.update_idletasks()
ancho_ventana = root.winfo_width()
alto_ventana = root.winfo_height()
posicion_x = (root.winfo_screenwidth() // 2) - (ancho_ventana // 2)
posicion_y = (root.winfo_screenheight() // 2) - (alto_ventana // 2)
root.geometry(f"+{posicion_x}+{posicion_y}")

# Frame para contener los widgets
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(fill="both", expand=True)

# Barra de menú
barra_menu = tk.Menu(root)
root.config(menu=barra_menu)

# Menú "Opciones"
menu_opciones = tk.Menu(barra_menu, tearoff=0)
barra_menu.add_cascade(label="Opciones", menu=menu_opciones)

menu_opciones.add_command(label="Salir", command=salir)

# Botón para seleccionar el archivo PDF
boton_seleccionar_pdf = tk.Button(frame, text="Seleccionar archivo PDF", command=seleccionar_archivo_pdf)
boton_seleccionar_pdf.pack(pady=10)

# Etiqueta para mostrar la ruta del archivo seleccionado
etiqueta_archivo = tk.Label(frame, text="No se ha seleccionado ningún archivo", wraplength=400)
etiqueta_archivo.pack(pady=10)

# Botón para comenzar la conversión
boton_comenzar = tk.Button(frame, text="Comenzar", command=convertir_pdf_a_texto)
boton_comenzar.pack(pady=10)

# Ejecutar el bucle principal de la aplicación
root.mainloop()