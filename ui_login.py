import tkinter as tk
from tkinter import messagebox

class LoginFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2D2D3A")

        tk.Label(self, text="🎬 Adivina la Película o Serie 🎬",
                 font=("Arial", 24, "bold"), bg="#2D2D3A", fg="#FFD700").pack(pady=30)

        tk.Label(self, text="Introduce tu nombre para comenzar:",
                 font=("Arial", 14), bg="#2D2D3A", fg="white").pack(pady=10)

        self.nombre_entry = tk.Entry(self, font=("Arial", 13), justify="center")
        self.nombre_entry.pack(pady=10, ipadx=10, ipady=5)

        tk.Button(self, text="Comenzar", bg="#5E60CE", fg="white",
                  font=("Arial", 12, "bold"), relief="flat", cursor="hand2",
                  command=self.iniciar).pack(pady=20)

    def iniciar(self):
        nombre = self.nombre_entry.get().strip()
        if not nombre:
            messagebox.showwarning("Atención", "Debes ingresar un nombre.")
            return
        self.master.usuario = nombre
        self.master.mostrar_menu()
