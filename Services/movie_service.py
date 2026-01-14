
import sqlite3

DB_PATH = "flet_peliculas_db"


def insert_movie(title, director, rating):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute(
            """
            INSERT INTO peliculas (titulo, director, puntuacion)
            VALUES (?, ?, ?)
            """,
            (title, director, rating),
        )
        conn.commit()
