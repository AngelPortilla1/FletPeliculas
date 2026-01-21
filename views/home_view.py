import flet as ft
from Services.pelicula_service import obtener_todos
from Services.pelicula_service import delete_movie


def home_view(page: ft.Page, refrescar_callback=None, editar_callback=None):  # ← Añadir parámetro

    def crear_tabla():
        """Crea o recrea la tabla con los datos actuales"""
        peliculas = obtener_todos()

        return ft.DataTable(
            border=ft.border.all(1, ft.Colors.GREY_700),
            border_radius=8,
            heading_row_color=ft.Colors.BLUE_GREY_700,
            heading_row_height=48,
            columns=[
                ft.DataColumn(ft.Text("ID", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Título", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Director", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Puntuación", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Acciones", weight=ft.FontWeight.BOLD)),
            ],
            rows=[
                ft.DataRow(
                    cells=[
                        ft.DataCell(ft.Text(str(p.id))),
                        ft.DataCell(ft.Text(p.titulo)),
                        ft.DataCell(ft.Text(p.director)),
                        ft.DataCell(ft.Text(str(p.puntuacion))),
                        ft.DataCell(
                            ft.Row(
                                spacing=0,
                                controls=[
                                    ft.IconButton(
                                        icon=ft.Icons.EDIT,
                                        tooltip="Editar",
                                        icon_color=ft.Colors.BLUE_400,  # Color para que resalte
                                        on_click=lambda e, pid=p.id: editar_callback(pid) if editar_callback else print("No hay función de edición")
                                        # Llamamos al callback con el ID
                                    ),
                                    ft.IconButton(
                                        icon=ft.Icons.DELETE,
                                        tooltip="Eliminar",
                                        icon_color=ft.Colors.RED_400,
                                        on_click=lambda e, pid=p.id, titulo=p.titulo:
                                        confirmar_eliminacion(pid, titulo)
                                    ),
                                ]
                            )
                        ),
                    ]
                )
                for p in peliculas
            ],
        )

    def actualizar_tabla():
        """Actualiza la tabla con los datos más recientes"""
        nueva_tabla = crear_tabla()
        tabla_container.content = nueva_tabla
        page.update()

    def confirmar_eliminacion(pelicula_id, titulo_pelicula):
        """Muestra diálogo de confirmación antes de eliminar"""

        def cerrar_dialogo(e):
            dialogo.open = False
            page.update()

        def eliminar_confirmado(e):
            # Cerrar el diálogo
            dialogo.open = False
            page.update()

            # Eliminar la película
            resultado = delete_movie(pelicula_id)

            # Mostrar mensaje de resultado
            if resultado["ok"]:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(resultado["mensaje"]),
                    bgcolor=ft.Colors.GREEN_700,
                )
            else:
                page.snack_bar = ft.SnackBar(
                    content=ft.Text(resultado["mensaje"]),
                    bgcolor=ft.Colors.RED_700,
                )
            page.snack_bar.open = True
            page.update()

            # Actualizar la tabla
            actualizar_tabla()

        dialogo = ft.AlertDialog(
            modal=True,
            title=ft.Text("Confirmar eliminación"),
            content=ft.Text(
                f"¿Estás seguro de que deseas eliminar la película '{titulo_pelicula}'?\n\n"
                "Esta acción no se puede deshacer."
            ),
            actions=[
                ft.TextButton("Cancelar", on_click=cerrar_dialogo),
                ft.TextButton(
                    "Eliminar",
                    on_click=eliminar_confirmado,
                    style=ft.ButtonStyle(color=ft.Colors.RED_400),
                ),
            ],
            actions_alignment=ft.MainAxisAlignment.END,
        )

        page.overlay.append(dialogo)
        dialogo.open = True
        page.update()

    header = ft.Row(
        alignment=ft.MainAxisAlignment.CENTER,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=16,
        controls=[
            ft.Icon(ft.Icons.MOVIE, size=56, color=ft.Colors.AMBER_400),
            ft.Text(
                "Flet Peliculas",
                size=30,
                weight=ft.FontWeight.BOLD,
                color=ft.Colors.WHITE,
            ),
        ],
    )

    subtitulo = ft.Text(
        "Listado de películas",
        size=18,
        color=ft.Colors.WHITE70,
        text_align=ft.TextAlign.CENTER,
    )

    # Container de la tabla (para poder actualizarlo)
    tabla_container = ft.Container(
        content=crear_tabla(),
        expand=True,
        padding=20,
        bgcolor=ft.Colors.BLUE_GREY_800,
        border_radius=10,
        alignment=ft.Alignment(0, 0)
    )

    contenido = ft.Column(
        expand=True,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=30,
        controls=[
            header,
            subtitulo,
            tabla_container,
        ],
    )

    return contenido