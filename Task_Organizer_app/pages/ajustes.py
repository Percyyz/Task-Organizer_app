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
                margin_bottom="20px",
            ),
            
            rx.vstack(
                rx.hstack(
                    rx.icon(tag="calendar-x", color="#F9A825", size=24),
                    rx.text("Transferencia automatica de tareas atrasadas", color="#000000", size="md"),
                    rx.switch(color="#4CAF50"),
                    align_items="center",
                ),
                rx.divider(color="#000000"),
                rx.hstack(
                    rx.icon(tag="globe", color="#F9A825", size=24),
                    rx.text("Idioma", color="#000000", size="md"),
                    rx.link(
                        rx.icon(tag="chevron-right", color="#000000"),
                        href="",
                        margin_left="15em"
                    ),
                    
                ),
                rx.divider(color="#000000"),
                rx.hstack(
                    rx.icon(tag="moon", color="#F9A825", size=24),
                    rx.text("Modo oscuro", color="#000000", size="md"),
                    rx.color_mode.button(margin_left="11.5em")
                    # rx.segmented_control.root(
                    #     rx.segmented_control.item(
                    #     rx.icon(tag="sun", size=20),
                    #     value="light",
                    #     ),
                    #     rx.segmented_control.item(
                    #     rx.icon(tag="moon", size=20),
                    #     value="dark",
                    #     ),
                    # )
                    
                    # rx.switch(color="#4CAF50",margin_left="11.7em"),
                    # align_items="center",
                ),
                rx.divider(color="#000000"),
                rx.hstack(
                    rx.icon(tag="bell",color="#F9A825",size=24),
                    rx.text("Notificacion",color="#000000", size="md"),
                    rx.link(
                        rx.icon(tag="chevron-right", color="#000000"),
                        href="",
                        margin_left="12.5em"
                    )
                ),
                rx.divider(color="#000000"),
                rx.hstack(
                    rx.icon(tag="cloud-upload",color="#F9A825",size=24),
                    rx.text("Copia de seguridad",color="#000000", size="md"),
                    rx.link(
                        rx.icon(tag="chevron-right", color="#000000"),
                        href="",
                        margin_left="9.2em"
                    )
                ),
                rx.divider(color="#000000"),
                rx.hstack(
                    rx.icon(tag="list",color="#F9A825",size=24),
                    rx.text("categorias",color="#000000", size="md"),
                    rx.link(
                        rx.icon(tag="chevron-right", color="#000000"),
                        href="",
                        margin_left="13.2em"
                    )
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