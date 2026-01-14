from database import Session
from models.pelicula import Pelicula


def obtener_todos():
    session = Session()
    peliculas = session.query(Pelicula).all()
    session.close()
    return peliculas


def crear(datos):
    titulo = datos.get("titulo","").strip()
    director = datos.get("director","").strip()
    puntuacion = datos.get("puntuacion")

    #Validaciones simples
    if not titulo or not director:
        return {"ok":False, "mensaje":"Todos los campos son obligatorios"}
    try:
        puntuacion = int(puntuacion)
    except Exception:
        return {"ok":False, "mensaje":"La puntuacion debe ser un un numero entero"}
    if puntuacion <0 or puntuacion > 10:
        return {"ok":False, "mensaje":"La puntuacion debe ser un numero entre 0 y 10"}


    #Guardar en BD
    session = Session()
    nueva = Pelicula(
        titulo = titulo,
        director = director,
        puntuacion = puntuacion,
    )

    session.add(nueva)
    session.commit()
    session.close()


    return {"ok":True, "mensaje":"Pelicula registrada correctamente"}
