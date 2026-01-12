import flet as ft
from views.home_view import home_view
from components.navbar import navbar


def main(page: ft.Page):
    # [MODIFICADO]
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Área dinámica de contenido
    content_area = ft.Column(expand=True)  # [NUEVO]

    def mostrar_home(e=None):
        content_area.controls.clear()  # [NUEVO]
        content_area.controls.append(home_view(page))  # [NUEVO]
        page.update()  # [NUEVO]

    def mostrar_form_placeholder(e=None):
        content_area.controls.clear()  # [NUEVO]
        content_area.controls.append(
            ft.Column(
                expand=True,
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    ft.Icon(
                        icon =ft.Icons.CONSTRUCTION,
                        size=60,
                        color=ft.Colors.AMBER_400,
                    ),
                    ft.Text(
                        "Formulario en construcción",
                        size=22,
                        weight=ft.FontWeight.BOLD,
                        color=ft.Colors.WHITE,
                        text_align=ft.TextAlign.CENTER,
                    ),
                    ft.Text(
                        "Aquí se agregará la película",
                        color=ft.Colors.GREY_300,
                    ),
                ],
            )
        )
        page.update()  # [NUEVO]

    # Navbar
    menu = navbar(mostrar_home, mostrar_form_placeholder)  # [NUEVO]

    page.add(menu, content_area)  # [MODIFICADO]

    mostrar_home()  # [NUEVO]


if __name__ == "__main__":
    ft.app(target=main)
