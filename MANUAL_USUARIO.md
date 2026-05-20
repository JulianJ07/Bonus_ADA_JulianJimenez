# Manual de usuario e indicaciones para la ejecucion

## Nombre del programa

Mini Modelo LLM - Resumen de Texto

## Descripcion

El programa permite ingresar un texto y generar un resumen automatico. Para
hacerlo, limpia el texto, elimina palabras vacias, calcula frecuencias,
construye un grafo de relaciones entre palabras y selecciona las oraciones mas
importantes.

## Requisitos

Antes de ejecutar el programa, la persona debe tener instalado:

- Python 3.
- Git, si desea descargar el proyecto desde GitHub.
- Navegador web, por ejemplo Chrome, Edge o Firefox.

## Acceso al proyecto

El proyecto se encuentra disponible en GitHub:

```text
https://github.com/JulianJ07/Bonus_ADA_JulianJimenez
```

Para descargarlo desde la terminal:

```bash
git clone https://github.com/JulianJ07/Bonus_ADA_JulianJimenez.git
cd Bonus_ADA_JulianJimenez
```

Tambien se puede descargar como archivo ZIP desde GitHub y luego descomprimirlo.

## Instalacion

Desde la carpeta del proyecto, instalar las dependencias con:

```bash
python -m pip install -r requirements.txt
```

Si en Windows el comando `python` no funciona, usar:

```bash
py -m pip install -r requirements.txt
```

## Ejecucion con vista web

Para iniciar la aplicacion, ejecutar:

```bash
python app.py
```

En Windows tambien se puede usar:

```bash
py app.py
```

Luego abrir en el navegador la siguiente direccion:

```text
http://127.0.0.1:5000
```

## Uso de la aplicacion

1. Escribir o pegar el texto en el cuadro llamado `Texto original`.
2. Elegir cuantas oraciones debe tener el resumen en el campo `Oraciones`.
3. Presionar el boton `Generar resumen`.
4. Revisar los resultados en la parte derecha de la pantalla:
   - Resumen generado.
   - Palabras importantes con su puntaje.
   - Grafo de relaciones entre palabras.

Tambien se puede presionar `Cargar ejemplo` para cargar automaticamente el texto
de prueba incluido en la aplicacion.

## Ejecucion en consola

El proyecto tambien se puede probar sin vista web:

```bash
python mini_modelo_resumen.py
```

La persona debe pegar el texto, presionar Enter en una linea vacia y luego
indicar cuantas oraciones desea en el resumen.

## Finalizar el programa

Para detener la aplicacion web, volver a la terminal donde se esta ejecutando y
presionar:

```text
Ctrl + C
```
