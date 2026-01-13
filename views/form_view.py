import flet as ft


def form_view(page: ft.Page):
    # GET: mostrar formulario vacío

    titulo = ft.TextField(
        label="Título",
        expand=True,
    )

    director = ft.TextField(
        label="Director",
        expand=True,
    )

    puntuacion = ft.TextField(
        label="Puntuación (1-10)",
        expand=True,
    )

    botones = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        controls=[
            ft.ElevatedButton(
                "Guardar",
                icon=ft.Icons.SAVE,
                disabled=True,  # aún sin acción
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
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Container(
                width=400,
                content=ft.Column(
                    spacing=15,
                    controls=[
                        titulo,
                        director,
                        puntuacion,
                        botones,
                    ],
                ),
            ),
        ],
    )
