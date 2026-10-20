from collections import deque

laberinto = [
    ["S", ".", ".", "#"],
    ["#", ".", ".", "#"],
    [".", ".", ".", "M"]
]

inicio = (0, 0)
meta = (2, 3)

def bfs_laberinto(tablero, inicio, meta):
    cola = deque([inicio])
    padres = {inicio: None}
    movimientos = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while cola:
        fila, columna = cola.popleft()
        actual = (fila, columna)

        if actual == meta:
            ruta = []
            while actual is not None:
                ruta.append(actual)
                actual = padres[actual]
            return list(reversed(ruta))

        for df, dc in movimientos:
            nf, nc = fila + df, columna + dc
            vecino = (nf, nc)
            dentro = 0 <= nf < len(tablero) and 0 <= nc < len(tablero[0])

            if dentro and tablero[nf][nc] != "#":
                if vecino not in padres:
                    padres[vecino] = (fila, columna)
                    cola.append(vecino)
    return None

ruta = bfs_laberinto(laberinto, inicio, meta)

if ruta:
    print("Ruta encontrada:", ruta)
    print("Cantidad de movimientos:", len(ruta) - 1)
else:
    print("No existe una ruta.")