import reflex as rx

def registro() -> rx.Component:
    return rx.box(
        rx.container(
            rx.heading(
                rx.text("Registrarse"),
                align="center",
                color="#000000",
                size="xl",
                margin_bottom="40px",
                margin_top="-30px",
            ),
            rx.hstack(
                rx.input(
                placeholder="Nombre",
                width="48%",
                paddin="8px",
                margin_top="10px",
                ),
            rx.input(
                placeholder="Apellido",
                width="48%",
                paddin="8px",
                margin_top="10px",
                ),
                spacing="4",
                margin_top="10px",
            ),
            rx.input(
                placeholder="Correo electrónico",
                margin_top="10px",
            ),
            rx.input(
                placeholder="Contraseña",
                type="password",
                margin_top="10px",
            ),
            rx.input(
                placeholder="Validar Contraseña",
                type="password",
                margin_top="10px",
            ),
            rx.button(
                "Registrarse",
                background_color="#28a745",
                color="#ffffff",
                padding="12px",
                border_radius="8px",
                width="100%",
                align_self="center",
                margin_top="40px",
            ),
            padding="16px",
            width="90%",
            max_width="400px",
            background_color="#ffffff",
            border_radius="8px",
            box_shadow="md",
        ),
        height="100vh",
        background_color="#f9f9f9",
        display="flex",
        justify_content="center",
        align_items="center",
    )
