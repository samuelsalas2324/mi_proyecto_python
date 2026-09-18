/* Quiz de Stack y Arquitecturas — lógica de la vista.
   La validación real ocurre en el servidor (POST /api/verificar),
   de modo que las respuestas correctas nunca viajan al navegador. */

(function () {
  "use strict";

  var preguntas = JSON.parse(document.getElementById("datos-quiz").textContent);
  var total = preguntas.length;
  var LETRAS = ["A", "B", "C", "D"];

  var indice = 0;
  var aciertos = 0;
  var seleccion = null;
  var bloqueado = false;

  var el = {
    tema: document.getElementById("tema"),
    enunciado: document.getElementById("enunciado"),
    opciones: document.getElementById("opciones"),
    contador: document.getElementById("contador"),
    barra: document.getElementById("barra"),
    marcador: document.getElementById("marcador"),
    feedback: document.getElementById("feedback"),
    feedbackTitulo: document.getElementById("feedback-titulo"),
    feedbackTexto: document.getElementById("feedback-texto"),
    btnResponder: document.getElementById("btn-responder"),
    btnSiguiente: document.getElementById("btn-siguiente"),
    btnReiniciar: document.getElementById("btn-reiniciar"),
    panelPregunta: document.getElementById("panel-pregunta"),
    panelResultado: document.getElementById("panel-resultado"),
    resultadoAciertos: document.getElementById("resultado-aciertos"),
    resultadoMensaje: document.getElementById("resultado-mensaje")
  };

  function crearOpcion(letra, texto) {
    var etiqueta = document.createElement("label");
    etiqueta.className = "opcion";
    etiqueta.dataset.letra = letra;

    var radio = document.createElement("input");
    radio.type = "radio";
    radio.name = "opcion";
    radio.value = letra;

    var spanLetra = document.createElement("span");
    spanLetra.className = "opcion__letra";
    spanLetra.textContent = letra;

    var spanTexto = document.createElement("span");
    spanTexto.className = "opcion__texto";
    spanTexto.textContent = texto;

    etiqueta.appendChild(radio);
    etiqueta.appendChild(spanLetra);
    etiqueta.appendChild(spanTexto);

    etiqueta.addEventListener("click", function () {
      if (bloqueado) return;
      seleccion = letra;
      marcarSeleccion(letra);
      el.btnResponder.disabled = false;
    });

    return etiqueta;
  }

  function pintarPregunta() {
    var pregunta = preguntas[indice];
    seleccion = null;
    bloqueado = false;

    el.tema.textContent = pregunta.tema;
    el.enunciado.textContent = pregunta.enunciado;
    el.contador.textContent = "Pregunta " + (indice + 1) + " de " + total;
    el.barra.style.width = (indice / total) * 100 + "%";

    el.opciones.innerHTML = "";
    LETRAS.forEach(function (letra) {
      el.opciones.appendChild(crearOpcion(letra, pregunta.opciones[letra]));
    });

    el.feedback.classList.add("oculto");
    el.feedback.classList.remove("feedback--ok", "feedback--error");
    el.btnResponder.classList.remove("oculto");
    el.btnResponder.disabled = true;
    el.btnSiguiente.classList.add("oculto");
    el.btnSiguiente.textContent = indice === total - 1 ? "Ver resultado" : "Siguiente";
  }

  function marcarSeleccion(letra) {
    var opciones = el.opciones.querySelectorAll(".opcion");
    Array.prototype.forEach.call(opciones, function (op) {
      op.classList.toggle("opcion--activa", op.dataset.letra === letra);
    });
  }

  function pintarCorreccion(datos) {
    var opciones = el.opciones.querySelectorAll(".opcion");
    Array.prototype.forEach.call(opciones, function (op) {
      var letra = op.dataset.letra;
      if (letra === datos.opcion_correcta) {
        op.classList.add("opcion--correcta");
      }
      if (letra === seleccion && !datos.correcta) {
        op.classList.add("opcion--incorrecta");
      }
    });
  }

  function responder(evento) {
    evento.preventDefault();
    if (!seleccion || bloqueado) return;
    bloqueado = true;
    el.btnResponder.disabled = true;

    fetch("/api/verificar", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pregunta_id: preguntas[indice].id, opcion: seleccion })
    })
      .then(function (respuesta) {
        if (!respuesta.ok) throw new Error("Respuesta no válida del servidor");
        return respuesta.json();
      })
      .then(function (datos) {
        pintarCorreccion(datos);

        if (datos.correcta) {
          aciertos += 1;
          el.marcador.textContent = aciertos;
          el.feedback.classList.add("feedback--ok");
          el.feedbackTitulo.textContent = "Respuesta correcta";
        } else {
          el.feedback.classList.add("feedback--error");
          el.feedbackTitulo.textContent =
            "Respuesta incorrecta. La opción correcta era " +
            datos.opcion_correcta + ": " + datos.texto_correcto;
        }
        el.feedbackTexto.textContent = datos.retroalimentacion;

        el.feedback.classList.remove("oculto");
        el.btnResponder.classList.add("oculto");
        el.btnSiguiente.classList.remove("oculto");
        el.barra.style.width = ((indice + 1) / total) * 100 + "%";
      })
      .catch(function () {
        el.feedbackTitulo.textContent = "No fue posible verificar la respuesta";
        el.feedbackTexto.textContent =
          "Revisa la conexión con el servidor e inténtalo nuevamente.";
        el.feedback.classList.remove("oculto");
        bloqueado = false;
        el.btnResponder.disabled = false;
      });
  }

  function siguiente(evento) {
    evento.preventDefault();
    if (indice === total - 1) {
      mostrarResultado();
      return;
    }
    indice += 1;
    pintarPregunta();
  }

  function mensajeSegunPuntaje(porcentaje) {
    if (porcentaje === 100) {
      return "Excelente: dominas los conceptos de stack y arquitecturas.";
    }
    if (porcentaje >= 70) {
      return "Buen resultado. Repasa los temas en los que fallaste.";
    }
    if (porcentaje >= 50) {
      return "Vas por buen camino, pero conviene repasar la teoría del curso.";
    }
    return "Es recomendable revisar nuevamente los conceptos vistos en clase.";
  }

  function mostrarResultado() {
    el.panelPregunta.classList.add("oculto");
    el.panelResultado.classList.remove("oculto");
    el.resultadoAciertos.textContent = aciertos;
    el.barra.style.width = "100%";
    el.contador.textContent = "Cuestionario finalizado";
    el.resultadoMensaje.textContent = mensajeSegunPuntaje((aciertos / total) * 100);
  }

  function reiniciar() {
    indice = 0;
    aciertos = 0;
    el.marcador.textContent = "0";
    el.panelResultado.classList.add("oculto");
    el.panelPregunta.classList.remove("oculto");
    pintarPregunta();
  }

  el.btnResponder.addEventListener("click", responder);
  el.btnSiguiente.addEventListener("click", siguiente);
  el.btnReiniciar.addEventListener("click", reiniciar);

  pintarPregunta();
})();
