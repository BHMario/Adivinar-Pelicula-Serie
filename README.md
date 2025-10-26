# 🎬 Adivina la Película o Serie

Un juego desarrollado en **Python + Tkinter + SQLite** donde el jugador debe **adivinar el nombre de una película o serie** a partir de una serie de pistas.  
Cada pista resta puntos, así que… ¡piénsalo bien antes de pedir otra! 😄  

---

## 🧠 Descripción

El juego comienza solicitando el nombre del jugador.  
A partir de ahí podrás:

- 🎮 Jugar una nueva partida  
- 📜 Consultar tu historial de partidas y puntuaciones  
- 🔄 Cambiar de usuario
- 🚪 Salir del juego  

Cada jugador comienza con **30 puntos**.  
Puedes pedir hasta **3 pistas**, pero cada una (excepto la primera) te restará **5 puntos**.  
Cuando adivines correctamente, tu puntuación se guardará en el historial junto con la fecha.

---

## 🖥️ Características principales

✅ Interfaz gráfica moderna con **Tkinter**  
✅ Base de datos **SQLite** para guardar películas y puntuaciones  
✅ Sistema de **usuarios y sesiones**  
✅ Historial de partidas por jugador  
✅ **Feedback visual** (efectos de color en lugar de cuadros de mensaje)  
✅ Posibilidad de **añadir fácilmente nuevas películas y series**

---

## 🧩 Tecnologías utilizadas

| Tecnología | Uso |
|-------------|-----|
| 🐍 Python | Lenguaje principal |
| 🖼️ Tkinter | Interfaz gráfica |
| 🗃️ SQLite | Base de datos local |
| 🧱 POO | Arquitectura basada en clases |
| 💾 CRUD | Gestión de películas e historial |

---

## 🗂️ Estructura del proyecto

```
📁 adivina-pelicula/
├── main.py                 # Punto de entrada principal
├── conection.py            # Conexión y operaciones con SQLite
├── ui_login.py             # Pantalla de login
├── ui_menu.py              # Menú principal del juego
├── ui_juego.py             # Lógica del juego (pistas, adivinanzas, feedback)
├── ui_historial.py         # Vista del historial del jugador
├── juego.db                # Base de datos SQLite (se crea automáticamente)
└── README.md               # Este archivo 😄
```

---

## ⚙️ Instalación y ejecución

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/BHMario/Adivinar-Pelicula-Serie.git
   cd Adivinar-Pelicula-Serie
   ```

2. **(Opcional) Crear un entorno virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate     # En Linux/Mac
   venv\Scripts\activate        # En Windows
   ```

3. **Ejecutar el juego**
   ```bash
   python main.py
   ```

4. ¡Disfruta adivinando películas y compitiendo por la mejor puntuación! 🎬

---

## 🧩 Base de datos

La base de datos se crea automáticamente al ejecutar el juego por primera vez.  
Puedes ampliar la lista de películas modificando la función `agregar_peliculas_iniciales()` en `conection.py`.

---

## 🧑‍💻 Autor

Desarrollado por **Mario Sánchez Ruiz**  
Proyecto realizado en Python.

---

🎯 *“Adivinar nunca fue tan divertido. Demuestra que eres el mayor cinéfilo de todos.”*
