import tkinter as tk

class MenuFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2D2D3A")

        tk.Label(self, text=f"👋 ¡Hola, {master.usuario}!",
                 font=("Arial", 20, "bold"), bg="#2D2D3A", fg="#FFD700").pack(pady=20)

        tk.Label(self, text="¿Qué deseas hacer?",
                 font=("Arial", 14), bg="#2D2D3A", fg="white").pack(pady=10)

        self.crear_boton("🎮 Jugar una nueva partida", master.mostrar_juego)
        self.crear_boton("📜 Ver mi historial", master.mostrar_historial)
        self.crear_boton("🚪 Salir", master.destroy)

    def crear_boton(self, texto, comando):
        tk.Button(self, text=texto, command=comando,
                  font=("Arial", 12, "bold"), bg="#5E60CE", fg="white",
                  activebackground="#4E50B5", relief="flat", cursor="hand2",
                  width=25).pack(pady=10)
