from tamagotchi import Tamagotchi

class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        print(f"\n{self.nombre} decide jugar con {self.tamagotchi.nombre}.")
        self.tamagotchi.jugar()
    
    def darle_comida(self):
        print(f"\n{self.nombre} le da de comer a {self.tamagotchi.nombre}.")
        self.tamagotchi.comer()
    
    def curarlo(self):
        print(f"\n{self.nombre} cuida y cura a {self.tamagotchi.nombre}.")
        self.tamagotchi.curar()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"