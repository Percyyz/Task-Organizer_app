import reflex as rx
from ..pages.state import AppState

def pantalla_principal()->rx.Component:
    return rx.box(
        rx.container(
            rx.hstack(
                rx.heading(rx.text("Mis tareas",font_size="2xl",color="#000000")),
                    rx.menu.root(
                        rx.menu.trigger(
                            rx.button(
                                rx.icon(tag="menu",color="#000000"),
                                background="#FFFFFF"),
                        ),
                        rx.menu.content(
                        rx.menu.item(
                            rx.icon(tag="home",size=15),"Pantalla principal"),
                        rx.menu.item(
                            rx.icon(tag="settings",size=15),"Ajustes",on_click=rx.redirect("/ajustes")),
                        rx.menu.item(
                            rx.icon(tag="square-check-big",size=15),"Tareas completadas",on_click=rx.redirect("/tareas_completadas")),
                        rx.menu.item(
                            rx.icon(tag="star",size=15),"Calificar aplicacion",on_click=rx.redirect("/calificar_aplicacion")),
                        ),
                    ),
                    justify="between",
                    margin_top="1em"
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
                margin_top="1em",
                margin_bottom="20px"
            ),
            rx.foreach(
                AppState.tareas,
                lambda tarea: rx.card(
                    rx.flex(
                        rx.checkbox(),
                        rx.text(tarea["nombre"], font_size="md", color="#000000"),
                        rx.text(tarea["descripcion"], font_size="md",color="#000000"), 
                        rx.text(tarea["fecha"], font_size="md",color="#000000"),
                        rx.hstack(
                            rx.menu.root(
                                rx.menu.trigger(
                                    rx.button(
                                        rx.icon(tag="pencil-line",color="#3D5AFE"),
                                        background="#FFFFFF"
                                    )
                                ),
                                rx.menu.content(
                                    rx.menu.item(
                                        "editar",
                                        on_click=lambda tarea=tarea:[
                                            AppState.seleccionar_tarea(tarea["nombre"]),
                                            rx.redirect("/editar_tarea"),
                                        ]
                                    )
                                ),
                            ),
                            rx.icon(
                                tag="trash-2",
                                color="#D50000",
                                on_click=lambda tarea=tarea: AppState.eliminar_tarea(tarea["nombre"])
                            ),
                            margin_left="auto",
                        ),
                        spacing="2",
                        align="center",
                    ),
                    color="#000000",
                    margin_bottom="5px",
                ),
            ),
            rx.box(
                rx.link(
                    rx.icon(tag="circle-plus", color="#D50000",size=50),
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
                margin_bottom="-5em"
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