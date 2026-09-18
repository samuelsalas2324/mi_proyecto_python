"""Aplicación Flask - Quiz de Stack y Arquitecturas de Software.

Versión 1: organización MVC clásica dentro de un monolito modular.
    models/      -> datos del quiz
    controllers/ -> coordinación y validación
    templates/   -> vistas (HTML)
    static/      -> CSS y JavaScript
"""

import os

from flask import Flask, jsonify, render_template, request

from controllers.quiz_controller import QuizController

# Cambia este valor por tu nombre completo.
ESTUDIANTE = "NOMBRE DEL ESTUDIANTE"
ASIGNATURA = "Ingeniería de Software II"

app = Flask(__name__)
controlador = QuizController()


@app.route("/")
def index():
    """Vista de presentación con el nombre del estudiante."""
    return render_template(
        "index.html",
        estudiante=ESTUDIANTE,
        asignatura=ASIGNATURA,
        total=controlador.total(),
    )


@app.route("/quiz")
def quiz():
    """Vista del cuestionario interactivo."""
    return render_template(
        "quiz.html",
        estudiante=ESTUDIANTE,
        asignatura=ASIGNATURA,
        preguntas=controlador.preguntas_publicas(),
        total=controlador.total(),
    )


@app.post("/api/verificar")
def verificar():
    """Valida en el servidor la opción seleccionada y devuelve el feedback."""
    datos = request.get_json(silent=True) or {}
    pregunta_id = datos.get("pregunta_id")
    opcion = datos.get("opcion")

    if not isinstance(pregunta_id, int) or opcion not in ("A", "B", "C", "D"):
        return jsonify({"error": "Solicitud inválida"}), 400

    resultado = controlador.verificar(pregunta_id, opcion)
    if resultado is None:
        return jsonify({"error": "Pregunta no encontrada"}), 404

    return jsonify(resultado)


if __name__ == "__main__":
    puerto = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=puerto, debug=True)
