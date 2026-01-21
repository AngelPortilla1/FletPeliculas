import flet as ft
from Services.pelicula_service import crear, actualizar, obtener_por_id


# [MODIFICADO] Añadimos el parámetro 'volver_home'
def form_view(page: ft.Page, volver_home, pelicula_id=None):
    # Variables de control
    es_edicion = pelicula_id is not None
    titulo_input = ft.TextField(label="Título", expand=True)
    director_input = ft.TextField(label="Director", expand=True)
    puntuacion_input = ft.TextField(label="Puntuación (0-10)", expand=True, keyboard_type=ft.KeyboardType.NUMBER)

    # [NUEVO] Si es edición, pre-llenamos los campos
    if es_edicion:
        peli = obtener_por_id(pelicula_id)
        if peli:
            titulo_input.value = peli.titulo
            director_input.value = peli.director
            puntuacion_input.value = str(peli.puntuacion)

    mensaje = ft.Text(color=ft.Colors.RED_400, text_align=ft.TextAlign.CENTER)

    def guardar(e):
        datos = {
            "titulo": titulo_input.value.strip(),
            "director": director_input.value.strip(),
            "puntuacion": int(puntuacion_input.value) if puntuacion_input.value.isdigit() else -1
        }

        # Validación rápida
        if not datos["titulo"] or not datos["director"]:
            mensaje.value = "Campos obligatorios vacíos";
            page.update();
            return

        # Decidir si CREAR o ACTUALIZAR
        if es_edicion:
            resultado = actualizar(pelicula_id, datos)
        else:
            resultado = crear(datos)

        if resultado["ok"]:
            snack = ft.SnackBar(ft.Text(resultado["mensaje"]), bgcolor=ft.Colors.GREEN_800)
            page.overlay.append(snack)
            snack.open = True
            volver_home()  # Regresar al home
        else:
            mensaje.value = resultado["mensaje"]
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
        expand=True, horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        controls=[
            ft.Icon(ft.Icons.EDIT_SQUARE if es_edicion else ft.Icons.MOVIE_EDIT, size=70, color=ft.Colors.AMBER_400),
            ft.Text("Editar Película" if es_edicion else "Agregar Película", size=28, weight="bold"),
            ft.Container(
                width=420, padding=20, bgcolor=ft.Colors.with_opacity(0.15, ft.Colors.WHITE),
                border_radius=12,
                content=ft.Column([
                    titulo_input, director_input, puntuacion_input, mensaje,
                    ft.Row([
                        ft.ElevatedButton("Actualizar" if es_edicion else "Guardar", on_click=guardar,
                                          bgcolor=ft.Colors.GREEN_700, color=ft.Colors.WHITE),
                        ft.OutlinedButton("Cancelar", on_click=lambda _: volver_home())
                    ], alignment="center")
                ])
            )
        ]
    )