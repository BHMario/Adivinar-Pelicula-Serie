import sqlite3

DB_NAME = "juego.db"


def connect_db():
    """Crea la conexión con la base de datos."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    return conn, cursor


def crear_tablas():
    """Crea las tablas necesarias si no existen."""
    conn, cursor = connect_db()

    cursor.execute('''CREATE TABLE IF NOT EXISTS peliculas_series (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        titulo TEXT NOT NULL,
                        pista1 TEXT,
                        pista2 TEXT,
                        pista3 TEXT)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS historial (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        usuario TEXT NOT NULL,
                        titulo TEXT NOT NULL,
                        puntos INTEGER,
                        fecha DATETIME DEFAULT CURRENT_TIMESTAMP)''')

    conn.commit()
    conn.close()


def agregar_peliculas_iniciales():
    """Agrega películas o series iniciales si la tabla está vacía."""
    conn, cursor = connect_db()
    cursor.execute("SELECT COUNT(*) FROM peliculas_series")
    if cursor.fetchone()[0] == 0:
        peliculas = [
            ("Matrix",
             "Es una película de ciencia ficción",
             "Protagonizada por Keanu Reeves",
             "Tiene una famosa pastilla roja y azul"),

            ("Stranger Things",
             "Serie de misterio y ciencia ficción",
             "Se desarrolla en Hawkins",
             "Tiene un Demogorgon"),

            ("Breaking Bad",
             "Serie sobre un profesor de química",
             "El protagonista se llama Walter White",
             "Hace metanfetamina azul"),
        ]
        cursor.executemany(
            "INSERT INTO peliculas_series (titulo, pista1, pista2, pista3) VALUES (?, ?, ?, ?)",
            peliculas
        )
        conn.commit()
    conn.close()


def obtener_pelicula_aleatoria():
    """Obtiene una película o serie aleatoria."""
    conn, cursor = connect_db()
    cursor.execute("SELECT * FROM peliculas_series ORDER BY RANDOM() LIMIT 1")
    pelicula = cursor.fetchone()
    conn.close()
    return pelicula


def guardar_historial(usuario, titulo, puntos):
    """Guarda el resultado de un juego en el historial."""
    conn, cursor = connect_db()
    cursor.execute(
        "INSERT INTO historial (usuario, titulo, puntos) VALUES (?, ?, ?)",
        (usuario, titulo, puntos)
    )
    conn.commit()
    conn.close()


def obtener_historial():
    """Devuelve el historial completo de puntuaciones."""
    conn, cursor = connect_db()
    cursor.execute("SELECT usuario, titulo, puntos, fecha FROM historial ORDER BY fecha DESC")
    historial = cursor.fetchall()
    conn.close()
    return historial
