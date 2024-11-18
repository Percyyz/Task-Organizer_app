"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx
from .componentes.inicio import inicio

def index()->rx.Component:
    return rx.box(
        inicio()
    )


app = rx.App()
app.add_page(index)
