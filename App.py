import flet as ft
from views.home_view import home_view
from components.navbar import navbar
from views.form_view import form_view


def main(page: ft.Page):
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.START

    # Área dinámica de contenido
    content_area = ft.Column(expand=True)

    def mostrar_home(e=None):
        content_area.controls.clear()
        content_area.controls.append(home_view(page, mostrar_home))  # ← Pasar la función
        page.update()

    def mostrar_form_placeholder(e=None):
        content_area.controls.clear()
        content_area.controls.append(form_view(page, mostrar_home))
        page.update()

    # Navbar
    menu = navbar(mostrar_home, mostrar_form_placeholder)

    page.add(menu, content_area)

    mostrar_home()


if __name__ == "__main__":
    ft.app(target=main)