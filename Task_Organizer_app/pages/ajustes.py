import reflex as rx

def ajustes() -> rx.Component:
    return rx.box(
        rx.container(
            rx.hstack(
                rx.link(
                    rx.icon(tag="arrow-left",color="#000000",margin_top="4px"),
                    href="/pantalla_principal",
                    margin_right="6.5em"
                ),
                rx.heading("Ajustes",  
                    margin_bottom="20px",
                    color="#000000",
                ),
                margin_top="20px",
            ),
            rx.text("Aquí puedes configurar los ajustes de la aplicación.",
                align="center",
                color="#000000",
                
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