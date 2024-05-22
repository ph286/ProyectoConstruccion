import tkinter as tk
from tkinter import messagebox

class AgregarPalabra:
    def __init__(self, archivo, titulo):
        self.archivo = archivo
        self.titulo = titulo
        self.crear_ventana()

    def agregar_palabra(self, palabra):
        with open(self.archivo, 'a') as f:
            f.write(palabra + '\n')

    def crear_ventana(self):
        self.root = tk.Toplevel()
        self.root.title(self.titulo)
        ancho_ventana = 500
        alto_ventana = 250
        self.centrar_ventana(self.root, ancho_ventana, alto_ventana)

        frame = tk.Frame(self.root)
        frame.pack(fill='both', expand=True)

        label = tk.Label(frame, text="Ingrese la palabra que desea agregar:")
        label.pack(pady=(50, 10))

        self.entry = tk.Entry(frame)
        self.entry.pack(pady=5)

        btn_agregar = tk.Button(frame, text="Agregar", command=self.agregar)
        btn_agregar.pack(pady=10)

        btn_salir = tk.Button(frame, text="Cancelar", command=self.root.destroy)
        btn_salir.pack(pady=10)

    def agregar(self):
        palabra = self.entry.get().strip()
        if palabra:
            self.agregar_palabra(palabra)
            messagebox.showinfo("Éxito", f'Palabra "{palabra}" agregada al listado.')
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Advertencia", "¡No se puede agregar una palabra vacía!")

    def centrar_ventana(self, ventana, ancho, alto):
        pantalla_ancho = ventana.winfo_screenwidth()
        pantalla_alto = ventana.winfo_screenheight()
        posicion_x = (pantalla_ancho // 2) - (ancho // 2)
        posicion_y = (pantalla_alto // 2) - (alto // 2)
        ventana.geometry(f"{ancho}x{alto}+{posicion_x}+{posicion_y}")
