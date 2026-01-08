import os
import subprocess
from dotenv import load_dotenv
from sqlalchemy import create_engine, text

# Cargar variables de entorno
load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")

DATABASE_URL = (
    f"mysql+pymysql://{DB_USER}:{DB_PASS}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


def limpiar_alembic_version():
    try:
        engine = create_engine(DATABASE_URL)
        with engine.connect() as conn:
            conn.execute(text("DROP TABLE IF EXISTS alembic_version"))
            conn.commit()
        print("🧹 Tabla alembic_version limpiada (si existía)")
    except Exception as e:
        print("⚠️ No se pudo limpiar alembic_version")
        print(e)


def ejecutar_migraciones():
    try:
        print("📦 Generando migración...")
        subprocess.run(
            ["alembic", "revision", "--autogenerate", "-m", "crear tabla peliculas"],
            check=True
        )

        print("🚀 Aplicando migraciones...")
        subprocess.run(
            ["alembic", "upgrade", "head"],
            check=True
        )

        print("✅ Migración aplicada correctamente")
    except subprocess.CalledProcessError as e:
        print("❌ Error durante la migración")
        print(e)


if __name__ == "__main__":
    limpiar_alembic_version()
    ejecutar_migraciones()
