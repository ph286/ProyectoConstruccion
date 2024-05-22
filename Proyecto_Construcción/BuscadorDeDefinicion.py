import csv
import tkinter as tk
from tkinter import messagebox


class BuscadorDeDefinicion:
    def __init__(self, archivo_csv):
        self.archivo_csv = archivo_csv

    def buscar_definicion(self, termino):
        termino = termino.lower()
        with open(self.archivo_csv, newline='', encoding='utf-8') as csvfile:
            lector_csv = csv.reader(csvfile)
            for fila in lector_csv:
                concepto, definicion = fila
                if concepto.lower().strip() == termino:
                    return definicion.strip().strip('"')
        return "Definición no encontrada."


class InterfazDelBuscador:
    def __init__(self, master, archivo_csv):
        self.buscador = BuscadorDeDefinicion(archivo_csv)
        self.master = master
        self.master.title("Buscador de Definiciones")

        self.label = tk.Label(
            master, text="Ingrese el término que desea buscar:"
        )
        self.label.pack(pady=10)

        self.termino_entry = tk.Entry(master, width=50)
        self.termino_entry.pack(pady=10)

        self.boton_buscar = tk.Button(
            master, text="Buscar", command=self.buscar_definicion
        )
        self.boton_buscar.pack(pady=10)

        self.resultado_label = tk.Label(master, text="", wraplength=400)
        self.resultado_label.pack(pady=10)

    def buscar_definicion(self):
        termino = self.termino_entry.get().strip()
        if termino:
            definicion = self.buscador.buscar_definicion(termino)
            self.resultado_label.config(
                text=f"Definición de '{termino}': {definicion}"
            )
        else:
            messagebox.showwarning(
                "Entrada vacía", "Por favor, ingrese un término para buscar."
            )


if __name__ == "__main__":
    archivo_csv = "Compendios/definiciones_mejoradas.csv"
    root = tk.Tk()
    interfaz = InterfazDelBuscador(root, archivo_csv)
    root.mainloop()
