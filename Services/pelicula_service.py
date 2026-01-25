from database import Session
from models.pelicula import Pelicula

from database import Session
from models.pelicula import Pelicula

def validar_datos(datos):
    """
    Validación lógica centralizada.
    Protege la BD aunque la UI falle.
    """
    titulo = datos.get("titulo", "").strip()
    director = datos.get("director", "").strip()
    puntuacion = datos.get("puntuacion")

    if not titulo or not director:
        return None, "Todos los campos son obligatorios"

    try:
        puntuacion_int = int(puntuacion)
    except (ValueError, TypeError):
        return None, "La puntuación debe ser un número entero"

    if not (1 <= puntuacion_int <= 10):
        return None, "La puntuación debe estar entre 1 y 10"

    return (titulo, director, puntuacion_int), None

def crear(datos):
    datos_validados, error = validar_datos(datos)
    if error:
        return {"ok": False, "mensaje": error}

    titulo, director, puntuacion = datos_validados

    session = Session()
    try:
        nueva = Pelicula(
            titulo=titulo,
            director=director,
            puntuacion=puntuacion
        )
        session.add(nueva)
        session.commit()
        return {"ok": True, "mensaje": "Película registrada correctamente"}
    except Exception as e:
        session.rollback()
        return {"ok": False, "mensaje": f"Error al guardar: {str(e)}"}
    finally:
        session.close()


def actualizar(pelicula_id, datos):
    session = Session()
    try:
        pelicula = session.get(Pelicula, pelicula_id)
        if not pelicula:
            return {"ok": False, "mensaje": "No se encontró la película"}

        datos_validados, error = validar_datos(datos)
        if error:
            return {"ok": False, "mensaje": error}

        titulo, director, puntuacion = datos_validados

        pelicula.titulo = titulo
        pelicula.director = director
        pelicula.puntuacion = puntuacion

        session.commit()
        return {"ok": True, "mensaje": "Película actualizada correctamente"}

    except Exception as e:
        session.rollback()
        return {"ok": False, "mensaje": f"Error: {str(e)}"}
    finally:
        session.close()

def obtener_todos():
    session = Session()
    peliculas = session.query(Pelicula).all()
    session.close()
    return peliculas




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

