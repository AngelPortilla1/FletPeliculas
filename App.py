import flet as ft
from database import Session
from models.pelicula import Pelicula


# [NUEVO]
def obtener_todos():
    session = Session()
    peliculas = session.query(Pelicula).all()
    session.close()
    return peliculas


def main(page: ft.Page):
    # [MODIFICADO]
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    peliculas = obtener_todos()  # [NUEVO]

    tabla = ft.DataTable(  # [NUEVO]
        expand=True,
        columns=[
            ft.DataColumn(ft.Text("ID")),
            ft.DataColumn(ft.Text("Título")),
            ft.DataColumn(ft.Text("Director")),
            ft.DataColumn(ft.Text("Puntuación")),
            ft.DataColumn(ft.Text("Acciones")),
        ],
        rows=[
            ft.DataRow(
                cells=[
                    ft.DataCell(ft.Text(str(p.id))),
                    ft.DataCell(ft.Text(p.titulo)),
                    ft.DataCell(ft.Text(p.director)),
                    ft.DataCell(ft.Text(str(p.puntuacion))),
                    ft.DataCell(
                        ft.Row(
                            controls=[
                                ft.IconButton(
                                    icon=ft.Icons.EDIT,
                                    tooltip="Editar",
                                    disabled=True,
                                ),
                                ft.IconButton(
                                    icon=ft.Icons.DELETE,
                                    tooltip="Eliminar",
                                    disabled=True,
                                ),
                            ]
                        )
                    ),
                ]
            )
            for p in peliculas
        ],
    )
    # Header con ícono + título uno al lado del otro
    header = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        controls=[
            ft.Icon(
                ft.Icons.MOVIE,
                size=64,
                color=ft.Colors.AMBER_400,
            ),
            ft.Text(
                "Listado de Películas",
                size=32,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
        ],
    )
    contenido = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            header,
            ft.Container(
                content=tabla,
                expand=True,
                padding=20,
            ),
        ],
    )

    page.add(contenido)


if __name__ == "__main__":
    ft.app(target=main)
