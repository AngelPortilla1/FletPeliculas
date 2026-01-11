import flet as ft
from Services.pelicula_service import obtener_todos

def home_view(page: ft.Page):
    peliculas = obtener_todos()

    tabla = ft.DataTable(
        # quitamos expand=True aquí para evitar conflictos
        border=ft.border.all(1, ft.Colors.GREY_700),
        border_radius=8,
        heading_row_color=ft.Colors.BLUE_GREY_700,
        heading_row_height=48,
        columns=[
            ft.DataColumn(ft.Text("ID", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Título", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Director", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Puntuación", weight=ft.FontWeight.BOLD)),
            ft.DataColumn(ft.Text("Acciones", weight=ft.FontWeight.BOLD)),
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
                            spacing=0,
                            controls=[
                                ft.IconButton(icon=ft.Icons.EDIT, tooltip="Editar", disabled=True),
                                ft.IconButton(icon=ft.Icons.DELETE, tooltip="Eliminar", disabled=True),
                            ]
                        )
                    ),
                ]
            ) for p in peliculas
        ],
    )

    header = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=16,
        controls=[
            ft.Icon(ft.Icons.MOVIE, size=56, color=ft.Colors.AMBER_400),
            ft.Text(
                "Flet Peliculas",
                size=30,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
        ],
    )

    subtitulo = ft.Text(                    # ← Cambiado a Text simple (más limpio)
        "Listado de películas",
        size=18,
        color=ft.Colors.WHITE70,
        text_align=ft.TextAlign.CENTER,
    )

    contenido = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,     # centro vertical (lo más importante ahora)
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30,
        controls=[
            header,
            subtitulo,
            ft.Container(                          # ← Container sin expand=True
                content=tabla,
                expand=True,                       # ← expand aquí SÍ está bien (ocupa el resto)
                padding=20,
                bgcolor=ft.Colors.BLUE_GREY_800,   # fondo para que se note
                border_radius=10,
                alignment = ft.Alignment(0, 0)
            ),
        ],
    )

    return contenido   # ← importante: retornamos el control principal