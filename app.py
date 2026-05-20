from flask import Flask, render_template, request

from mini_modelo_resumen import resumir


app = Flask(__name__)

EJEMPLO = (
    "Los algoritmos son fundamentales en informatica. "
    "Los algoritmos permiten resolver problemas de manera eficiente. "
    "La eficiencia es importante en el diseno de algoritmos."
)


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
