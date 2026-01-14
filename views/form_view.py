import flet as ft
from Services.movie_service import insert_movie


def form_view(page: ft.Page):
    titulo = ft.TextField(label="Título", expand=True)
    director = ft.TextField(label="Director", expand=True)
    puntuacion = ft.TextField(label="Puntuación (1-10)", expand=True)

    mensaje = ft.Text(color=ft.Colors.RED_400)

    def guardar(e):
        if not titulo.value or not director.value or not puntuacion.value:
            mensaje.value = "Todos los campos son obligatorios"
            page.update()
            return

        try:
            rating = int(puntuacion.value)
            if rating < 1 or rating > 10:
                raise ValueError
        except ValueError:
            mensaje.value = "La puntuación debe ser un número entre 1 y 10"
            page.update()
            return

        insert_movie(titulo.value, director.value, rating)
        page.go("/")  # volver al home

    botones = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(
                "Guardar",
                icon=ft.Icons.SAVE,
                on_click=guardar,
            ),
            ft.OutlinedButton(
                "Cancelar",
                icon=ft.Icons.CANCEL,
                on_click=lambda e: page.go("/"),
            ),
        ],
    )

    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(
                icon=ft.Icons.MOVIE_EDIT,
                size=70,
                color=ft.Colors.AMBER_400,
            ),
            ft.Text(
                "Agregar Película",
                size=26,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
            ft.Container(
                width=400,
                content=ft.Column(
                    spacing=15,
                    controls=[
                        titulo,
                        director,
                        puntuacion,
                        mensaje,
                        botones,
                    ],
                ),
            ),
        ],
    )
