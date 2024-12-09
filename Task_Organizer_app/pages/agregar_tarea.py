import reflex as rx
from ..pages.state import AppState

def agregar_tarea() -> rx.Component:
    return rx.box(
        rx.container(
            rx.heading(
                rx.text("Agregar Tarea"), 
                size="xl", 
                color="#000000", 
                margin_bottom="40px",
                align="center",
            ),
            rx.vstack(
                rx.text("Nombre de la tarea",margin_bottom="-13px",color="#000000",size="1"),
                rx.input(
                width="100%",
                color="#000000",
                bg="#FFFFFF",
                margin_bottom="10px",
                border="2px solid #1565C0",
                on_change=AppState.set_nombre_tarea),

            rx.text("Descripcion de la tarea",margin_bottom="-13px",color="#000000",size="1"),    
            rx.text_area(
                width="100%",
                color="#000000",
                bg="#FFFFFF",
                margin_bottom="10px",
                border="2px solid #1565C0"),
            
            rx.text("Establecer fecha",margin_bottom="-13px",color="#000000",size="1"),
            rx.input(
                type="date", 
                margin_bottom="20px",
                bg="#757575",
                width="100%",
            ),
            
            rx.flex(
                rx.link(
                rx.button(
                "Guardar",
                background_color="#28a745",
                color="#FFFFFF",
                width="100%",
                margin_bottom="5px",
                border_radius="5px",
                on_click=AppState.guardar_tarea,
                ),
                href="/pantalla_principal",
                width="100%"
            ),
            rx.link(
                rx.button(
                    "Cancelar",
                    background_color="#D50000",
                    color="#FFFFFF",
                    width="100%",
                    border_radius="5px",
                    ),
                    href="/pantalla_principal",
                    width="100%"
                    ),
                spacing="2",
                justify="center",
                margin_left="6em"
                ),
            ),
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