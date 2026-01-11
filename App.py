import flet as ft
from database import Session
from models.pelicula import Pelicula
from views.home_view import home_view






def main(page: ft.Page):
    # [MODIFICADO]
    page.title = "🎞️ Flet Películas"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = ft.Colors.BLUE_GREY_900
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER



    page.add(home_view(page))


if __name__ == "__main__":
    ft.app(target=main)
