"""Modelo: datos del quiz de Stack y Arquitecturas de Software.

Esta capa solo conoce los datos. No sabe nada de Flask ni de HTML.
"""

PREGUNTAS = [
    {
        "id": 1,
        "tema": "Arquitectura hexagonal",
        "enunciado": "¿Qué representan los puertos en la arquitectura hexagonal?",
        "opciones": {
            "A": "Bases de datos utilizadas por la aplicación",
            "B": "Interfaces mediante las cuales el núcleo se comunica con el exterior",
            "C": "Servidores encargados del despliegue",
            "D": "Componentes exclusivos del frontend",
        },
        "correcta": "B",
        "retroalimentacion": (
            "Los puertos son interfaces: definen el contrato mediante el cual el "
            "núcleo de la aplicación se comunica con el exterior, sin depender de "
            "una tecnología concreta."
        ),
    },
    {
        "id": 2,
        "tema": "Clean Architecture",
        "enunciado": "¿Cuál es la regla principal de Clean Architecture?",
        "opciones": {
            "A": "Las dependencias apuntan hacia la infraestructura",
            "B": "Las dependencias del código deben apuntar hacia el núcleo",
            "C": "Toda aplicación debe utilizar microservicios",
            "D": "El frontend debe controlar la base de datos",
        },
        "correcta": "B",
        "retroalimentacion": (
            "La regla de dependencia indica que el código fuente siempre apunta "
            "hacia adentro: la infraestructura depende del dominio y nunca al revés."
        ),
    },
    {
        "id": 3,
        "tema": "Arquitectura orientada a eventos",
        "enunciado": "¿Qué caracteriza a una arquitectura orientada a eventos?",
        "opciones": {
            "A": "Productores, consumidores e intermediario o bus de eventos",
            "B": "Únicamente un servidor central",
            "C": "Únicamente bases de datos relacionales",
            "D": "Una estructura obligatoria de tres capas",
        },
        "correcta": "A",
        "retroalimentacion": (
            "En EDA los productores publican eventos, un bus o broker los distribuye "
            "y los consumidores reaccionan, lo que permite desacoplar los componentes."
        ),
    },
    {
        "id": 4,
        "tema": "Stack tecnológico",
        "enunciado": "¿Qué se entiende por Stack tecnológico?",
        "opciones": {
            "A": "La combinación de lenguajes, frameworks, bases de datos, herramientas y servicios",
            "B": "Únicamente el lenguaje utilizado",
            "C": "Únicamente el framework backend",
            "D": "El diseño visual de una aplicación",
        },
        "correcta": "A",
        "retroalimentacion": (
            "El stack es el conjunto completo de tecnologías que sostienen la "
            "aplicación, desde el lenguaje hasta el servicio de despliegue."
        ),
    },
    {
        "id": 5,
        "tema": "Monolito modular",
        "enunciado": "¿Cuál es una característica del monolito modular?",
        "opciones": {
            "A": "Cada módulo debe ejecutarse en un servidor independiente",
            "B": "Organiza internamente las responsabilidades en módulos definidos",
            "C": "No permite utilizar diferentes componentes",
            "D": "Siempre utiliza un bus de eventos",
        },
        "correcta": "B",
        "retroalimentacion": (
            "El monolito modular se despliega como una sola unidad, pero mantiene "
            "fronteras internas claras entre sus módulos."
        ),
    },
    {
        "id": 6,
        "tema": "Arquitectura hexagonal",
        "enunciado": "¿Cuál es el propósito de un adaptador en arquitectura hexagonal?",
        "opciones": {
            "A": "Convertir la comunicación externa para ajustarse al contrato de un puerto",
            "B": "Crear automáticamente bases de datos",
            "C": "Sustituir al núcleo de la aplicación",
            "D": "Administrar usuarios de GitHub",
        },
        "correcta": "A",
        "retroalimentacion": (
            "El adaptador traduce entre el mundo exterior (HTTP, SQL, colas) y el "
            "contrato definido por el puerto, de modo que el núcleo no cambie."
        ),
    },
    {
        "id": 7,
        "tema": "Git y GitHub",
        "enunciado": "¿Cuál es el propósito principal de un Pull Request?",
        "opciones": {
            "A": "Solicitar revisión e integración de cambios en un repositorio",
            "B": "Crear una máquina virtual",
            "C": "Ejecutar Python",
            "D": "Crear una base de datos",
        },
        "correcta": "A",
        "retroalimentacion": (
            "El Pull Request propone integrar los cambios de una rama en otra y "
            "abre el espacio de revisión y discusión del código."
        ),
    },
    {
        "id": 8,
        "tema": "Despliegue",
        "enunciado": "¿Qué evidencia demuestra un despliegue exitoso en Render?",
        "opciones": {
            "A": "Una captura del código fuente",
            "B": "El enlace público funcional y evidencia del proceso de despliegue",
            "C": "Únicamente el repositorio local",
            "D": "Una captura del editor de código",
        },
        "correcta": "B",
        "retroalimentacion": (
            "El despliegue se demuestra con la URL pública funcionando y el log de "
            "build/deploy exitoso en Render."
        ),
    },
]
