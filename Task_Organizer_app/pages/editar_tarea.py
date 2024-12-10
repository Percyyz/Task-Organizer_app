import reflex as rx
from ..pages.state import AppState

def editar_tarea() -> rx.Component:
    return rx.box(
        rx.container(
            rx.heading("Editar Tarea",align="center", size="xl", margin_bottom="20px", color="#000000"),
            rx.input(
                AppState.tarea_en_edicion["nombre"],
                #placeholder="Nombre de la tarea",
                on_change=AppState.set_nombre_tarea,
                margin_bottom="10px",
                width="100%",
                color="#000000",
                bg="#FFFFFF",
                border="2px solid #1565C0"
            ),
            rx.button(
                "Guardar cambios",
                on_click=lambda: AppState.guardar_cambios_tarea(
                    AppState.nombre_tarea, AppState.descripcion_tarea, AppState.fecha_tarea
                ),
                background_color="#28a745",
                color="#FFFFFF",
                width="100%",
                margin_bottom="10px",
                on_double_click=rx.redirect("/pantalla_principal")
            ),
            # rx.link(
            #     "Cancelar",
            #     href="/pantalla_principal",
            #     color="#D50000",
            # ),
            width="90%",
            max_width="400px",
            background_color="#FFFFFF",
            border_radius="8px",
            box_shadow="md",
        ),
        height="100vh",
        background_color="#f9f9f9",
        display="flex",
        justify_content="center",
        align_items="center",
    )
