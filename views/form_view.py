import flet as ft
from Services.pelicula_service import crear


# [MODIFICADO] Añadimos el parámetro 'volver_home'
def form_view(page: ft.Page, volver_home):
    titulo = ft.TextField(label="Título", expand=True)
    director = ft.TextField(label="Director", expand=True)
    puntuacion = ft.TextField(
        label="Puntuación (0-10)",
        expand=True,
        keyboard_type=ft.KeyboardType.NUMBER,
        max_length=2,
    )

    mensaje = ft.Text(color=ft.Colors.RED_400, text_align=ft.TextAlign.CENTER)

    def guardar(e):
        mensaje.value = ""
        page.update()

        tit = titulo.value.strip()
        dir_ = director.value.strip()
        pun = puntuacion.value.strip()

        if not tit or not dir_ or not pun:
            mensaje.value = "Todos los campos son obligatorios"
            page.update()
            return

        try:
            rating = int(pun)
            if rating < 0 or rating > 10:
                raise ValueError
        except ValueError:
            mensaje.value = "La puntuación debe ser un número entero entre 0 y 10"
            page.update()
            return

        resultado = crear({"titulo": tit, "director": dir_, "puntuacion": rating})

        if resultado["ok"]:
            # Corrección del SnackBar (show_dialog no sirve para SnackBar)
            snack = ft.SnackBar(
                content=ft.Text("¡Película registrada correctamente!", color=ft.Colors.WHITE),
                bgcolor=ft.Colors.GREEN_800
            )
            page.overlay.append(snack)
            snack.open = True
            page.update()

            # [MODIFICADO] Usamos la función callback en vez de page.go
            volver_home()
        else:
            mensaje.value = resultado["mensaje"]
            mensaje.color = ft.Colors.RED_400
            page.update()

    botones = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
        controls=[
            ft.ElevatedButton(
                "Guardar",
                icon=ft.Icons.SAVE,
                bgcolor=ft.Colors.GREEN_700,
                color=ft.Colors.WHITE,
                on_click=guardar,
            ),
            ft.OutlinedButton(
                "Cancelar",
                icon=ft.Icons.CANCEL,
                # [MODIFICADO] Llamamos a la función pasada por parámetro
                on_click=lambda e: volver_home(),
            ),
        ],
    )

    return ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20,
        controls=[
            ft.Icon(icon=ft.Icons.MOVIE_EDIT, size=70, color=ft.Colors.AMBER_400),
            ft.Text("Agregar Película", size=28, weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
            ft.Container(
                width=420,
                padding=20,
                bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
                border_radius=12,
                content=ft.Column(
                    spacing=16,
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    controls=[titulo, director, puntuacion, mensaje, botones],
                ),
            ),
        ],
    )