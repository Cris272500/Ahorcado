import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Configurar propiedades de la ventana
ventana.title("Mi ventana")
ventana.geometry("400x300")

# Agregar un widget de etiqueta
etiqueta = tk.Label(ventana, text="Crizzz!")
etiqueta.pack()

# Ejecutar el bucle principal de la ventana
ventana.mainloop()
