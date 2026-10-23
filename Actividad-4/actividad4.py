from collections import deque
import time

# S = inicio, M = meta, # = pared, . = camino
laberinto = [
    ["S", ".", ".", "#", ".", "."],
    ["#", "#", ".", "#", ".", "#"],
    [".", ".", ".", ".", ".", "."],
    [".", "#", "#", "#", "#", "."],
    [".", ".", ".", ".", ".", "M"]
]

inicio = (0, 0)
meta = (4, 5)

# Abajo, derecha, arriba e izquierda
MOVIMIENTOS = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def buscar(metodo):
    if metodo == "BFS":
        pendientes = deque([inicio])
    else:
        pendientes = [inicio]

    padres = {inicio: None}
    expandidos = 0

    while pendientes:
        if metodo == "BFS":
            actual = pendientes.popleft()
        else:
            actual = pendientes.pop()

        expandidos += 1

        if actual == meta:
            ruta = []
            nodo = actual

            while nodo is not None:
                ruta.append(nodo)
                nodo = padres[nodo]

            ruta.reverse()
            return ruta, expandidos

        if metodo == "BFS":
            movimientos = MOVIMIENTOS
        else:
            movimientos = list(reversed(MOVIMIENTOS))

        for df, dc in movimientos:
            nf = actual[0] + df
            nc = actual[1] + dc
            vecino = (nf, nc)

            dentro = (
                0 <= nf < len(laberinto)
                and 0 <= nc < len(laberinto[0])
            )

            if (
                dentro
                and laberinto[nf][nc] != "#"
                and vecino not in padres
            ):
                padres[vecino] = actual
                pendientes.append(vecino)

    return None, expandidos


def mostrar_ruta(ruta):
    dibujo = [fila[:] for fila in laberinto]

    for fila, columna in ruta[1:-1]:
        dibujo[fila][columna] = "*"

    for fila in dibujo:
        print(" ".join(fila))


if __name__ == "__main__":
    for metodo in ("BFS", "DFS"):
        inicio_tiempo = time.perf_counter()

        ruta, expandidos = buscar(metodo)

        tiempo = time.perf_counter() - inicio_tiempo

        print(f"\nRESULTADOS DE {metodo}")

        if ruta:
            print("Ruta encontrada:", ruta)
            print("Movimientos:", len(ruta) - 1)
            print("Nodos expandidos:", expandidos)
            print(f"Tiempo: {tiempo:.6f} segundos")
            print("Laberinto con la ruta marcada:")
            mostrar_ruta(ruta)
        else:
            print("No se encontró una solución.")
