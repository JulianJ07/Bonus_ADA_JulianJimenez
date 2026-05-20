# Mini Modelo LLM - Resumen de Texto

Este proyecto implementa un mini modelo de resumen siguiendo la guia del PDF:

1. Lee un texto ingresado por el usuario.
2. Limpia y tokeniza las palabras.
3. Elimina stopwords.
4. Calcula frecuencias.
5. Construye un grafo de co-ocurrencia por oracion.
6. Puntua palabras y oraciones.
7. Muestra un resumen con las oraciones mas importantes.

## Ejecutar

```bash
python mini_modelo_resumen.py
```

Pega el texto que quieres resumir, presiona Enter en una linea vacia y elige
cuantas oraciones debe tener el resumen.

## Ejemplo de texto

```text
Los algoritmos son fundamentales en informatica. Los algoritmos permiten resolver problemas de manera eficiente. La eficiencia es importante en el diseno de algoritmos.
```
