class Tamagotchi:
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.salud = 100
        self.felicidad = 50
        self.energia = 100
        self.esta_vivo = True

    def _actualizar_stats(self):
        self.salud = min(100, self.salud)
        self.felicidad = min(100, self.felicidad)
        self.energia = min(100, self.energia)

        if self.salud <= 0:
            self.esta_vivo = False
            print(f"\n¡Oh no! {self.nombre} se ha quedado sin salud y ha muerto. 😢")

    def jugar(self):
        if not self.esta_vivo:
            print(f"{self.nombre} no puede jugar, está muerto.")
            return

        self.felicidad += 10
        self.salud -= 5
        print(f"\n¡Has jugado con {self.nombre}!")
        self._actualizar_stats()
        if self.esta_vivo:
            print(f"Su felicidad es {self.felicidad} y su salud {self.salud}.")

    def comer(self):
        if not self.esta_vivo:
            print(f"{self.nombre} no puede comer, está muerto.")
            return
            
        self.felicidad += 5
        self.salud += 10
        print(f"\n¡{self.nombre} ha comido!")
        self._actualizar_stats()
        if self.esta_vivo:
            print(f"Su felicidad es {self.felicidad} y su salud {self.salud}.")

    def curar(self):
        if not self.esta_vivo:
            print(f"{self.nombre} no puede ser curado, está muerto.")
            return

        self.salud += 20
        self.felicidad -= 5
        print(f"\n¡Has curado a {self.nombre}!")
        self._actualizar_stats()
        if self.esta_vivo:
            print(f"Su salud es {self.salud} y su felicidad {self.felicidad}.")

    def __str__(self):
       estado = "Vivo" if self.esta_vivo else "Muerto"
       return f"\n--- Estado de {self.nombre} ---\nEstado: {estado}\nColor: {self.color}\nSalud: {self.salud}\nFelicidad: {self.felicidad}\nEnergía: {self.energia}\n"