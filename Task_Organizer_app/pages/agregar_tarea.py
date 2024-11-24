import reflex as rx

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
            
            rx.input(placeholder="Nombre de la tarea", margin_bottom="10px",bg="#757575"),
            rx.text_area(placeholder="Descripción de la tarea", margin_bottom="10px",bg="#757575"),
            rx.input(type="date", margin_bottom="20px",bg="#757575"),
            rx.link(
                rx.button(
                "Guardar Tarea",
                background_color="#28a745",
                color="#FFFFFF",
                padding="10px",
                width="100%",
                margin_bottom="20px",
                border_radius="5px",
                ),
                href="/pantalla_principal"
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
            ),
            padding="16px",
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