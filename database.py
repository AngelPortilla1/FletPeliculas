import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

# Cargar variables de entorno
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

# Construcción de la URL de conexión
DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

# Crear engine
engine = create_engine(DATABASE_URL, echo=True)

# Crear sesión
Session = sessionmaker(bind=engine)

# Base para los modelos
Base = declarative_base()


def test_connection():
    try:
        with engine.connect() as connection:
            connection.execute(text("SELECT 1"))
        print("✅ Conexión a MySQL exitosa")
    except Exception as e:
        print("❌ Error al conectar con MySQL")
        print(e)


if __name__ == "__main__":
    test_connection()
