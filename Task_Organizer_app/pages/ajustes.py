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
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.icon(tag="chevron-down",color="#000000"),
                                background="#FFFFFF",
                                margin_left="16.1em"),
                        ),
                        rx.menu.content(
                            rx.menu.item(
                                rx.text("Español")),
                            rx.menu.item(
                                rx.text("Ingles")),
                        )
                    )
                    
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
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.icon(tag="chevron-down", color="#000000"),
                                background="#FFFFFF",
                                margin_left="14em"
                            ),
                        ),
                        rx.menu.content(
                            rx.menu.item(
                                rx.icon(tag="notebook-text",size=15),"Educacion"),
                            rx.menu.item(
                                rx.icon(tag="briefcase-business",size=15),"Trabajo"),
                            rx.menu.item(
                                rx.icon(tag="home",size=15),"Hogar"),
                            rx.menu.item(
                                rx.icon(tag="shopping-cart",size=15),"Compras"),
                        ),
                        #justify="between",
                        margin_top="2em"
                    ),
                    justify="between",
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