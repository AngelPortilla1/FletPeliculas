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

    # 1. Definimos la función que sabe ir al formulario en modo edición
    def ir_a_editar(id_pelicula):
        content_area.controls.clear()
        # Pasamos el id_pelicula al form_view
        content_area.controls.append(form_view(page, mostrar_home, id_pelicula))
        page.update()

    # 2. Actualizamos mostrar_home para que SIEMPRE pase 'ir_a_editar'
    def mostrar_home(e=None):
        content_area.controls.clear()
        # IMPORTANTE: Aquí es donde le pasas la función al home_view
        content_area.controls.append(home_view(page, mostrar_home, ir_a_editar))
        page.update()

    def mostrar_form_placeholder(e=None):
        content_area.controls.clear()
        # En modo creación normal, el tercer parámetro (pelicula_id) queda como None por defecto
        content_area.controls.append(form_view(page, mostrar_home))
        page.update()

    # Navbar
    menu = navbar(mostrar_home, mostrar_form_placeholder)
    page.add(menu, content_area)
    mostrar_home()  # Esta llamada inicial ahora ya llevará ir_a_editar




if __name__ == "__main__":
    ft.app(target=main)