import re
import unicodedata
from collections import Counter, defaultdict


STOPWORDS = {
    "a", "al", "algo", "algunas", "algunos", "ante", "antes", "aquel",
    "aquella", "aquellas", "aquello", "aquellos", "aqui", "asi", "cada",
    "como", "con", "contra", "cual", "cuando", "de", "del", "desde",
    "donde", "dos", "e", "el", "ella", "ellas", "ellos", "en", "entre",
    "era", "eran", "eres", "es", "esa", "esas", "ese", "eso", "esos",
    "esta", "estaba", "estaban", "estado", "estan", "estar", "estas",
    "este", "esto", "estos", "fue", "fueron", "ha", "han", "hasta",
    "hay", "la", "las", "le", "les", "lo", "los", "mas", "me", "mi",
    "mis", "mucho", "muy", "ni", "no", "nos", "o", "otra", "otras",
    "otro", "otros", "para", "pero", "por", "porque", "que", "se",
    "ser", "si", "sin", "sobre", "son", "su", "sus", "tambien",
    "te", "tiene", "tienen", "todo", "todos", "tu", "un", "una",
    "unas", "uno", "unos", "y", "ya",
}


def normalizar(texto):
    """Convierte a minusculas, quita tildes y deja solo letras/numeros."""
    texto = texto.lower()
    texto = unicodedata.normalize("NFD", texto)
    texto = "".join(c for c in texto if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9\s]", " ", texto)


def dividir_oraciones(texto):
    oraciones = re.split(r"(?<=[.!?])\s+|\n+", texto.strip())
    return [oracion.strip() for oracion in oraciones if oracion.strip()]


def tokenizar(texto):
    texto_limpio = normalizar(texto)
    return re.findall(r"[a-z0-9]+", texto_limpio)


def quitar_stopwords(palabras):
    return [palabra for palabra in palabras if palabra not in STOPWORDS]


def construir_grafo(oraciones):
    grafo = defaultdict(set)

    for oracion in oraciones:
        palabras = quitar_stopwords(tokenizar(oracion))
        palabras_unicas = list(dict.fromkeys(palabras))

        for palabra in palabras_unicas:
            grafo[palabra]

        for i, palabra in enumerate(palabras_unicas):
            for otra_palabra in palabras_unicas[i + 1:]:
                grafo[palabra].add(otra_palabra)
                grafo[otra_palabra].add(palabra)

    return grafo


def puntuar_palabras(palabras, grafo):
    frecuencias = Counter(palabras)
    return {
        palabra: frecuencia + len(grafo[palabra])
        for palabra, frecuencia in frecuencias.items()
    }


def puntuar_oraciones(oraciones, puntajes_palabras):
    puntajes = []

    for indice, oracion in enumerate(oraciones):
        palabras = quitar_stopwords(tokenizar(oracion))
        puntaje = sum(puntajes_palabras.get(palabra, 0) for palabra in palabras)
        puntajes.append((indice, oracion, puntaje))

    return puntajes


def resumir(texto, cantidad_oraciones=2):
    oraciones = dividir_oraciones(texto)
    palabras = quitar_stopwords(tokenizar(texto))

    if not oraciones or not palabras:
        return [], [], {}

    grafo = construir_grafo(oraciones)
    puntajes_palabras = puntuar_palabras(palabras, grafo)
    puntajes_oraciones = puntuar_oraciones(oraciones, puntajes_palabras)

    mejores_oraciones = sorted(
        puntajes_oraciones,
        key=lambda item: item[2],
        reverse=True,
    )[:cantidad_oraciones]

    resumen = [
        oracion
        for _, oracion, _ in sorted(mejores_oraciones, key=lambda item: item[0])
    ]

    palabras_importantes = sorted(
        puntajes_palabras.items(),
        key=lambda item: item[1],
        reverse=True,
    )

    return resumen, palabras_importantes, grafo


def leer_texto_usuario():
    print("Ingrese el texto que desea resumir.")
    print("Cuando termine, presione Enter en una linea vacia.\n")

    lineas = []
    while True:
        linea = input()
        if not linea.strip():
            break
        lineas.append(linea)

    return "\n".join(lineas)


def pedir_cantidad_oraciones():
    cantidad = input("\nCuantas oraciones debe tener el resumen? [2]: ").strip()

    if not cantidad:
        return 2

    try:
        return max(1, int(cantidad))
    except ValueError:
        print("Valor no valido. Se usaran 2 oraciones.")
        return 2


def main():
    texto = leer_texto_usuario()

    if not texto.strip():
        print("No se ingreso texto.")
        return

    cantidad_oraciones = pedir_cantidad_oraciones()
    resumen, palabras_importantes, grafo = resumir(texto, cantidad_oraciones)

    if not resumen:
        print("No se encontraron suficientes palabras importantes para resumir.")
        return

    print("\nTexto procesado correctamente.")
    print("\nPalabras mas importantes:")
    for palabra, puntaje in palabras_importantes[:5]:
        print(f"- {palabra} (score: {puntaje})")

    print("\nResumen:")
    for indice, oracion in enumerate(resumen, 1):
        print(f"{indice}. {oracion}")

    print("\nGrafo de palabras (lista de adyacencia):")
    for palabra, conexiones in sorted(grafo.items()):
        conexiones_ordenadas = ", ".join(sorted(conexiones)) or "sin conexiones"
        print(f"- {palabra}: {conexiones_ordenadas}")


if __name__ == "__main__":
    main()
