"""Controlador: coordina el acceso a los datos del quiz y la validación."""

from models.quiz_model import PREGUNTAS


class QuizController:
    """Intermediario entre las rutas de Flask y el modelo del quiz."""

    def __init__(self, preguntas=None):
        self._preguntas = preguntas if preguntas is not None else PREGUNTAS

    def total(self):
        return len(self._preguntas)

    def preguntas_publicas(self):
        """Devuelve las preguntas sin la respuesta correcta.

        La respuesta nunca viaja al navegador: la validación ocurre en el servidor.
        """
        return [
            {
                "id": p["id"],
                "tema": p["tema"],
                "enunciado": p["enunciado"],
                "opciones": p["opciones"],
            }
            for p in self._preguntas
        ]

    def buscar(self, pregunta_id):
        for p in self._preguntas:
            if p["id"] == pregunta_id:
                return p
        return None

    def verificar(self, pregunta_id, opcion):
        """Valida una respuesta y construye la retroalimentación."""
        pregunta = self.buscar(pregunta_id)
        if pregunta is None:
            return None

        es_correcta = opcion == pregunta["correcta"]
        return {
            "id": pregunta["id"],
            "correcta": es_correcta,
            "opcion_correcta": pregunta["correcta"],
            "texto_correcto": pregunta["opciones"][pregunta["correcta"]],
            "retroalimentacion": pregunta["retroalimentacion"],
        }
