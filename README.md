Descripción

En esta actividad se desarrollaron dos programas en Python para comprender cómo funcionan los algoritmos de búsqueda. El primero utiliza los algoritmos BFS y DFS para encontrar rutas dentro de un grafo, mientras que el segundo utiliza BFS para encontrar un camino dentro de un laberinto, evitando las paredes.

Objetivo

Comprender y aplicar los algoritmos de búsqueda BFS (Breadth-First Search) y DFS (Depth-First Search), identificando sus diferencias y su funcionamiento mediante ejemplos prácticos en Python.

Contenido del proyecto

Problema 1: Búsqueda en un grafo

Archivo: problema1_grafo_bfs_dfs.py

Este programa representa un grafo mediante una lista de adyacencia. Implementa dos algoritmos:

* BFS: busca por niveles y permite encontrar una ruta con el menor número de aristas en un grafo no ponderado.
* DFS: explora una ruta lo más profundo posible antes de retroceder y continuar con otras opciones.

Ambos algoritmos buscan una ruta desde el nodo A hasta el nodo G.

Problema 2: Búsqueda en un laberinto

Archivo: problema2_laberinto_bfs.py

Este programa representa un laberinto mediante una matriz. Utiliza BFS para encontrar un camino desde la posición inicial hasta la meta, evitando las casillas que representan paredes.

El programa muestra la ruta encontrada y la cantidad de movimientos necesarios para llegar al destino.

Requisitos

* Python 3.
* Un editor de código, como Visual Studio Code, o una terminal para ejecutar los programas.

No es necesario instalar librerías externas, ya que se utiliza collections, que forma parte de Python.

Cómo ejecutar los programas

1. Descarga o clona este repositorio.
2. Abre una terminal en la carpeta donde guardaste los archivos.
3. Ejecuta el primer programa con el siguiente comando:

python problema1_grafo_bfs_dfs.py

4. Ejecuta el segundo programa con:

python problema2_laberinto_bfs.py

Si el comando python no funciona, puedes intentar con python3.

Resultados esperados

* En el primer programa se muestran las rutas encontradas mediante BFS y DFS.
* En el segundo programa se muestra la secuencia de posiciones que forman la ruta del laberinto y el número de movimientos realizados.

Conclusión

Con esta actividad se pudo comprender que los algoritmos BFS y DFS permiten buscar rutas dentro de diferentes estructuras. BFS explora los nodos por niveles, mientras que DFS profundiza en una ruta antes de regresar. También se observó cómo BFS puede utilizarse para resolver un laberinto y encontrar el camino con menos movimientos cuando todos los movimientos tienen el mismo costo.

Autor

Nombre: Melonie Suarez

Materia: Fundamentos IA

Actividad: 2

Fecha de entrega: 19 de Octubre 2026