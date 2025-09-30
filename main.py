from persona import Persona
from tamagotchi import Tamagotchi
from subclases_tamagotchi import Mametchi, Pochitchi

def mostrar_menu():
    print("\n╔═════════════════════════════════╗")
    print("║        MENÚ PRINCIPAL           ║")
    print("╠═════════════════════════════════╣")
    print("║ 1. Crear un nuevo Tamagotchi    ║")
    print("║ 2. Jugar con Tamagotchi         ║")
    print("║ 3. Darle de comer               ║")
    print("║ 4. Curar al Tamagotchi          ║")
    print("║ 5. Usar habilidad especial      ║")
    print("║ 6. Ver estado del Tamagotchi    ║")
    print("║ 7. Salir                        ║")
    print("╚═════════════════════════════════╝")
    return input("Elige una opción: ")

def crear_nuevo_ciclo():
    print("\n--- Creación de un Nuevo Tamagotchi ---")
    
    nombre_persona = input("¿Cuál es tu nombre? ")
    apellido_persona = input("¿Y tu apellido? ")

    mi_tamagotchi = None
    while mi_tamagotchi is None:
        print("\nElige tu tipo de Tamagotchi:")
        print("  1. Tamagotchi Normal")
        print("  2. Mametchi (Inventor)")
        print("  3. Pochitchi (Conductor)")
        tipo = input("Opción: ")
        
        if tipo in ["1", "2", "3"]:
            nombre_tamagotchi = input("Ingresa el nombre de tu Tamagotchi: ")
            color_tamagotchi = input(f"Ingresa el color de {nombre_tamagotchi}: ")

            if tipo == "1":
                mi_tamagotchi = Tamagotchi(nombre_tamagotchi, color_tamagotchi)
            elif tipo == "2":
                mi_tamagotchi = Mametchi(nombre_tamagotchi, color_tamagotchi)
            elif tipo == "3":
                mi_tamagotchi = Pochitchi(nombre_tamagotchi, color_tamagotchi)
        else:
            print("Opción no válida.")
    
    dueño = Persona(nombre_persona, apellido_persona, mi_tamagotchi)
    print(f"\n¡Felicidades! {dueño} ha adoptado a {mi_tamagotchi.nombre}.")
    print(dueño.tamagotchi)
    return dueño

print("¡Bienvenido al simulador de Tamagotchi!")
dueño = None

while True:
    opcion = mostrar_menu()

    if opcion == '1':
        dueño = crear_nuevo_ciclo()

    elif opcion == '7':
        print("\nGracias por jugar. ¡Adiós!")
        break

    elif dueño and dueño.tamagotchi and dueño.tamagotchi.esta_vivo:
        if opcion == '2':
            dueño.jugar_con_tamagotchi()
        elif opcion == '3':
            dueño.darle_comida()
        elif opcion == '4':
            dueño.curarlo()
        elif opcion == '5':
            if isinstance(dueño.tamagotchi, Mametchi):
                dueño.tamagotchi.inventar()
            elif isinstance(dueño.tamagotchi, Pochitchi):
                dueño.tamagotchi.conducir()
            else:
                print(f"\n{dueño.tamagotchi.nombre} no tiene una habilidad especial.")
        elif opcion == '6':
            print(dueño.tamagotchi)
        else:
            print("\nOpción no válida. Inténtalo de nuevo.")
        
        if not dueño.tamagotchi.esta_vivo:
            print("\nTu Tamagotchi ha muerto. Puedes crear uno nuevo o salir.")

    elif opcion in ['2', '3', '4', '5', '6']:
        if dueño and dueño.tamagotchi and not dueño.tamagotchi.esta_vivo:
            print(f"\nNo puedes interactuar con {dueño.tamagotchi.nombre} porque ha muerto. Por favor, crea uno nuevo.")
        else:
            print("\nNo tienes un Tamagotchi. Por favor, crea uno nuevo usando la opción 1.")
    
    else:
        print("\nOpción no válida. Inténtalo de nuevo.")