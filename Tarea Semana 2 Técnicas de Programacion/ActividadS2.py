"""
Rediseño del proyecto aplicando:
- Abstracción
- Encapsulación
- Herencia
- Polimorfismo

Cada fórmula, cálculo y método incluye comentarios explicativos.
"""


# ==========================================================
# CLASE BASE: PERSONAJE (ABSTRACCIÓN Y ENCAPSULACIÓN)
# ==========================================================

class Personaje:
    """
    Representa un personaje genérico.
    Contiene atributos básicos y comportamientos comunes.
    """

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida):
        # Encapsulación: cada personaje tiene sus atributos
        self.nombre = nombre
        self.fuerza = fuerza
        self.inteligencia = inteligencia
        self.defensa = defensa
        self.vida = vida

    def atributos(self):
        """Muestra los atributos actuales del personaje."""
        print(self.nombre, ":", sep="")
        print("· Fuerza:", self.fuerza)
        print("· Inteligencia:", self.inteligencia)
        print("· Defensa:", self.defensa)
        print("· Vida:", self.vida)

    def subir_nivel(self, fuerza, inteligencia, defensa):
        """
        Incrementa atributos.
        Fórmulas:
        nueva_fuerza = fuerza_actual + subida
        nueva_inteligencia = inteligencia_actual + subida
        nueva_defensa = defensa_actual + subida
        """
        self.fuerza += fuerza
        self.inteligencia += inteligencia
        self.defensa += defensa

    def esta_vivo(self):
        """
        Fórmula:
        Un personaje está vivo si su vida es mayor a 0.
        return vida > 0
        """
        return self.vida > 0

    def morir(self):
        """Al morir la vida se pone en cero."""
        self.vida = 0
        print(self.nombre, "ha muerto")

    def daño(self, enemigo):
        """
        Fórmula básica de daño (se sobreescribe en subclases):
        daño = fuerza_atacante - defensa_enemigo
        """
        return self.fuerza - enemigo.defensa

    def atacar(self, enemigo):
        """
        Aplica daño al enemigo.

        1. Calcula daño con la fórmula definida en daño()
        2. Resta ese valor a la vida del enemigo.

        Fórmula:
        vida_enemigo = vida_enemigo - daño
        """

        daño = self.daño(enemigo)

        # Evitar daño negativo: si la defensa es mayor, daño = 0
        daño = max(0, daño)

        enemigo.vida -= daño

        print(f"{self.nombre} ha realizado {daño} puntos de daño a {enemigo.nombre}")

        # Mostrar vida restante o muerte
        if enemigo.esta_vivo():
            print(f"Vida de {enemigo.nombre}: {enemigo.vida}")
        else:
            enemigo.morir()


# ==========================================================
# SUBCLASE: GUERRERO (HERENCIA + POLIMORFISMO)
# ==========================================================

class Guerrero(Personaje):
    """Personaje especializado en ataques físicos con espada."""

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, espada):
        # Hereda atributos de Personaje
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.espada = espada  # fuerza multiplicadora del arma

    def cambiar_arma(self):
        """
        Cambia el arma del guerrero.
        Opción 1: Daño = 8
        Opción 2: Daño = 10
        """
        opcion = int(input("Elige un arma: (1) Acero Valyrio, daño 8. (2) Matadragones, daño 10: "))

        if opcion == 1:
            self.espada = 8
        elif opcion == 2:
            self.espada = 10
        else:
            print("Número inválido.")

    def atributos(self):
        """Muestra atributos normales + arma."""
        super().atributos()
        print("· Espada:", self.espada)

    def daño(self, enemigo):
        """
        POLIMORFISMO: redefinimos el cálculo de daño.

        Fórmula del daño del guerrero:
        daño = fuerza * espada - defensa_enemigo

        Donde:
        - fuerza: fuerza física del guerrero
        - espada: multiplicador del arma
        - defensa_enemigo: resta parte del daño final
        """
        return (self.fuerza * self.espada) - enemigo.defensa


# ==========================================================
# SUBCLASE: MAGO (HERENCIA + POLIMORFISMO)
# ==========================================================

class Mago(Personaje):
    """Personaje especializado en magia."""

    def __init__(self, nombre, fuerza, inteligencia, defensa, vida, libro):
        # Hereda de Personaje
        super().__init__(nombre, fuerza, inteligencia, defensa, vida)
        self.libro = libro  # multiplicador del daño mágico

    def atributos(self):
        """Muestra atributos normales + libro mágico."""
        super().atributos()
        print("· Libro mágico:", self.libro)

    def daño(self, enemigo):
        """
        POLIMORFISMO: el mago ataca distinto al guerrero.

        Fórmula del daño mágico:
        daño = inteligencia * libro - defensa_enemigo

        Donde:
        - inteligencia: atributo principal del mago
        - libro: potencia del hechizo
        """
        return (self.inteligencia * self.libro) - enemigo.defensa


# ==========================================================
# FUNCIÓN DE COMBATE
# ==========================================================

def combate(jugador_1, jugador_2):
    """
    Simula un combate por turnos.

    Cada turno:
    1. Ataca jugador_1
    2. Ataca jugador_2 (solo si sigue vivo)

    Finaliza cuando uno muere.

    """

    turno = 1

    while jugador_1.esta_vivo() and jugador_2.esta_vivo():

        print(f"\n=========== TURNO {turno} ===========")

        # Ataca jugador 1
        print(f">>> Acción de {jugador_1.nombre}:")
        jugador_1.atacar(jugador_2)

        # Si vive, ataca jugador 2
        if jugador_2.esta_vivo():
            print(f">>> Acción de {jugador_2.nombre}:")
            jugador_2.atacar(jugador_1)

        turno += 1

    print("\n=========== RESULTADO FINAL ===========")

    if jugador_1.esta_vivo():
        print("Ganador:", jugador_1.nombre)
    elif jugador_2.esta_vivo():
        print("Ganador:", jugador_2.nombre)
    else:
        print("Empate")


# ==========================================================
# OBJETOS Y EJECUCIÓN
# ==========================================================

if __name__ == "__main__":
    # Creamos personajes
    personaje_1 = Guerrero("Guts", 20, 10, 4, 100, 4)
    personaje_2 = Mago("Vanessa", 5, 15, 4, 100, 3)

    print("\n--- ATRIBUTOS INICIALES ---")
    personaje_1.atributos()
    personaje_2.atributos()

    # Iniciar combate
    combate(personaje_1, personaje_2)
