import reflex as rx

def calificar_aplicacion()->rx.Component:
    return rx.box(
        rx.container(
            rx.hstack(
                rx.link(
                    rx.icon(tag="arrow-left",color="#000000",margin_top="4px"),
                    href="/pantalla_principal",
                    margin_right="7em"
                ),
                rx.heading("califícanos",  
                margin_bottom="20px",
                color="#000000",
                ),
                margin_top="20px",
            ),
            rx.vstack(
                rx.text.strong("¿Cómo calificarías esta aplicación?",color="#000000"),
                rx.text("Tu opinion es importante para nosotros. Seleccione la cantidad de estrellas que refleje mejor tu experiencia y ayudanos a mejorar.",
                    color="#000000",
                    size="2"
                ),
                rx.hstack(
                    rx.icon(tag="star", color="#FFD700", size=30),
                    rx.icon(tag="star", color="#FFD700", size=30),
                    rx.icon(tag="star", color="#FFD700", size=30),
                    rx.icon(tag="star", color="#FFD700", size=30),
                    rx.icon(tag="star", color="#FFD700", size=30),
                    justify="center",
                    margin_top="20px",
                    margin_left="5em"
                ),
                rx.text.strong("¿Cómo fue tu experiencia?",color="#000000",margin_top="20px",),
                rx.text("Queremos hacer esta app perfecta para ti. Comparte cualquier idea, problema o comentario que tengas.",
                    color="#000000",
                    size="2"
                ),
                rx.text("Agrega un comentario...",margin_bottom="-13px",color="#000000",size="1",margin_top="20px",),
                rx.text_area(
                    color="#000000",
                    bg="#FFFFFF",
                    border="2px solid #1565C0",
                    width="100%",
                    height="150px",
                    margin_bottom="10px",
                ),
                rx.button(
                    "Enviar ahora",
                    color_scheme="blue",
                    width="100%",
                    margin_top="30px",
                ),
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