from flask import Flask, render_template, request

from mini_modelo_resumen import resumir


app = Flask(__name__)

EJEMPLO = """
El mandatario distrital dijo que a la fecha no han recibido ninguna notificación oficial, y que más allá del pronunciamiento que emitió la ministra de Transporte, en la ciudad ningún proceso de fotodetección puede ser irregular, y más ahora que es algo que corresponde netamente a la administración municipal tras finalizar el contrato en diciembre del año pasado con la concesión que estaba a cargo de dicha labor.

“Señalizamos todas las cámaras para que dejaran de ser cámaras trampa, y hoy tenemos reducción en las fotomultas con respecto al mismo mes del año anterior. Yo no quiero la plata de la gente, yo quiero que cuiden su vida”, dijo Gutiérrez.

Además, precisó que, como medida preventiva en la ciudad, un mes antes del vencimiento del SOAT o la revisión tecnicomecánica de los vehículos, se les empieza a notificar a los conductores vía correo electrónico o mensaje de texto que deben estar al tanto de su renovación para evitar multas. He ahí la importancia de tener la información actualizada en el Registro Único Nacional de Tránsito RUNT.

Respecto a la investigación por parte del Gobierno Nacional, el mandatario dice que deberán revisar una vez les llegue la notificación, y a la par, determinar acciones caso tal que sí se estén presentando dichas irregularidades en los sistemas de fotodetección de la capital antioqueña.

Otro de los puntos detallados por la SuperTransporte es que las autoridades investigadas que ya hayan hecho cobros por multas de origen irregular, “podrían verse obligadas a devolver estos recursos y además enfrentar sanciones equivalentes al doble de lo recaudado, lo que superaría los $2,1 billones, conforme a lo establecido en la Ley 2251 de 2022”.

“Vamos a analizar esto. Y antes de hablar de devoluciones primero tengo que preguntarle al equipo qué fue lo que llegó y hacer la revisión: cuántos casos corresponden a Medellín y cuántos a otras zonas, porque ahí hay un tema global. Pero vuelvo y digo, no se pueden cometer injusticias con esos sistemas”, agregó el alcalde.
""".strip()


def preparar_grafo(grafo, palabras_importantes, limite=8):
    puntajes = dict(palabras_importantes)
    palabras = [palabra for palabra, _ in palabras_importantes[:limite]]

    return [
        {
            "palabra": palabra,
            "conexiones": sorted(
                grafo.get(palabra, []),
                key=lambda p: puntajes.get(p, 0),
                reverse=True,
            )[:6],
        }
        for palabra in palabras
    ]


@app.route("/", methods=["GET", "POST"])
def index():
    texto = ""
    cantidad_oraciones = 2
    resumen = []
    palabras_importantes = []
    grafo_visible = []
    error = ""

    if request.method == "POST":
        texto = request.form.get("texto", "").strip()
        accion = request.form.get("accion", "resumir")

        if accion == "ejemplo":
            texto = EJEMPLO

        try:
            cantidad_oraciones = max(
                1,
                min(8, int(request.form.get("cantidad_oraciones", 2))),
            )
        except ValueError:
            cantidad_oraciones = 2

        if not texto:
            error = "Ingresa un texto para generar el resumen."
        else:
            resumen, palabras_importantes, grafo = resumir(texto, cantidad_oraciones)
            grafo_visible = preparar_grafo(grafo, palabras_importantes)

            if not resumen:
                error = "No se encontraron suficientes palabras importantes para resumir."

    return render_template(
        "index.html",
        texto=texto,
        cantidad_oraciones=cantidad_oraciones,
        resumen=resumen,
        palabras_importantes=palabras_importantes[:8],
        grafo_visible=grafo_visible,
        error=error,
        tiene_resultados=bool(resumen),
    )


if __name__ == "__main__":
    app.run(debug=True)
