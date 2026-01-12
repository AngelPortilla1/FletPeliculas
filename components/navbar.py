import flet as ft


def navbar(on_home, on_add):
    return ft.Container(
        bgcolor=ft.Colors.BLUE_GREY_800,
        padding=10,
        content=ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            controls=[
                ft.ElevatedButton(
                    "Inicio",
                    icon=ft.Icons.HOME,
                    on_click=on_home,
                ),
                ft.ElevatedButton(
                    "Agregar Película",
                    icon=ft.Icons.ADD,
                    on_click=on_add,
                ),
            ],
        ),
    )
