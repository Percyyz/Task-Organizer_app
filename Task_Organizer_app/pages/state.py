import reflex as rx

class AppState(rx.State):
    # Lista de tareas
    tareas: list[dict] = []

    # Variables temporales para los datos de la nueva tarea
    nombre_tarea: str = ""
    descripcion_tarea: str = ""
    fecha_tarea: str = ""

    # Métodos para actualizar las variables temporales
    # ... Otros métodos y variables

    def eliminar_tarea(self, nombre_tarea: str):
        """Elimina una tarea de la lista por su nombre."""
        self.tareas = [tarea for tarea in self.tareas if tarea["nombre"] != nombre_tarea]


    def set_nombre_tarea(self, nombre: str):
        self.nombre_tarea = nombre

    def set_descripcion_tarea(self, descripcion: str):
        self.descripcion_tarea = descripcion

    def set_fecha_tarea(self, fecha: str):
        self.fecha_tarea = fecha

    # Método para guardar la tarea
    def guardar_tarea(self):
        # Crear una nueva tarea y agregarla a la lista
        nueva_tarea = {
            "nombre": self.nombre_tarea,
            "descripcion": self.descripcion_tarea,
            "fecha": self.fecha_tarea,
        }
        self.tareas.append(nueva_tarea)

        # Limpia los campos temporales
        self.nombre_tarea = ""
        self.descripcion_tarea = ""
        self.fecha_tarea = ""

        # Redirige a la pantalla principal
        rx.redirect("/pantalla_principal")
