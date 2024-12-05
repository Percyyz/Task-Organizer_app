"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

# Importar las interfaces de las páginas
from .pages.inicio import inicio
from .pages.registro import registro
from .pages.pantalla_principal import pantalla_principal
from .pages.agregar_tarea import agregar_tarea
from .pages.ajustes import ajustes
from .pages.tareas_completadas import tareas_completadas
from .pages.calificar_aplicacion import calificar_aplicacion

# Crear la instancia de la aplicación
app = rx.App()

# Configurar las rutas de la aplicación
app.add_page(route="/", component=inicio)
app.add_page(route="/registro", component=registro)
app.add_page(route="/pantalla_principal", component=pantalla_principal)
app.add_page(route="/agregar_tarea",component=agregar_tarea)
app.add_page(route="/ajustes",component=ajustes)
app.add_page(route="/tareas_completadas",component=tareas_completadas)
app.add_page(route="/calificar_aplicacion",component=calificar_aplicacion)