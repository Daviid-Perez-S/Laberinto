# Laberinto

Se tiene un tablero cuadriculado de N*N casillas, en el cual se generan un número dado de obstáculos distribuidos de manera aleatoria por el tablero para impedir el paso del agente, un agente necesita encontrar los diferentes caminos para llegar a la solución destino, utilizando un algoritmo de búsqueda en profundidad (DFS) e ignorando si esta es la más corta o larga.

El agente sólo podrá moverse hacia arriba, derecha, abajo o izquierda (en ese orden).

**Reglas**

Las reglas para generar el árbol son las siguientes:

- El árbol representativo se generará con base en el algoritmo de búsqueda no informada llamado “Depth First Search” o “Búsqueda en profundidad”.
- El orden de búsqueda del algoritmo dentro del tablero seguirá el siguiente orden de movimientos:
    - Arriba
    - Derecha
    - Abajo
    - Izquierda
- La generación del árbol y la expansión de sus respectivos nodos se detendrá cuando encuentre una solución objetivo.
- Aquellas casillas del tablero (hojas/nodos en el árbol) que ya se hayan recorrido previamente dentro del algoritmo de búsqueda serán ignoradas para no generar un ciclo infinito de búsqueda y optimizar los recursos de la búsqueda.
- Aquellas casillas del tablero que sean obstáculos no serán comtempladas para representarse dentro del árbol.
- El árbol generado puede o no tener una profundidad del doble de las casillas libres del tablero.


## Creación del entorno virtual

Es necesario virtualenv (python3)

Para instalar virtualenv con python3 se utilia pip3

```
pip3 install virtualenv
```

Para generar el virtualenv llamado, en este caso, "venv"

```
virtualenv venv
```

### MacOS

Activar el virtualenv llamado "venv"

```
source venv/bin/activate
```

### Windows

Activar el virtualenv llamado "venv"

```
.\env\Scripts\activate
```

## Instalación

Una vez activado el entorno virtual se deben de instalar desde cero las dependecias contenidas dentro del archivo de requerimientos.
Para instalar las dependencias del proyecto ejecute el siguiente comando:

```
pip install -r requirements.txt
```

## Ejecutar el programa

```
python generar_arbol.py
```

Ingresamos los parámetros que se nos solicita:

- Tamaño del tablero
- Número de obstáculos

Al final de la ejecución del programa, este generará una imagen llamada "arbol_generado.png" 
en el directorio raíz que contendrá el árbol que representa la solución al problema.

## Desactivar el entorno virtual

```
deactivate venv
```

***

## Créditos

Código creado por:

> - Luis Fernando Hernández M.
> - David Pérez S.
