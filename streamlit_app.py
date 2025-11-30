import streamlit as st

# ==============================================================================
# CONFIGURACIÓN
# ==============================================================================
st.set_page_config(page_title="Simulador Tamagotchi", page_icon="🥚")

# ==============================================================================
# ZONA DE CLASES (Tus clases originales copiadas y adaptadas a st.write)
# ==============================================================================

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
            st.error(f"\n¡Oh no! {self.nombre} se ha quedado sin salud y ha muerto. 😢")

    def jugar(self):
        if not self.esta_vivo:
            st.warning(f"{self.nombre} no puede jugar, está muerto.")
            return

        self.felicidad += 10
        self.salud -= 5
        st.write(f"\n¡Has jugado con {self.nombre}!")
        self._actualizar_stats()
        if self.esta_vivo:
            st.caption(f"Su felicidad es {self.felicidad} y su salud {self.salud}.")

    def comer(self):
        if not self.esta_vivo:
            st.warning(f"{self.nombre} no puede comer, está muerto.")
            return
            
        self.felicidad += 5
        self.salud += 10
        st.write(f"\n¡{self.nombre} ha comido!")
        self._actualizar_stats()
        if self.esta_vivo:
            st.caption(f"Su felicidad es {self.felicidad} y su salud {self.salud}.")

    def curar(self):
        if not self.esta_vivo:
            st.warning(f"{self.nombre} no puede ser curado, está muerto.")
            return

        self.salud += 20
        self.felicidad -= 5
        st.write(f"\n¡Has curado a {self.nombre}!")
        self._actualizar_stats()
        if self.esta_vivo:
            st.caption(f"Su salud es {self.salud} y su felicidad {self.felicidad}.")

    def __str__(self):
       estado = "Vivo" if self.esta_vivo else "Muerto"
       # Usamos markdown simple para que se vea bien en web
       return f"Estado: {estado} | Color: {self.color} | Salud: {self.salud} | Felicidad: {self.felicidad} | Energía: {self.energia}"


class Mametchi(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)
    
    def inventar(self):
        if not self.esta_vivo:
            st.warning(f"{self.nombre} no puede inventar, está muerto.")
            return
            
        self.felicidad += 15
        self.energia -= 10
        st.success(f"\n¡{self.nombre} ha inventado algo nuevo! 💡")
        self._actualizar_stats()
        if self.esta_vivo:
            st.caption(f"Su felicidad es {self.felicidad} y su energía {self.energia}.")


class Pochitchi(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)

    def conducir(self):
        if not self.esta_vivo:
            st.warning(f"{self.nombre} no puede conducir, está muerto.")
            return

        self.felicidad += 10
        self.energia -= 5
        st.success(f"\n¡{self.nombre} ha salido a conducir! 🏎️")
        self._actualizar_stats()
        if self.esta_vivo:
            st.caption(f"Su felicidad es {self.felicidad} y su energía {self.energia}.")


class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        st.write(f"\n{self.nombre} decide jugar con {self.tamagotchi.nombre}.")
        self.tamagotchi.jugar()
    
    def darle_comida(self):
        st.write(f"\n{self.nombre} le da de comer a {self.tamagotchi.nombre}.")
        self.tamagotchi.comer()
    
    def curarlo(self):
        st.write(f"\n{self.nombre} cuida y cura a {self.tamagotchi.nombre}.")
        self.tamagotchi.curar()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==============================================================================
# LÓGICA DEL JUEGO (REEMPLAZO DE TU MAIN)
# ==============================================================================

st.title("Simulador de Tamagotchi")

# Inicializamos el estado para guardar los objetos entre recargas
if 'dueño' not in st.session_state:
    st.session_state.dueño = None

# --- FASE 1: CREAR (Tu función crear_nuevo_ciclo) ---
if st.session_state.dueño is None:
    st.header("--- Creación de un Nuevo Tamagotchi ---")
    
    col1, col2 = st.columns(2)
    nombre_persona = col1.text_input("¿Cuál es tu nombre?")
    apellido_persona = col2.text_input("¿Y tu apellido?")

    st.write("\nElige tu tipo de Tamagotchi:")
    tipo = st.radio("Opción:", ["1. Tamagotchi Normal", "2. Mametchi (Inventor)", "3. Pochitchi (Conductor)"])
    
    c_t1, c_t2 = st.columns(2)
    nombre_tamagotchi = c_t1.text_input("Ingresa el nombre de tu Tamagotchi:")
    color_tamagotchi = c_t2.text_input(f"Ingresa el color:")

    if st.button("Crear"):
        if nombre_persona and nombre_tamagotchi:
            mi_tamagotchi = None
            
            # Tu lógica original de selección
            if "1" in tipo:
                mi_tamagotchi = Tamagotchi(nombre_tamagotchi, color_tamagotchi)
            elif "2" in tipo:
                mi_tamagotchi = Mametchi(nombre_tamagotchi, color_tamagotchi)
            elif "3" in tipo:
                mi_tamagotchi = Pochitchi(nombre_tamagotchi, color_tamagotchi)
            
            # Instanciamos a la Persona
            dueño = Persona(nombre_persona, apellido_persona, mi_tamagotchi)
            
            # Guardamos en sesión
            st.session_state.dueño = dueño
            st.success(f"\n¡Felicidades! {dueño} ha adoptado a {mi_tamagotchi.nombre}.")
            st.rerun()
        else:
            st.error("Faltan datos por llenar.")

# --- FASE 2: MENU PRINCIPAL (Tu bucle while True) ---
else:
    dueño = st.session_state.dueño
    
    # Barra lateral con datos del dueño
    st.sidebar.markdown("### Datos del Dueño")
    st.sidebar.text(str(dueño))
    if st.sidebar.button("7. Salir (Reiniciar)"):
        st.session_state.dueño = None
        st.rerun()

    # Mostrar estado actual (Opción 6 original)
    st.info(f"--- Estado de {dueño.tamagotchi.nombre} ---")
    st.markdown(str(dueño.tamagotchi)) # Muestra los stats
    
    st.divider()

    if dueño.tamagotchi.esta_vivo:
        st.subheader("MENÚ PRINCIPAL")
        
        # Botones que replican tus opciones 2, 3, 4 y 5
        col_1, col_2, col_3, col_4 = st.columns(4)
        
        with col_1:
            if st.button("2. Jugar"):
                dueño.jugar_con_tamagotchi()

        with col_2:
            if st.button("3. Comer"):
                dueño.darle_comida()

        with col_3:
            if st.button("4. Curar"):
                dueño.curarlo()

        with col_4:
            if st.button("5. Habilidad"):
                # SOLUCIÓN AL BUG: Usamos el nombre de la clase para evitar
                # problemas de recarga de Streamlit, manteniendo tu lógica.
                tipo_clase = type(dueño.tamagotchi).__name__
                
                if tipo_clase == "Mametchi":
                    dueño.tamagotchi.inventar()
                elif tipo_clase == "Pochitchi":
                    dueño.tamagotchi.conducir()
                else:
                    st.warning(f"\n{dueño.tamagotchi.nombre} no tiene una habilidad especial.")
                    
    else:
        st.error(f"\nTu Tamagotchi ha muerto. Puedes crear uno nuevo o salir.")
        if st.button("Crear nuevo"):
            st.session_state.dueño = None
            st.rerun()
