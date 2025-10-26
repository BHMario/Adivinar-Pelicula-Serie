import tkinter as tk
from conection import obtener_pelicula_aleatoria, guardar_historial

class JuegoFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master, bg="#2D2D3A")
        self.master = master

        self.puntos = 30
        self.pistas_usadas = 0
        self.actual = obtener_pelicula_aleatoria()
        self.pistas = [self.actual[2], self.actual[3], self.actual[4]]

        tk.Label(self, text="🎬 Adivina la Película o Serie 🎬",
                 font=("Arial", 20, "bold"), bg="#2D2D3A", fg="#FFD700").pack(pady=15)

        self.pista_label = tk.Label(self, text="Pulsa 'Pedir pista' para comenzar.",
                                    wraplength=600, justify="center", font=("Arial", 13),
                                    bg="#2D2D3A", fg="white")
        self.pista_label.pack(pady=20)

        self.puntos_label = tk.Label(self, text=f"Puntos: {self.puntos}",
                                     font=("Arial", 13, "bold"), bg="#2D2D3A", fg="#FFD700")
        self.puntos_label.pack()

        # Label de feedback (aciertos/fallos/pistas)
        self.feedback_label = tk.Label(self, text="", font=("Arial", 14, "bold"),
                                       bg="#2D2D3A", fg="#FFD700")
        self.feedback_label.pack(pady=5)

        botones_frame = tk.Frame(self, bg="#2D2D3A")
        botones_frame.pack(pady=10)

        self.crear_boton(botones_frame, "🧩 Pedir pista", self.pedir_pista).grid(row=0, column=0, padx=10)
        self.crear_boton(botones_frame, "⬅️ Volver al menú", master.mostrar_menu).grid(row=0, column=1, padx=10)

        self.entrada = tk.Entry(self, width=40, font=("Arial", 12), justify="center")
        self.entrada.pack(pady=10, ipady=5)

        self.crear_boton(self, "✅ Adivinar", self.adivinar).pack(pady=10)

    # Feedback visual
    def mostrar_feedback(self, mensaje, color="#00FF00", duracion=1500):
        self.feedback_label.config(text=mensaje, fg=color)
        self.after(duracion, lambda: self.feedback_label.config(text=""))

    # Funciones de juego
    def pedir_pista(self):
        if self.pistas_usadas < len(self.pistas):
            pista = self.pistas[self.pistas_usadas]
            self.pista_label.config(text=pista)
            self.mostrar_feedback(f"Pista {self.pistas_usadas + 1}", color="#FFD700")

            if self.pistas_usadas >= 1:
                self.puntos -= 5
                self.puntos_label.config(text=f"Puntos: {self.puntos}")

            self.pistas_usadas += 1
        else:
            self.mostrar_feedback("Ya no hay más pistas.", color="#FF4500")

    def adivinar(self):
        intento = self.entrada.get().strip()
        if not intento:
            self.mostrar_feedback("Debes escribir una respuesta.", color="#FF4500")
            return

        if intento.lower() == self.actual[1].lower():
            self.mostrar_feedback(f"¡Has acertado '{self.actual[1]}'!", color="#00FF00")
            guardar_historial(self.master.usuario, self.actual[1], self.puntos)
            self.after(1500, self.master.mostrar_menu)
        else:
            self.mostrar_feedback("¡Incorrecto! Sigue intentando.", color="#FF4500")

    # Botón estilizado
    def crear_boton(self, parent, texto, comando):
        return tk.Button(parent, text=texto, command=comando,
                         font=("Arial", 12, "bold"),
                         bg="#5E60CE", fg="white",
                         activebackground="#4E50B5",
                         relief="flat", cursor="hand2", padx=10, pady=5)
