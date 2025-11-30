import streamlit as st

# ==============================================================================
# CONFIGURACIÓN DE LA PÁGINA
# ==============================================================================
st.set_page_config(
    page_title="Simulador Tamagotchi",
    page_icon="🥚",
    layout="centered"
)

# ==============================================================================
# ZONA DE CLASES (Adaptadas para Web)
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
        # Mantenemos tu lógica de límites
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
        st.write(f"Has jugado con **{self.nombre}**! 🎾")
        self._actualizar_stats()
        if self.esta_vivo:
            st.caption(f"Felicidad: {self.felicidad} | Salud: {self.salud}")

    def comer(self):
        if not self.esta_vivo:
            st.warning(f"{self.nombre} no puede comer, está muerto.")
            return
            
        self.felicidad += 5
        self.salud += 10
        st.write(f"¡**{self.nombre}** ha comido! 🍔")
        self._actualizar_stats()
        if self.esta_vivo:
            st.caption(f"Felicidad: {self.felicidad} | Salud: {self.salud}")

    def curar(self):
        if not self.esta_vivo:
            st.warning(f"{self.nombre} no puede ser curado, está muerto.")
            return

        self.salud += 20
        self.felicidad -= 5
        st.write(f"¡Has curado a **{self.nombre}**! 💊")
        self._actualizar_stats()
        if self.esta_vivo:
            st.caption(f"Salud: {self.salud} | Felicidad: {self.felicidad}")

    def __str__(self):
       estado = "Vivo" if self.esta_vivo else "Muerto"
       # Usamos markdown para que se vea bonito en la web
       return f"**Estado:** {estado} | **Color:** {self.color}\n\n❤️ **Salud:** {self.salud} | 😄 **Felicidad:** {self.felicidad} | ⚡ **Energía:** {self.energia}"


class Mametchi(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)
    
    def inventar(self):
        if not self.esta_vivo:
            st.warning(f"{self.nombre} no puede inventar, está muerto.")
            return
            
        self.felicidad += 15
        self.energia -= 10
        st.success(f"¡**{self.nombre}** ha inventado algo nuevo! 💡")
        self._actualizar_stats()
        if self.esta_vivo:
            st.caption(f"Felicidad: {self.felicidad} | Energía: {self.energia}")


class Pochitchi(Tamagotchi):
    def __init__(self, nombre, color):
        super().__init__(nombre, color)

    def conducir(self):
        if not self.esta_vivo:
            st.warning(f"{self.nombre} no puede conducir, está muerto.")
            return

        self.felicidad += 10
        self.energia -= 5
        st.success(f"¡**{self.nombre}** ha salido a conducir! 🏎️")
        self._actualizar_stats()
        if self.esta_vivo:
            st.caption(f"Felicidad: {self.felicidad} | Energía: {self.energia}")


class Persona:
    def __init__(self, nombre, apellido, tamagotchi):
        self.nombre = nombre
        self.apellido = apellido
        self.tamagotchi = tamagotchi

    def jugar_con_tamagotchi(self):
        st.write(f"**{self.nombre}** decide jugar con **{self.tamagotchi.nombre}**.")
        self.tamagotchi.jugar()
    
    def darle_comida(self):
        st.write(f"**{self.nombre}** le da de comer a **{self.tamagotchi.nombre}**.")
        self.tamagotchi.comer()
    
    def curarlo(self):
        st.write(f"**{self.nombre}** cuida y cura a **{self.tamagotchi.nombre}**.")
        self.tamagotchi.curar()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

# ==============================================================================
# LÓGICA PRINCIPAL DEL JUEGO (Interfaz Web)
# ==============================================================================

st.title("🥚 Simulador de Tamagotchi")
st.markdown("Proyecto de Programación Orientada a Objetos (POO)")

# Inicializar la sesión (Memoria de la web)
if 'dueño' not in st.session_state:
    st.session_state.dueño = None

# ------------------------------------------------------------------
# PANTALLA 1: CREACIÓN DE PERSONAJE (Tu función crear_nuevo_ciclo)
# ------------------------------------------------------------------
if st.session_state.dueño is None:
    st.subheader("🆕 Nueva Partida")
    
    col1, col2 = st.columns(2)
    nombre_persona = col1.text_input("¿Cuál es tu nombre?")
    apellido_persona = col2.text_input("¿Y tu apellido?")

    st.markdown("---")
    st.write("**Diseña tu Mascota:**")
    
    tipo_input = st.radio(
        "Elige tu tipo de Tamagotchi:",
        ("1. Tamagotchi Normal", "2. Mametchi (Inventor)", "3. Pochitchi (Conductor)")
    )
    
    c_t1, c_t2 = st.columns(2)
    nombre_tamagotchi = c_t1.text_input("Nombre del Tamagotchi:")
    color_tamagotchi = c_t2.text_input("Color del Tamagotchi:")

    if st.button("Adoptar Tamagotchi"):
        if nombre_persona and nombre_tamagotchi:
            # Lógica de instanciación original
            mi_tamagotchi = None
            if "1" in tipo_input:
                mi_tamagotchi = Tamagotchi(nombre_tamagotchi, color_tamagotchi)
            elif "2" in tipo_input:
                mi_tamagotchi = Mametchi(nombre_tamagotchi, color_tamagotchi)
            elif "3" in tipo_input:
                mi_tamagotchi = Pochitchi(nombre_tamagotchi, color_tamagotchi)
            
            # Crear dueño
            st.session_state.dueño = Persona(nombre_persona, apellido_persona, mi_tamagotchi)
            st.success(f"¡Felicidades! {nombre_persona} ha adoptado a {mi_tamagotchi.nombre}.")
            st.rerun() # Recargar página para ir al juego
        else:
            st.error("Por favor completa todos los nombres.")

# ------------------------------------------------------------------
# PANTALLA 2: JUEGO E INTERACCIÓN (Tu bucle while True y menú)
# ------------------------------------------------------------------
else:
    dueño = st.session_state.dueño
    t = dueño.tamagotchi

    # Cabecera con datos del dueño
    st.sidebar.header(f"👤 Dueño: {dueño}")
    if st.sidebar.button("Salir / Reiniciar"):
        st.session_state.dueño = None
        st.rerun()

    # Panel principal
    st.info(f"📊 **Estado de {t.nombre}**")
    st.markdown(str(t)) # Usa tu método __str__ modificado con markdown

    st.divider()

    if t.esta_vivo:
        st.subheader("¿Qué quieres hacer?")
        
        # Botones de acción (replican tu menú 1-6)
        col_acc1, col_acc2, col_acc3, col_acc4 = st.columns(4)
        
        with col_acc1:
            if st.button("🎮 Jugar"):
                dueño.jugar_con_tamagotchi()
        
        with col_acc2:
            if st.button("🍔 Comer"):
                dueño.darle_comida()
        
        with col_acc3:
            if st.button("💊 Curar"):
                dueño.curarlo()
        
        with col_acc4:
            if st.button("✨ Habilidad"):
                if isinstance(t, Mametchi):
                    t.inventar()
                elif isinstance(t, Pochitchi):
                    t.conducir()
                else:
                    st.warning(f"{t.nombre} no tiene una habilidad especial.")

    else:
        st.error(f"☠️ **{t.nombre} ha muerto.**")
        st.write("No puedes interactuar con él.")
        if st.button("Crear uno nuevo"):
            st.session_state.dueño = None
            st.rerun()
