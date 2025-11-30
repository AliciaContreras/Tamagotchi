import streamlit as st

# ==============================================================================
# ZONA 1: TUS CLASES ORIGINALES (PEGA AQUÍ TU CÓDIGO VIEJO)
# ==============================================================================

# 1. Pega aquí abajo todo el contenido de 'tamagotchi.py'
# (Mantén tus clases class Tamagotchi: ... tal cual las escribiste)
# ---------------------------------------------------------
class Tamagotchi:
    # ... pega aquí tu código de la clase Tamagotchi ...
    def __init__(self, nombre, color):
        self.nombre = nombre
        self.color = color
        self.energia = 100
        self.hambre = 0
        self.felicidad = 100
        self.esta_vivo = True

    def __str__(self):
        return f"Nombre: {self.nombre} | Energía: {self.energia} | Hambre: {self.hambre}"
    # ... etc (tu código original) ...

# 2. Pega aquí abajo todo el contenido de 'subclases_tamagotchi.py'
# ---------------------------------------------------------
class Mametchi(Tamagotchi):
    # ... tu código original ...
    pass

class Pochitchi(Tamagotchi):
    # ... tu código original ...
    pass

# 3. Pega aquí abajo todo el contenido de 'persona.py'
# ---------------------------------------------------------
class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi
    
    def jugar_con_tamagotchi(self):
        # ... tu código original (aunque tenga prints, funcionará la lógica interna)
        self.tamagotchi.energia -= 10
        self.tamagotchi.felicidad += 10
        # ... etc
        
    def darle_comida(self):
        # ... tu código original ...
        pass
        
    def curarlo(self):
        # ... tu código original ...
        pass

# ==============================================================================
# ZONA 2: LA INTERFAZ WEB (ESTO SUSTITUYE A TU 'MAIN.PY')
# ==============================================================================

# Configuración si este fuera el archivo único, si es parte del menú anterior
# ignora el set_page_config.

if 'dueño' not in st.session_state:
    st.session_state.dueño = None

st.title("🥚 Simulador de Tamagotchi")

# --- MENÚ DE CREACIÓN (Equivalente a tu función crear_nuevo_ciclo) ---
if st.session_state.dueño is None:
    st.write("--- Creación de un Nuevo Tamagotchi ---")
    
    col1, col2 = st.columns(2)
    nombre_persona = col1.text_input("¿Cuál es tu nombre?")
    apellido_persona = col2.text_input("¿Y tu apellido?")
    
    tipo = st.selectbox("Elige tu tipo de Tamagotchi:", ["1. Normal", "2. Mametchi", "3. Pochitchi"])
    nombre_tamagotchi = st.text_input("Ingresa el nombre de tu Tamagotchi:")
    color_tamagotchi = st.text_input("Ingresa el color:")

    if st.button("Crear Tamagotchi"):
        if nombre_persona and nombre_tamagotchi:
            mi_tamagotchi = None
            if "1" in tipo:
                mi_tamagotchi = Tamagotchi(nombre_tamagotchi, color_tamagotchi)
            elif "2" in tipo:
                mi_tamagotchi = Mametchi(nombre_tamagotchi, color_tamagotchi)
            elif "3" in tipo:
                mi_tamagotchi = Pochitchi(nombre_tamagotchi, color_tamagotchi)
            
            # Aquí usamos TU clase Persona
            st.session_state.dueño = Persona(nombre_persona, apellido_persona, mi_tamagotchi)
            st.success("¡Creado con éxito!")
            st.rerun()
        else:
            st.warning("Por favor llena todos los datos.")

# --- MENÚ DE JUEGO (Equivalente a tu while True) ---
else:
    dueño = st.session_state.dueño
    t = dueño.tamagotchi
    
    st.subheader(f"Dueño: {dueño.nombre} {dueño.apellido}")
    
    # Mostramos el estado usando TU método __str__ original
    st.info(f"Estado: {t}") 

    if t.esta_vivo:
        st.write("¿Qué deseas hacer?")
        
        c1, c2, c3, c4 = st.columns(4)
        
        # Botones que ejecutan TUS métodos originales
        if c1.button("Jugar"):
            dueño.jugar_con_tamagotchi()
            st.success("Jugaste con el Tamagotchi.")
            
        if c2.button("Comer"):
            dueño.darle_comida()
            st.success("Le diste de comer.")
            
        if c3.button("Curar"):
            dueño.curarlo()
            st.success("Lo has curado.")
            
        if c4.button("Habilidad Especial"):
            # Mantenemos tu lógica de 'isinstance'
            if isinstance(t, Mametchi):
                # Ojo: Si tus métodos solo hacen print(), en la web no se verá el texto,
                # pero los stats SÍ cambiarán.
                if hasattr(t, 'inventar'): t.inventar()
                st.info("Usó su habilidad de inventor.")
            elif isinstance(t, Pochitchi):
                if hasattr(t, 'conducir'): t.conducir()
                st.info("Salió a conducir.")
            else:
                st.warning("Este Tamagotchi no tiene habilidades especiales.")
                
    else:
        st.error("☠️ Tu Tamagotchi ha muerto...")
        if st.button("Reiniciar juego"):
            st.session_state.dueño = None
            st.rerun()

    # Botón de salir (Equivalente a tu opción 7)
    if st.button("Salir / Cambiar Dueño"):
        st.session_state.dueño = None
        st.rerun()
