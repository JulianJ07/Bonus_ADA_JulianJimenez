# Mini Modelo LLM - Resumen de Texto

Este proyecto implementa un mini modelo de resumen siguiendo la guia del PDF:

1. Lee un texto ingresado por el usuario.
2. Limpia y tokeniza las palabras.
3. Elimina stopwords.
4. Calcula frecuencias.
5. Construye un grafo de co-ocurrencia por oracion.
6. Puntua palabras y oraciones.
7. Muestra un resumen con las oraciones mas importantes.

## Explicacion tecnica

El proyecto esta dividido en dos partes principales:

- `mini_modelo_resumen.py`: contiene la logica del modelo de resumen.
- `app.py`: expone esa logica mediante una aplicacion web hecha con Flask.

El sistema no usa un modelo de inteligencia artificial entrenado, sino un
algoritmo extractivo basado en procesamiento de texto y estructuras de datos.
El resumen se genera seleccionando las oraciones originales que tienen mayor
puntaje segun la importancia de sus palabras.

### Flujo del algoritmo

1. **Entrada del texto**

   El usuario ingresa un texto desde la vista web o desde la consola. Ese texto
   se conserva completo para poder mostrar en el resumen las oraciones
   originales.

2. **Division en oraciones**

   La funcion `dividir_oraciones()` separa el texto usando signos como punto,
   interrogacion, exclamacion y saltos de linea. Cada oracion queda guardada en
   una lista para poder evaluarla individualmente.

3. **Normalizacion**

   La funcion `normalizar()` convierte todo el texto a minusculas, elimina
   tildes y reemplaza signos de puntuacion por espacios. Esto permite que
   palabras como `Fotodeteccion`, `fotodeteccion` y `fotodeteccion.` se
   analicen como la misma palabra.

4. **Tokenizacion**

   La funcion `tokenizar()` convierte el texto limpio en una lista de palabras.
   Para esto usa expresiones regulares y conserva solamente caracteres
   alfanumericos.

5. **Eliminacion de stopwords**

   La funcion `quitar_stopwords()` elimina palabras frecuentes que aportan poco
   significado por si solas, como articulos, preposiciones y conectores. Esto
   reduce ruido en el conteo y mejora la seleccion de ideas importantes.

6. **Conteo de frecuencias**

   Se usa `Counter` de Python para contar cuantas veces aparece cada palabra
   relevante. Una palabra con mayor frecuencia tiene mayor probabilidad de
   representar un tema central del texto.

7. **Construccion del grafo de palabras**

   La funcion `construir_grafo()` crea una lista de adyacencia usando
   `defaultdict(set)`. Cada palabra es un nodo del grafo. Dos palabras se
   conectan si aparecen dentro de la misma oracion. Este grafo representa una
   relacion basica de co-ocurrencia entre conceptos.

8. **Puntaje de palabras**

   Cada palabra recibe un puntaje con la formula:

   ```text
   puntaje_palabra = frecuencia + numero_de_conexiones_en_el_grafo
   ```

   Asi, una palabra es mas importante si aparece varias veces y si ademas esta
   relacionada con muchas otras palabras dentro del texto.

9. **Puntaje de oraciones**

   Cada oracion recibe un puntaje sumando los puntajes de sus palabras
   relevantes. Las oraciones con mayor puntaje se consideran mejores candidatas
   para el resumen.

10. **Seleccion del resumen**

    La funcion `resumir()` ordena las oraciones por puntaje de mayor a menor,
    selecciona la cantidad solicitada por el usuario y finalmente las vuelve a
    ordenar segun su posicion original en el texto. Esto hace que el resumen
    mantenga una lectura natural.

### Funcionamiento de la vista web

La aplicacion Flask define una ruta principal `/` en `app.py`.

- Con una solicitud `GET`, se muestra el formulario inicial.
- Con una solicitud `POST`, se recibe el texto del usuario, se llama a
  `resumir()` y se envian los resultados a la plantilla HTML.

La interfaz esta construida con:

- `templates/index.html`: estructura de la pagina y renderizado de resultados.
- `static/styles.css`: estilos visuales, distribucion responsive y diseno de la
  vista.
- `requirements.txt`: dependencia necesaria para instalar Flask.

El resultado mostrado incluye el resumen, las palabras mas importantes con su
puntaje y una representacion parcial del grafo de relaciones.

## Manual de usuario

Las instrucciones completas para acceder, instalar, ejecutar y usar el programa
estan en [MANUAL_USUARIO.md](MANUAL_USUARIO.md).

## Probar con vista web

Instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

Ejecuta la aplicacion:

```bash
python app.py
```

Abre esta direccion en el navegador:

```text
http://127.0.0.1:5000
```

Si en Windows `python` no funciona, prueba con `py`:

```bash
py -m pip install -r requirements.txt
py app.py
```

En la vista puedes pegar un texto, elegir cuantas oraciones quieres en el
resumen y ver las palabras mas importantes junto con el grafo de relaciones.

## Probar en consola

```bash
python mini_modelo_resumen.py
```

Pega el texto que quieres resumir, presiona Enter en una linea vacia y elige
cuantas oraciones debe tener el resumen.

## Ejemplo de texto

```text
Los algoritmos son fundamentales en informatica. Los algoritmos permiten resolver problemas de manera eficiente. La eficiencia es importante en el diseno de algoritmos.
```
