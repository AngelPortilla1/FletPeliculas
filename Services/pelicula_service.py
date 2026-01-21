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


def delete_movie(movie_id: int) -> dict:
    session = Session()
    try:

        pelicula = session.get(Pelicula, movie_id)

        if not pelicula:
            return {"ok": False, "mensaje": f"No existe película con id {movie_id}"}

        session.delete(pelicula)
        session.commit()

        return {"ok": True, "mensaje": "Película eliminada correctamente"}

    except Exception as e:
        session.rollback()
        return {"ok": False, "mensaje": f"Error al eliminar: {str(e)}"}

    finally:
        session.close()


def obtener_por_id(pelicula_id):
    session = Session()
    # Usamos .get() de SQLAlchemy que es lo más directo por ID
    pelicula = session.get(Pelicula, pelicula_id)
    session.close()
    return pelicula

def actualizar(pelicula_id, datos):
    session = Session()
    try:
        pelicula = session.get(Pelicula, pelicula_id)
        if pelicula:
            pelicula.titulo = datos.get("titulo")
            pelicula.director = datos.get("director")
            pelicula.puntuacion = datos.get("puntuacion")
            session.commit()
            return {"ok": True, "mensaje": "Película actualizada correctamente"}
        return {"ok": False, "mensaje": "No se encontró la película"}
    except Exception as e:
        session.rollback()
        return {"ok": False, "mensaje": f"Error: {str(e)}"}
    finally:
        session.close()
