
# Archivo: main.py
# Programa principal
# Descripción:
# Este archivo ejecuta el sistema de reservas, creando los
# objetos necesarios y demostrando la interacción entre ellos.


from hotel import Hotel
from habitacion import Habitacion

# Creación del objeto Hotel
hotel = Hotel("Hotel Central")

# Creación de objetos Habitacion
habitacion1 = Habitacion(101, 50)
habitacion2 = Habitacion(102, 60)

# Asociación de las habitaciones al hotel
hotel.agregar_habitacion(habitacion1)
hotel.agregar_habitacion(habitacion2)

# Muestra el estado inicial de las habitaciones
hotel.mostrar_habitaciones()

# Reserva de una habitación
habitacion1.reservar()

# Muestra el estado final de las habitaciones
hotel.mostrar_habitaciones()
