import tkinter as tk
from tkinter import messagebox, ttk
from conection import (
    crear_tablas,
    agregar_peliculas_iniciales,
    obtener_pelicula_aleatoria,
    guardar_historial,
    obtener_historial
)

# Inicializar base de datos
crear_tablas()
agregar_peliculas_iniciales()


class Juego:
    def __init__(self, master):
        self.master = master
        master.title("🎬 Adivina la Película o Serie")
        master.geometry("800x500")
        master.configure(bg="#1E1E2E")  # fondo oscuro
        master.resizable(False, False)

        # Variables del juego
        self.usuario = None
        self.puntos = 30
        self.pistas_usadas = 0
        self.actual = None
        self.pistas = []

        # Colores y estilo
        self.color_fondo = "#1E1E2E"
        self.color_frame = "#2D2D3A"
        self.color_texto = "#FFFFFF"
        self.color_boton = "#5E60CE"
        self.color_boton_hover = "#4E50B5"
        self.color_acento = "#FFD700"
        self.color_tabla_fondo = "#2D2D3A"
        self.color_tabla_texto = "#FFFFFF"
        self.color_tabla_encabezado = "#3E3E4E"

        # Mostrar pantalla de inicio
        self.mostrar_login()

    # ===================== LOGIN ===================== #
    def mostrar_login(self):
        self.limpiar_ventana()
        frame = self.crear_frame_centrado()

        tk.Label(frame, text="🎬 Adivina la Película o Serie 🎬",
                 font=("Arial", 22, "bold"), bg=self.color_frame, fg=self.color_acento).pack(pady=20)

        tk.Label(frame, text="Introduce tu nombre para comenzar:",
                 font=("Arial", 14), bg=self.color_frame, fg=self.color_texto).pack(pady=10)

        self.nombre_entry = tk.Entry(frame, font=("Arial", 13), justify="center")
        self.nombre_entry.pack(pady=10, ipadx=10, ipady=5)

        self.crear_boton(frame, "Comenzar", self.iniciar_sesion).pack(pady=15)

    def iniciar_sesion(self):
        nombre = self.nombre_entry.get().strip()
        if not nombre:
            messagebox.showwarning("Atención", "Debes ingresar un nombre.")
            return
        self.usuario = nombre
        self.mostrar_menu_principal()

    # ===================== MENÚ PRINCIPAL ===================== #
    def mostrar_menu_principal(self):
        self.limpiar_ventana()
        frame = self.crear_frame_centrado()

        tk.Label(frame, text=f"👋 ¡Hola, {self.usuario}!", font=("Arial", 20, "bold"),
                 bg=self.color_frame, fg=self.color_acento).pack(pady=10)

        tk.Label(frame, text="¿Qué deseas hacer?", font=("Arial", 14),
                 bg=self.color_frame, fg=self.color_texto).pack(pady=10)

        self.crear_boton(frame, "🎮 Jugar una nueva partida", self.iniciar_juego).pack(pady=10)
        self.crear_boton(frame, "📜 Ver mi historial", self.mostrar_historial_usuario).pack(pady=10)
        self.crear_boton(frame, "🚪 Salir", self.master.destroy).pack(pady=10)

    # ===================== INTERFAZ DEL JUEGO ===================== #
    def iniciar_juego(self):
        self.limpiar_ventana()
        self.puntos = 30
        self.pistas_usadas = 0
        self.actual = obtener_pelicula_aleatoria()
        self.pistas = [self.actual[2], self.actual[3], self.actual[4]]

        frame = self.crear_frame_centrado()

        tk.Label(frame, text="🎬 Adivina la Película o Serie 🎬",
                 font=("Arial", 18, "bold"), bg=self.color_frame, fg=self.color_acento).pack(pady=10)

        self.pista_label = tk.Label(frame, text="Pulsa 'Pedir pista' para comenzar.",
                                    wraplength=600, justify="center",
                                    font=("Arial", 13), bg=self.color_frame, fg=self.color_texto)
        self.pista_label.pack(pady=20)

        self.puntos_label = tk.Label(frame, text=f"Puntos: {self.puntos}",
                                     font=("Arial", 13, "bold"), bg=self.color_frame, fg=self.color_acento)
        self.puntos_label.pack()

        botones_frame = tk.Frame(frame, bg=self.color_frame)
        botones_frame.pack(pady=10)

        self.crear_boton(botones_frame, "🧩 Pedir pista", self.pedir_pista).grid(row=0, column=0, padx=10)
        self.crear_boton(botones_frame, "⬅️ Volver al menú", self.mostrar_menu_principal).grid(row=0, column=1, padx=10)

        self.entrada = tk.Entry(frame, width=40, font=("Arial", 12), justify="center")
        self.entrada.pack(pady=10, ipady=5)

        self.crear_boton(frame, "✅ Adivinar", self.adivinar).pack(pady=10)

    def pedir_pista(self):
        """Muestra una pista. La primera no resta puntos; las siguientes sí."""
        if self.pistas_usadas < len(self.pistas):
            self.pista_label.config(text=self.pistas[self.pistas_usadas])

            # Resta puntos solo a partir de la segunda pista
            if self.pistas_usadas >= 1:
                self.puntos -= 5
                self.puntos_label.config(text=f"Puntos: {self.puntos}")

            self.pistas_usadas += 1
        else:
            messagebox.showinfo("Sin pistas", "Ya no hay más pistas disponibles.")

    def adivinar(self):
        intento = self.entrada.get().strip()
        if not intento:
            messagebox.showwarning("Atención", "Debes escribir una respuesta.")
            return

        if intento.lower() == self.actual[1].lower():
            messagebox.showinfo("¡Correcto!", f"¡Has acertado '{self.actual[1]}'!\nPuntuación: {self.puntos}")
            guardar_historial(self.usuario, self.actual[1], self.puntos)
            self.mostrar_menu_principal()
        else:
            messagebox.showerror("Incorrecto", "No es correcto. ¡Sigue intentando!")

    # ===================== HISTORIAL ===================== #
    def mostrar_historial_usuario(self):
        self.limpiar_ventana()
        frame = self.crear_frame_centrado()

        tk.Label(frame, text=f"📜 Historial de {self.usuario}",
                 font=("Arial", 18, "bold"), bg=self.color_frame, fg=self.color_acento).pack(pady=15)

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Custom.Treeview",
                        background=self.color_tabla_fondo,
                        foreground=self.color_tabla_texto,
                        fieldbackground=self.color_tabla_fondo,
                        rowheight=25,
                        font=("Arial", 11))
        style.configure("Custom.Treeview.Heading",
                        background=self.color_tabla_encabezado,
                        foreground=self.color_acento,
                        font=("Arial", 12, "bold"))

        tree = ttk.Treeview(frame, columns=("Título", "Puntos", "Fecha"), show='headings',
                            style="Custom.Treeview", height=10)
        tree.heading("Título", text="Título")
        tree.heading("Puntos", text="Puntos")
        tree.heading("Fecha", text="Fecha")
        tree.column("Título", width=300, anchor="center")
        tree.column("Puntos", width=100, anchor="center")
        tree.column("Fecha", width=180, anchor="center")
        tree.pack(fill=tk.BOTH, expand=True, padx=20, pady=10)

        # Filtrar solo partidas del usuario actual
        historial = obtener_historial()
        for user, titulo, puntos, fecha in historial:
            if user == self.usuario:
                tree.insert("", tk.END, values=(titulo, puntos, fecha))

        self.crear_boton(frame, "⬅️ Volver al menú", self.mostrar_menu_principal).pack(pady=15)

    # ===================== UTILIDADES ===================== #
    def crear_frame_centrado(self):
        """Crea un frame centrado con fondo oscuro."""
        frame = tk.Frame(self.master, bg=self.color_frame, bd=3, relief="flat")
        frame.place(relx=0.5, rely=0.5, anchor="center", width=700, height=400)
        return frame

    def crear_boton(self, parent, texto, comando):
        """Crea un botón estilizado."""
        btn = tk.Button(parent, text=texto, command=comando,
                        font=("Arial", 12, "bold"),
                        bg=self.color_boton, fg="white",
                        activebackground=self.color_boton_hover,
                        activeforeground="white",
                        relief="flat", padx=15, pady=5, cursor="hand2")
        return btn

    def limpiar_ventana(self):
        """Elimina todos los widgets actuales de la ventana."""
        for widget in self.master.winfo_children():
            widget.destroy()


# Ejecutar aplicación
if __name__ == "__main__":
    root = tk.Tk()
    app = Juego(root)
    root.mainloop()
