
# Programa: Cálculo del área de un rectángulo
# Descripción:
# Este programa solicita al usuario el largo y el ancho de un rectángulo,
# calcula su área y verifica si el resultado es válido.
# Aplicable al cálculo de áreas en arquitectura.
# Creado por el alumno: Leiber Correa

# Se solicita al usuario el largo del rectángulo y se convierte a tipo float
largo = float(input("Ingrese el largo del rectángulo: "))

# Se solicita al usuario el ancho del rectángulo y se convierte a tipo float
ancho = float(input("Ingrese el ancho del rectángulo: "))

# Se calcula el área del rectángulo multiplicando largo por ancho
area_rectangulo = largo * ancho

# Se evalúa si el área calculada es mayor que cero (variable booleana)
area_valida = area_rectangulo > 0

# Se muestra el área calculada en pantalla
print("El área del rectángulo es:", area_rectangulo)

# Estructura condicional para validar el resultado del cálculo
if area_valida:
    # Mensaje cuando el área es correcta
    print("El área calculada es válida.")
else:
    # Mensaje cuando el área no es correcta
    print("El área calculada no es válida.")
