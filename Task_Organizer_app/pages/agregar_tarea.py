import reflex as rx

def agregar_tarea() -> rx.Component:
    return rx.box(
        rx.container(
            rx.heading("Agregar Tarea", size="xl", color="#000000", margin_bottom="20px"),))