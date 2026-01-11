from database import Session
from models.pelicula import Pelicula


def obtener_todos():
    session = Session()
    peliculas = session.query(Pelicula).all()
    session.close()
    return peliculas
