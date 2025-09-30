Simulador de Tamagotchi con POO

Este proyecto implementa un simulador de Tamagotchi en Python, aplicando conceptos fundamentales de la Programación Orientada a Objetos. La aplicación de consola permite al usuario crear, cuidar e interactuar con una mascota virtual, gestionando sus atributos de salud, felicidad y energía.

Diseño

El diseño del software se estructuró para cumplir con todos los requisitos del ejercicio

    Asociación de Clases:

        Se creó la clase Persona, que contiene una instancia de la clase Tamagotchi como uno de sus atributos (self.tamagotchi).

        Los métodos de Persona (jugar_con_tamagotchi, darle_comida, etc.) no implementan la lógica de la mascota, sino que delegan la llamada a los métodos correspondientes del objeto Tamagotchi asociado. Esto demuestra una correcta relación de "usa un" entre las clases.

    Encapsulamiento:

        La clase Tamagotchi encapsula sus propios datos (salud, felicidad) y los métodos que los modifican (jugar, comer, curar). La lógica de cómo cambian los stats está contenida únicamente dentro de esta clase.

    Modularización:

        El código está organizado en cuatro archivos distintos para separar responsabilidades, mejorando la claridad y el mantenimiento:

            tamagotchi.py: Clase base.

            personajes_tamagotchi.py: Subclases especializadas.

            persona.py: Clase del dueño.

            main.py: Orquestador principal y lógica de interacción con el usuario.

    Herencia:

        Se implementaron las subclases Mametchi y Pochitchi, que heredan de la clase Tamagotchi.

        Estas subclases reutilizan todos los atributos y métodos de la clase padre y, además, extienden la funcionalidad añadiendo métodos propios y únicos (inventar() y conducir()).

Funcionalidad Adicional Implementada

    Gestión de estado: El sistema maneja correctamente si el Tamagotchi está vivo o muerto, permitiendo reiniciar el ciclo de juego.

    Límites de Atributos: Se implementó una lógica para que los stats no superen el valor máximo de 100.

    Menú Interactivo: La lógica en main.py proporciona una interfaz de usuario robusta que guía la interacción y maneja las entradas incorrectas.

Ejecución

Para ejecutar el programa, sitúese en el directorio del proyecto y ejecute el siguiente comando en la terminal:
    
python main.py

  