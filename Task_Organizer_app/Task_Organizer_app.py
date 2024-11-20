"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

# Importar las interfaces de las páginas
from .pages.inicio import inicio
from .pages.registro import registro

# Crear la instancia de la aplicación
app = rx.App()

# Configurar las rutas de la aplicación
app.add_page(route="/", component=inicio)
app.add_page(route="/registro", component=registro)
