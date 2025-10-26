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
            # Películas clásicas
            ("Matrix", "Es una película de ciencia ficción", "Protagonizada por Keanu Reeves", "Tiene una famosa pastilla roja y azul"),
            ("Titanic", "Un barco, amor y tragedia", "Dirigida por James Cameron", "Protagonizada por Leonardo DiCaprio y Kate Winslet"),
            ("Inception", "Sueños dentro de sueños", "Protagonizada por Leonardo DiCaprio", "Dirigida por Christopher Nolan"),
            ("Jurassic Park", "Ciencia, dinosaurios y caos", "Basada en una novela de Michael Crichton", "Dirigida por Steven Spielberg"),
            ("The Matrix", "Realidad simulada y lucha por la libertad", "Protagonizada por Keanu Reeves", "Dirigida por las hermanas Wachowski"),
            ("The Godfather", "Mafia, familia y poder", "Dirigida por Francis Ford Coppola", "Protagonizada por Marlon Brando y Al Pacino"),
            ("The Dark Knight", "Un héroe oscuro en una ciudad corrupta", "Protagonizada por Christian Bale", "El villano es el Joker, interpretado por Heath Ledger"),

            # Series famosas
            ("Breaking Bad", "Serie sobre un profesor de química", "El protagonista se llama Walter White", "Hace metanfetamina azul"),
            ("Stranger Things", "Serie de misterio y ciencia ficción", "Se desarrolla en Hawkins", "Tiene un Demogorgon"),
            ("Game of Thrones", "Reinos, dragones y traición", "Basada en los libros de George R. R. Martin", "Frase famosa: 'Winter is Coming'"),
            ("Friends", "Un grupo de amigos en Nueva York", "Un sofá en una cafetería", "Personajes: Rachel, Ross, Monica, Chandler, Joey y Phoebe"),
            ("The Office", "Comedia en una empresa de papel", "Protagonizada por Steve Carell", "Documental falso sobre empleados de oficina"),
            ("The Mandalorian", "Un cazarrecompensas en una galaxia lejana", "Del universo de Star Wars", "Aparece un personaje adorable apodado 'Baby Yoda'"),
            ("Sherlock", "Detective moderno en Londres", "Interpretado por Benedict Cumberbatch", "Su compañero es el Dr. Watson"),

            # Películas animadas
            ("Toy Story", "Juguetes que cobran vida", "El protagonista es un vaquero", "Su mejor amigo es un astronauta"),
            ("Finding Nemo", "Un padre busca a su hijo en el océano", "Animación de Pixar", "El hijo es un pez payaso"),
            ("Shrek", "Un ogro y una princesa poco convencional", "Acompañado por un burro parlante", "Protagonizada por Mike Myers y Eddie Murphy"),
            ("Frozen", "Hermanas, hielo y una canción muy famosa", "De Disney", "Frase clave: 'Let it go'"),
            ("Coco", "Un niño viaja al mundo de los muertos", "Inspirada en el Día de Muertos mexicano", "Protagonizada por Miguel")
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
