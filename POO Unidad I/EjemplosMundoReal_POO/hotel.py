
# Archivo: hotel.py
# Clase: Hotel
# Descripción:
# Este archivo define la clase Hotel, encargada de gestionar
# las habitaciones y su estado dentro del sistema.




class Hotel:
    """
    Clase que representa un hotel y administra sus habitaciones.
    """

    def __init__(self, nombre):
        """
        Constructor de la clase Hotel.

        Parámetros:
        - nombre: nombre del hotel
        """
        self.nombre = nombre
        self.habitaciones = []  # Lista de objetos Habitacion

    def agregar_habitacion(self, habitacion):
        """
        Método que agrega una habitación al hotel.

        Parámetros:
        - habitacion: objeto de la clase Habitacion
        """
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones(self):
        """
        Método que muestra el estado actual de todas
        las habitaciones del hotel.
        """
        print(f"\nEstado de habitaciones del {self.nombre}:")
        for hab in self.habitaciones:
            estado = "Disponible" if hab.disponible else "Ocupada"
            print(f"Habitación {hab.numero} - {estado}")
