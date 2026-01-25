import flet as ft
from Services.pelicula_service import crear, actualizar, obtener_por_id


def form_view(page: ft.Page, volver_home, pelicula_id=None):
    es_edicion = pelicula_id is not None

    # Referencia al botón para manipularlo dinámicamente
    btn_guardar = ft.ElevatedButton(
        "Actualizar" if es_edicion else "Guardar",
        bgcolor=ft.Colors.GREEN_700,
        color=ft.Colors.WHITE,
        disabled=True,  # Empieza deshabilitado
    )

    def validar_interfaz(e):
        """Revisa los campos y actualiza el estado visual y del botón."""
        # Resetear errores previos
        puntuacion_input.error_text = None

        # Validar Título y Director
        hay_titulo = bool(titulo_input.value.strip())
        hay_director = bool(director_input.value.strip())

        # Validar Puntuación
        puntuacion_valida = False
        val = puntuacion_input.value.strip()

        if not val:
            puntuacion_input.error_text = "La puntuación es requerida"
        elif not val.isdigit():
            puntuacion_input.error_text = "Debe ser un número entero"
        elif not (1 <= int(val) <= 10):
            puntuacion_input.error_text = "Rango permitido: 1 a 10"
        else:
            puntuacion_valida = True
            puntuacion_input.error_text = None

        # Habilitar botón solo si todo está OK
        btn_guardar.disabled = not (hay_titulo and hay_director and puntuacion_valida)
        page.update()

    # Inputs con el evento on_change activado
    titulo_input = ft.TextField(
        label="Título", expand=True, on_change=validar_interfaz
    )
    director_input = ft.TextField(
        label="Director", expand=True, on_change=validar_interfaz
    )
    puntuacion_input = ft.TextField(
        label="Puntuación (1-10)",
        expand=True,
        keyboard_type=ft.KeyboardType.NUMBER,
        on_change=validar_interfaz,

    )
    puntuacion_helper = ft.Text(
        "Ingresa un valor entre 1 y 10",
        size=12,
        color=ft.Colors.GREY_600
    )

    if es_edicion:
        peli = obtener_por_id(pelicula_id)
        if peli:
            titulo_input.value = peli.titulo
            director_input.value = peli.director
            puntuacion_input.value = str(peli.puntuacion)
            # Al cargar datos, validamos para habilitar el botón
            btn_guardar.disabled = False

    def ejecutar_guardado(e):
        datos = {
            "titulo": titulo_input.value,
            "director": director_input.value,
            "puntuacion": puntuacion_input.value
        }

        resultado = actualizar(pelicula_id, datos) if es_edicion else crear(datos)

        if resultado["ok"]:
            # SnackBar de éxito
            snack = ft.SnackBar(
                ft.Text(resultado["mensaje"]),
                bgcolor=ft.Colors.GREEN_800,
                action="OK"
            )
            page.overlay.append(snack)
            snack.open = True
            volver_home()
        else:
            # SnackBar de error
            snack = ft.SnackBar(
                ft.Text(resultado["mensaje"]),
                bgcolor=ft.Colors.RED_800
            )
            page.overlay.append(snack)
            snack.open = True
            page.update()

    btn_guardar.on_click = ejecutar_guardado

    # UI principal
    return ft.Container(
        expand=True,
        content=ft.Column(
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            controls=[
                ft.Icon(
                    ft.Icons.EDIT_SQUARE if es_edicion else ft.Icons.MOVIE_FILTER,
                    size=70, color=ft.Colors.AMBER_400
                ),
                ft.Text(
                    "Editar Película" if es_edicion else "Nueva Película",
                    size=28, weight="bold"
                ),
                ft.Container(
                    width=450,
                    padding=30,
                    bgcolor=ft.Colors.with_opacity(0.05, ft.Colors.WHITE),
                    border_radius=15,
                    border=ft.border.all(1, ft.Colors.WHITE24),
                    content=ft.Column([
                        titulo_input,
                        director_input,
                        puntuacion_input,
                        puntuacion_helper,
                        ft.Divider(height=20, color="transparent"),
                        ft.Row([
                            btn_guardar,
                            ft.OutlinedButton("Cancelar", on_click=lambda _: volver_home())
                        ], alignment="center", spacing=20)
                    ])
                )
            ]
        )
    )