# 🌿 Proyecto Flask - Naturaleza & Experiencia Web

# Quiz de Stack y Arquitecturas de Software

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-3.1.3-000000?style=for-the-badge&logo=flask&logoColor=white)
![Gunicorn](https://img.shields.io/badge/Gunicorn-26.2-499848?style=for-the-badge&logo=gunicorn&logoColor=white)
![Render](https://img.shields.io/badge/Render-Live-46E3B7?style=for-the-badge&logo=render&logoColor=white)
![Licencia](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

Aplicación web desarrollada con **Python y Flask** que incorpora un cuestionario
interactivo sobre Stack y Arquitecturas de Software, como parte de la evaluación
práctica de **Ingeniería de Software II**.

**Estudiante:** Samuel Salas Echeverry
**Asignatura:** Ingeniería de Software II
**Corporación Universitaria Lasallista**

---

## Evidencias

### Evidencia 1 — Pull Request hacia el repositorio original

Solicitud de integración desde el fork personal hacia el repositorio del docente.

> https://github.com/g3in-unilasallista/mi_proyecto_python/pulls

### Evidencia 2 — Aplicación desplegada en Render

Enlace público de la aplicación funcionando en la nube.

> https://mi-proyecto-python-x5cy.onrender.com

### Evidencia 3 — Pull Request específico

Pull Request con la modificación del HTML y la implementación del quiz.

> https://github.com/g3in-unilasallista/mi_proyecto_python/pull/18

### Evidencia 4 — Despliegue exitoso en Render

Registro de construcción y publicación del servicio: instalación de dependencias,
arranque de Gunicorn y confirmación `Your service is live`.

![Despliegue exitoso en Render](docs/evidencias/01-despliegue-render.png)

| Dato del despliegue | Valor |
|---|---|
| Estado | Deploy succeeded · Live |
| Duración | 37,1 s |
| Fecha | 18 de septiembre de 2026, 5:20 p. m. GMT-5 |
| Commit desplegado | `3a8ef18` |
| Servidor | Gunicorn 26.2.0, escuchando en `0.0.0.0:10000` |
| URL primaria | https://mi-proyecto-python-x5cy.onrender.com |

### Evidencia 5 — Código del controlador (`app.py`)

Controlador de la aplicación: define la instancia de Flask, la ruta raíz y el
renderizado de la plantilla.

![Código fuente de app.py](docs/evidencias/02-codigo-app-py.png)

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
```

---

## Stack tecnológico

| Elemento | Tecnología |
|---|---|
| Lenguaje de programación | Python 3.13 |
| Framework backend | Flask 3.1.3 |
| Servidor de producción | Gunicorn 26.2.0 |
| Tecnologías frontend | HTML5, CSS3 (variables, Flexbox, Grid) y JavaScript |
| Base de datos o almacenamiento | Sin base de datos; banco de preguntas en memoria |
| Arquitectura o patrón | Monolito modular con patrón MVC (MTV en Flask) |
| Control de versiones | Git y GitHub |
| Servicio de despliegue | Render (Web Service) |

---

## Arquitectura

El proyecto es un **monolito modular** organizado según el patrón **MVC**, que en
el ecosistema Flask se conoce como **MTV** (Model–Template–View):

| Capa | Responsabilidad | Ubicación |
|---|---|---|
| **Modelo** | Banco de preguntas: enunciado, opciones, respuesta correcta y retroalimentación | Arreglo `PREGUNTAS` en `templates/index.html` |
| **Vista** | Interfaz de portada y cuestionario | `templates/index.html` |
| **Controlador** | Enrutamiento HTTP y validación de respuestas | `app.py` y la lógica JavaScript del quiz |

Se eligió esta arquitectura por el alcance del problema: una sola unidad
desplegable, un dominio acotado y ningún adaptador externo que aislar. Los
microservicios habrían impuesto comunicación en red y despliegues coordinados sin
beneficio funcional, y la arquitectura hexagonal aporta su valor cuando existen
múltiples integraciones externas, que aquí no las hay.

### Estructura del proyecto

```
mi_proyecto_python/
├── app.py                  # Controlador: instancia Flask y ruta '/'
├── templates/
│   └── index.html          # Vista + Modelo: interfaz y banco de preguntas
├── docs/
│   └── evidencias/         # Capturas de la evaluación
├── requirements.txt        # Dependencias: Flask y Gunicorn
├── Procfile                # Comando de arranque: gunicorn app:app
├── .gitignore
├── LICENSE
└── README.md
```

---

## Funcionalidad del Quiz

El cuestionario cumple los requisitos de la evaluación práctica:

- **8 preguntas** sobre arquitectura hexagonal, Clean Architecture, arquitecturas
  orientadas a eventos, monolito modular, stack tecnológico, Git/GitHub y despliegue.
- **Cuatro opciones** de respuesta (A, B, C, D) en cada pregunta.
- **Identificación de la opción seleccionada**, resaltada antes de confirmar.
- **Indicación de correcta o incorrecta**: verde para el acierto, rojo para el
  error, señalando siempre cuál era la respuesta correcta.
- **Retroalimentación explicada** que justifica el concepto evaluado.
- **Marcador acumulado** y pantalla de resultado final con opción de reintentar.
- **Presentación visual coherente** con el resto de la aplicación.

### Pregunta de ejemplo

> **¿Qué representan los puertos en la arquitectura hexagonal?**
>
> - A) Bases de datos utilizadas por la aplicación
> - B) Interfaces mediante las cuales el núcleo se comunica con el exterior ✅
> - C) Servidores encargados del despliegue
> - D) Componentes exclusivos del frontend
>
> *Retroalimentación:* Los puertos son interfaces: definen el contrato mediante el
> cual el núcleo de la aplicación se comunica con el exterior, sin depender de una
> tecnología concreta.

---

## Ejecución local

### 1. Clonar el repositorio

```bash
git clone https://github.com/samuelsalas2324/mi_proyecto_python.git
cd mi_proyecto_python
```

### 2. Crear y activar el entorno virtual

```bash
python -m venv .venv
```

```bash
.\.venv\Scripts\Activate.ps1
```

En Mac o Linux: `source .venv/bin/activate`

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Ejecutar la aplicación

```bash
python app.py
```

La aplicación queda disponible en **http://127.0.0.1:5000**

---

## Despliegue en Render

| Parámetro | Valor |
|---|---|
| Tipo de servicio | Web Service |
| Runtime | Python 3 |
| Build Command | `pip install -r requirements.txt` |
| Start Command | `gunicorn app:app` |

El archivo `Procfile` declara el comando de arranque en producción:

```
web: gunicorn app:app
```

Gunicorn reemplaza al servidor integrado de Flask, que es de un solo hilo y está
pensado únicamente para desarrollo.

---

## Pipeline del trabajo

```
Fork ──▶ Clone ──▶ Ejecución local (.venv) ──▶ Rama ──▶ Modificación HTML
                                                              │
                                                              ▼
Render ◀── Pull Request ◀── Push ◀── Commit ◀────────────── Quiz
```

| # | Etapa | Descripción |
|---|---|---|
| 1 | Fork | Copia del repositorio `g3in-unilasallista` a la cuenta `samuelsalas2324` |
| 2 | Clone | `git clone` del fork al equipo local |
| 3 | Ejecución local | Entorno virtual `.venv`, dependencias y `python app.py` |
| 4 | Rama | Desarrollo aislado de la rama principal |
| 5 | Modificación HTML | Rediseño de `templates/index.html` con identidad visual propia |
| 6 | Quiz | Cuestionario interactivo de 8 preguntas |
| 7 | Commit | Confirmación de los cambios |
| 8 | Push | Envío de los cambios al fork en GitHub |
| 9 | Pull Request | Solicitud de integración al repositorio original |
| 10 | Render | Despliegue y publicación del enlace público |

---

## Licencia

Distribuido bajo la licencia MIT. Consulte el archivo [LICENSE](LICENSE).

---

**Samuel Salas Echeverry** · Ingeniería de Software II
