import reflex as rx

def pantalla_principal()->rx.Component:
    return rx.box(
        rx.container(
            rx.hstack(
                rx.link(
                    rx.icon(tag="menu",color="#000000"),
                    href=""
                ),
                rx.spacer(width="100%"),
                rx.link(
                    rx.icon(tag="settings",color="#000000"),
                    href=""
                ),
                justify="start",
                width="98%",
                padding="10px",
            ),
            rx.box(
                rx.hstack(
                    rx.text("TAREAS",font_size="18px",font_weight="bold",color="#FFFFFF"),
                rx.hstack(
                    rx.text("0",font_size="18px",font_weight="bold",color="#FFFFFF"),
                    align="center",
                    justify="end",
                    width="100%",
                    ),
                ),
                background_color="#28a745",
                width="100%",
                padding="10px",
                margin_top="2em",
                margin_bottom="20px"
            ),
            
            rx.card(
                rx.flex(
                    rx.checkbox(),
                    "Tarea 1",
                    rx.hstack(
                        rx.link( rx.icon(tag="pencil-line",color="#3D5AFE"),href=""),
                        rx.link(rx.icon(tag="trash-2",color="#D50000"),href=""),
                        margin_left="13em"
                    )
                ),
                color="#000000",
                margin_bottom="5px"
            ),
            rx.card(
                rx.flex(
                    "Tarea 2",
                    rx.hstack(
                        rx.link( rx.icon(tag="pencil-line",color="#3D5AFE"),href=""),
                        rx.link(rx.icon(tag="trash-2",color="#D50000"),href=""),
                        margin_left="14em"
                    )
                ),
                color="#000000",
                margin_bottom="5px"
            ),
            rx.card(
                rx.flex(
                    "Tarea 3",
                    rx.hstack(
                        rx.link( rx.icon(tag="pencil-line",color="#3D5AFE"),href=""),
                        rx.link(rx.icon(tag="trash-2",color="#D50000"),href=""),
                        margin_left="14em"
                    )
                ),
                color="#000000"
            ),
            
            rx.box(
                rx.link(
                    rx.icon(tag="circle-plus", color="#D50000"),
                    href="/agregar_tarea"
                ),
                width="100px",
                height="200px",
                display="flex",
                justify_content="center",
                align_items="center",
                position="fixed",
                bottom="40px",
                right="10px",
            ),
            padding="16px",
            width="90%",
            max_width="400px",
            height="85vh",
            background_color="#FFFFFF",    
        ),
        height="735px",
        background_color="#f9f9f9",
        display="flex",
        justify_content="center",
    )