import tkinter as tk
from tkinter import ttk
from conection import obtener_historial

class HistorialFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2D2D3A")

        tk.Label(self, text=f"📜 Historial de {master.usuario}",
                 font=("Arial", 18, "bold"), bg="#2D2D3A", fg="#FFD700").pack(pady=15)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview",
                        background="#2D2D3A", foreground="white",
                        fieldbackground="#2D2D3A", rowheight=25)
        style.configure("Custom.Treeview.Heading",
                        background="#3E3E4E", foreground="#FFD700",
                        font=("Arial", 12, "bold"))

        tree = ttk.Treeview(self, columns=("Título", "Puntos", "Fecha"), show='headings',
                            style="Custom.Treeview", height=10)
        tree.heading("Título", text="Título")
        tree.heading("Puntos", text="Puntos")
        tree.heading("Fecha", text="Fecha")
        tree.column("Título", width=300, anchor="center")
        tree.column("Puntos", width=100, anchor="center")
        tree.column("Fecha", width=180, anchor="center")
        tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Cargar historial del usuario actual
        historial = obtener_historial()
        for user, titulo, puntos, fecha in historial:
            if user == master.usuario:
                tree.insert("", tk.END, values=(titulo, puntos, fecha))

        tk.Button(self, text="⬅️ Volver al menú", command=master.mostrar_menu,
                  font=("Arial", 12, "bold"), bg="#5E60CE", fg="white",
                  activebackground="#4E50B5", relief="flat", cursor="hand2").pack(pady=15)
