import tkinter as tk
from conection import crear_tablas, agregar_peliculas_iniciales
from ui_login import LoginFrame
from ui_menu import MenuFrame
from ui_juego import JuegoFrame
from ui_historial import HistorialFrame

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Configuración general de la ventana
        self.title("🎬 Adivina la Película o Serie")
        self.geometry("800x500")
        self.configure(bg="#1E1E2E")
        self.resizable(False, False)

        # Base de datos
        crear_tablas()
        agregar_peliculas_iniciales()

        # Variables globales
        self.usuario = None

        # Frame actual
        self.frame_actual = None

        # Mostrar login al iniciar
        self.mostrar_login()

    def cambiar_frame(self, nuevo_frame_class):
        """Destruye el frame actual y crea uno nuevo."""
        if self.frame_actual is not None:
            self.frame_actual.destroy()

        self.frame_actual = nuevo_frame_class(self)
        self.frame_actual.pack(fill="both", expand=True)

    # ==== Navegación entre pantallas ====
    def mostrar_login(self):
        self.cambiar_frame(LoginFrame)

    def mostrar_menu(self):
        self.cambiar_frame(MenuFrame)

    def mostrar_juego(self):
        self.cambiar_frame(JuegoFrame)

    def mostrar_historial(self):
        self.cambiar_frame(HistorialFrame)
