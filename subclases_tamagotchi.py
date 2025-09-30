from tamagotchi import Tamagotchi

class Mametchi(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)
    
    def inventar(self):
        if not self.esta_vivo:
            print(f"{self.nombre} no puede inventar, está muerto.")
            return
            
        self.felicidad += 15
        self.energia -= 10
        print(f"\n¡{self.nombre} ha inventado algo nuevo!")
        self._actualizar_stats()
        if self.esta_vivo:
            print(f"Su felicidad es {self.felicidad} y su energía {self.energia}.")

class Pochitchi(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)

    def conducir(self):
        if not self.esta_vivo:
            print(f"{self.nombre} no puede conducir, está muerto.")
            return

        self.felicidad += 10
        self.energia -= 5
        print(f"\n¡{self.nombre} ha salido a conducir!")
        self._actualizar_stats()
        if self.esta_vivo:
            print(f"Su felicidad es {self.felicidad} y su energía {self.energia}.")