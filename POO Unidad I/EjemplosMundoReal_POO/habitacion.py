
# Archivo: habitacion.py
# Clase: Habitacion
# Descripción:
# Este archivo contiene la definición de la clase Habitacion,
# la cual representa una habitación dentro de un hotel.
# Elaborado por: Leiber Correa Bravo

class Habitacion:
    """
    Clase que modela una habitación de un hotel.
    """

    def __init__(self, numero, precio):
        """
        Constructor de la clase Habitacion.

        Parámetros:
        - numero: número identificador de la habitación
        - precio: costo de la habitación por noche
        """
        self.numero = numero
        self.precio = precio
        self.disponible = True  # Indica si la habitación está disponible

    def reservar(self):
        """
        Método que permite realizar la reserva de la habitación.
        Cambia el estado de la habitación a no disponible.
        """
        if self.disponible:
            self.disponible = False
            print(f"Habitación {self.numero} reservada con éxito.")
        else:
            print(f"Habitación {self.numero} no se encuentra disponible.")
