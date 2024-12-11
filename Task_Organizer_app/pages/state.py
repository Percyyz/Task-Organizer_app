import reflex as rx

class AppState(rx.State):

    tareas: list[dict] = []
    tarea_en_edicion:dict={}


    nombre_tarea: str = ""
    descripcion_tarea: str = ""
    fecha_tarea: str = ""

    def selecc_tarea(self, nombre: str):
        """Selecciona una tarea por nombre y muestra el modal."""
        self.tarea_seleccionada = next((tarea for tarea in self.tareas if tarea["nombre"] == nombre), {})
        self.mostrar_modal = True

    def cerrar_modal(self):
        """Cierra el modal."""
        self.mostrar_modal = False
        self.tarea_seleccionada = {}
    
    def seleccionar_tarea(self, nombre:str):
        self.tarea_en_edicion=next(
            (tarea for tarea in self.tareas if tarea["nombre"]==nombre),{}
        )

    def guardar_cambios_tarea(self,nuevo_nombre:str,nueva_descripcion:str,nueva_fecha:str):
        for tarea in self.tareas:
            if tarea==self.tarea_en_edicion:
                tarea["nombre"]=nuevo_nombre
                tarea["descripcion"]=nueva_descripcion
                tarea["fecha"]=nueva_fecha
                break
        self.tarea_en_edicion={}

    def eliminar_tarea(self, nombre_tarea: str):
        """Elimina una tarea de la lista por su nombre."""
        self.tareas = [tarea for tarea in self.tareas if tarea["nombre"] != nombre_tarea]


    def set_nombre_tarea(self, nombre: str):
        self.nombre_tarea = nombre

    def set_descripcion_tarea(self, descripcion: str):
        self.descripcion_tarea = descripcion

    def set_fecha_tarea(self, fecha: str):
        self.fecha_tarea = fecha


    def guardar_tarea(self):
 
        nueva_tarea = {
            "nombre": self.nombre_tarea,
            "descripcion": self.descripcion_tarea,
            "fecha": self.fecha_tarea,
        }
        self.tareas.append(nueva_tarea)


        self.nombre_tarea = ""
        self.descripcion_tarea = ""
        self.fecha_tarea = ""


        rx.redirect("/pantalla_principal")
