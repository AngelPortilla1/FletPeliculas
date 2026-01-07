import flet as ft


def main(page: ft.Page):
    # Configuración general de la página
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # Contenido principal
    content = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(
                icon=ft.Icons.MOVIE,
                size=80,
                color=ft.Colors.AMBER_400,
            ),
            ft.Text(
                "Bienvenido al Sistema de Películas",
                size=28,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
                text_align=ft.TextAlign.CENTER,
            ),
            ft.Text(
                "Tu primera app CRUD con Flet y MySQL",
                size=16,
                color=ft.Colors.GREY_300,
                text_align=ft.TextAlign.CENTER,
            ),
        ],
    )

    page.add(content)


if __name__ == "__main__":
    ft.run(main)
