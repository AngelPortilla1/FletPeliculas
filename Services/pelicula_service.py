from database import Session
from models.pelicula import Pelicula


def validar_datos(datos):
    """Función auxiliar para centralizar la validación lógica."""
    titulo = datos.get("titulo", "").strip()
    director = datos.get("director", "").strip()
    puntuacion = datos.get("puntuacion")

    if not titulo or not director:
        return None, "Todos los campos son obligatorios."

    try:
        # Convertimos a entero por seguridad si viene como string
        puntuacion_int = int(puntuacion)
        if not (1 <= puntuacion_int <= 10):
            return None, "La puntuación debe estar entre 1 y 10."
    except (ValueError, TypeError):
        return None, "La puntuación debe ser un número entero válido."

    return (titulo, director, puntuacion_int), None
def obtener_todos():
    session = Session()
    peliculas = session.query(Pelicula).all()
    session.close()
    return peliculas


def crear(datos):
    campos, error = validar_datos(datos)
    if error:
        return {"ok": False, "mensaje": error}

    titulo, director, puntuacion = campos
    session = Session()
    try:
        nueva = Pelicula(titulo=titulo, director=director, puntuacion=puntuacion)
        session.add(nueva)
        session.commit()
        return {"ok": True, "mensaje": "Película registrada con éxito."}
    except Exception as e:
        return {"ok": False, "mensaje": f"Error de base de datos: {str(e)}"}
    finally:
        session.close()


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
    campos, error = validar_datos(datos)
    if error:
        return {"ok": False, "mensaje": error}

    titulo, director, puntuacion = campos
    session = Session()
    try:
        pelicula = session.get(Pelicula, pelicula_id)
        if pelicula:
            pelicula.titulo = titulo
            pelicula.director = director
            pelicula.puntuacion = puntuacion
            session.commit()
            return {"ok": True, "mensaje": "Película actualizada correctamente."}
        return {"ok": False, "mensaje": "No se encontró la película."}
    except Exception as e:
        session.rollback()
        return {"ok": False, "mensaje": f"Error: {str(e)}"}
    finally:
        session.close()
