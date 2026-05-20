# Mini Modelo LLM - Resumen de Texto

Este proyecto implementa un mini modelo de resumen siguiendo la guia del PDF:

1. Lee un texto ingresado por el usuario.
2. Limpia y tokeniza las palabras.
3. Elimina stopwords.
4. Calcula frecuencias.
5. Construye un grafo de co-ocurrencia por oracion.
6. Puntua palabras y oraciones.
7. Muestra un resumen con las oraciones mas importantes.

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
