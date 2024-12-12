import reflex as rx
from ..pages.state import AppState

def tareas_completadas()->rx.Component:
    return rx.box(
        rx.container(
            rx.hstack(
                rx.link(
                    rx.icon(tag="arrow-left",color="#000000",margin_top="4px"),
                    href="/pantalla_principal",
                    margin_right="3em"
                ),
                rx.heading("Tareas completadas",  
                    margin_bottom="20px",
                    color="#000000",
                ),
                margin_top="20px",
            ),
            rx.foreach(
                AppState.tareas_completadas,
                lambda tarea: rx.card(
                    rx.flex(
                       rx.text(tarea["nombre"], font_size="md", color="#000000"),
                       spacing="2",
                       align="center" 
                    ),
                    color="#000000",
                    margin_bottom="5px",
                )
            ),
            width="90%",
            max_width="400px",
            background_color="#FFFFFF", 
            border_radius="8px",
            box_shadow="md"
        ),
        height="100vh",
        background_color="#f9f9f9",
        display="flex",
        justify_content="center",
        aling_items="center"
    )