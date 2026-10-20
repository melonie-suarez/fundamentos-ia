from collections import deque

grafo = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B", "G"],
    "E": ["B", "G"],
    "F": ["C", "G"],
    "G": ["D", "E", "F"]
}

def reconstruir_ruta(padres, meta):
    ruta = []
    actual = meta
    while actual is not None:
        ruta.append(actual)
        actual = padres[actual]
    return list(reversed(ruta))

def bfs(grafo, inicio, meta):
    cola = deque([inicio])
    padres = {inicio: None}
    while cola:
        actual = cola.popleft()
        if actual == meta:
            return reconstruir_ruta(padres, meta)
        for vecino in grafo[actual]:
            if vecino not in padres:
                padres[vecino] = actual
                cola.append(vecino)
    return None

def dfs(grafo, inicio, meta):
    pila = [inicio]
    padres = {inicio: None}
    while pila:
        actual = pila.pop()
        if actual == meta:
            return reconstruir_ruta(padres, meta)
        for vecino in reversed(grafo[actual]):
            if vecino not in padres:
                padres[vecino] = actual
                pila.append(vecino)
    return None

print("Ruta encontrada con BFS:", bfs(grafo, "A", "G"))
print("Ruta encontrada con DFS:", dfs(grafo, "A", "G"))