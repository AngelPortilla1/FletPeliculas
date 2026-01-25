import flet as ft
from Services.pelicula_service import crear, actualizar, obtener_por_id


def form_view(page: ft.Page, volver_home, pelicula_id=None):

    es_edicion = pelicula_id is not None

    titulo_input = ft.TextField(
        label="Título",
        expand=True,
        error_style=ft.TextStyle(
            color=ft.Colors.RED_400,
            size=12
        )
    )

    director_input = ft.TextField(
        label="Director",
        expand=True,
        error_style=ft.TextStyle(color=ft.Colors.RED_400, size=12)
    )

    puntuacion_input = ft.TextField(
        label="Puntuación (1-10)",
        expand=True,
        keyboard_type=ft.KeyboardType.NUMBER,
        error_style=ft.TextStyle(color=ft.Colors.RED_400, size=12)
    )

    btn_guardar = ft.ElevatedButton(
        "Actualizar" if es_edicion else "Guardar",
        icon=ft.Icons.SAVE,
        bgcolor=ft.Colors.GREEN_700,
        color=ft.Colors.WHITE,
        disabled=True
    )

    # Prellenado en edición
    if es_edicion:
        peli = obtener_por_id(pelicula_id)
        if peli:
            titulo_input.value = peli.titulo
            director_input.value = peli.director
            puntuacion_input.value = str(peli.puntuacion)

    def validar_interfaz(e=None):
        # Reset errores
        titulo_input.error_text = None
        director_input.error_text = None
        puntuacion_input.error_text = None

        hay_titulo = False
        hay_director = False
        puntuacion_ok = False

        # --- TÍTULO ---
        titulo = titulo_input.value.strip()
        if not titulo:
            titulo_input.error_text = "El título no puede estar vacío"
        elif titulo.isdigit():
            titulo_input.error_text = "El título no puede ser solo números"
        else:
            hay_titulo = True

        # --- DIRECTOR ---
        director = director_input.value.strip()
        if not director:
            director_input.error_text = "El director no puede estar vacío"
        elif director.isdigit():
            director_input.error_text = "El director no puede ser solo números"
        else:
            hay_director = True

        # --- PUNTUACIÓN ---
        val = puntuacion_input.value.strip()
        if not val:
            puntuacion_input.error_text = "Ingrese un número del 1 al 10"
        elif not val.isdigit():
            puntuacion_input.error_text = "Debe ser un número entero"
        elif not (1 <= int(val) <= 10):
            puntuacion_input.error_text = "Rango permitido: 1 a 10"
        else:
            puntuacion_ok = True

        es_valido = hay_titulo and hay_director and puntuacion_ok

        btn_guardar.disabled = not es_valido
        btn_guardar.bgcolor = (
            ft.Colors.GREEN_700 if es_valido else ft.Colors.GREY_600
        )

        page.update()

    def guardar(e):
        datos = {
            "titulo": titulo_input.value,
            "director": director_input.value,
            "puntuacion": puntuacion_input.value
        }

        resultado = actualizar(pelicula_id, datos) if es_edicion else crear(datos)

        if resultado["ok"]:
            snack = ft.SnackBar(
                ft.Text(resultado["mensaje"]),
                bgcolor=ft.Colors.GREEN_800
            )
            page.overlay.append(snack)
            snack.open = True
            volver_home()
        else:
            snack = ft.SnackBar(
                ft.Text(resultado["mensaje"]),
                bgcolor=ft.Colors.RED_700
            )
            page.overlay.append(snack)
            snack.open = True

    btn_guardar.on_click = guardar
    # Conectar validación dinámica
    titulo_input.on_change = validar_interfaz
    director_input.on_change = validar_interfaz
    puntuacion_input.on_change = validar_interfaz

    # Validación inicial (edición o formulario vacío)
    validar_interfaz()

    validar_interfaz()
    return ft.Column(
        expand=True,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(
                ft.Icons.EDIT_SQUARE if es_edicion else ft.Icons.MOVIE_EDIT,
                size=70,
                color=ft.Colors.AMBER_400
            ),
            ft.Text(
                "Editar Película" if es_edicion else "Agregar Película",
                size=28,
                weight="bold"
            ),
            ft.Container(
                width=420,
                padding=20,
                bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
                border_radius=12,
                content=ft.Column(
                    spacing=12,
                    controls=[
                        titulo_input,
                        director_input,
                        puntuacion_input,
                        ft.Row(
                            alignment="center",
                            spacing=20,
                            controls=[
                                btn_guardar,
                                ft.OutlinedButton(
                                    "Cancelar",
                                    icon=ft.Icons.CANCEL,
                                    on_click=lambda _: volver_home()
                                )
                            ]
                        )
                    ]
                )
            )
        ]
    )
