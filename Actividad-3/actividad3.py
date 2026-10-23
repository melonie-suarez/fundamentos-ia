import random
import math
import matplotlib.pyplot as plt

# Funcion que queremos minimizar
def funcion(x):
    return (x - 3) ** 2 + 2

# Algoritmo Hill Climbing
def hill_climbing(x, paso=0.1, max_iter=500):
    historial = [funcion(x)]

    for _ in range(max_iter):
        vecinos = [
            max(-10, min(10, x - paso)),
            max(-10, min(10, x + paso))
        ]

        mejor = min(vecinos, key=funcion)

        if funcion(mejor) >= funcion(x):
            break

        x = mejor
        historial.append(funcion(x))

    return x, funcion(x), historial

# Algoritmo Simulated Annealing
def simulated_annealing(
    x, temperatura=10.0, enfriamiento=0.97,
    temperatura_min=0.001, max_iter=500
):
    mejor_x = x
    historial = [funcion(x)]
    T = temperatura

    for _ in range(max_iter):
        candidato = max(
            -10, min(10, x + random.uniform(-1, 1))
        )

        diferencia = funcion(candidato) - funcion(x)

        # Acepta mejoras y algunos movimientos peores
        if diferencia < 0 or random.random() < math.exp(-diferencia / T):
            x = candidato

        if funcion(x) < funcion(mejor_x):
            mejor_x = x

        historial.append(funcion(mejor_x))
        T *= enfriamiento

        if T < temperatura_min:
            break

    return mejor_x, funcion(mejor_x), historial

# Programa principal
if __name__ == "__main__":
    random.seed(42)

    x1, costo1, historial1 = hill_climbing(-8)
    x2, costo2, historial2 = simulated_annealing(-8)

    print("RESULTADOS DE HILL CLIMBING")
    print(f"x encontrado: {x1:.4f}")
    print(f"Costo: {costo1:.4f}")

    print("\nRESULTADOS DE SIMULATED ANNEALING")
    print(f"x encontrado: {x2:.4f}")
    print(f"Costo: {costo2:.4f}")

    print("\nMinimo teorico: x = 3, f(x) = 2")

    plt.plot(historial1, label="Hill Climbing")
    plt.plot(historial2, label="Simulated Annealing")
    plt.xlabel("Iteraciones")
    plt.ylabel("Mejor costo encontrado")
    plt.title("Comparacion de convergencia")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("convergencia_actividad3.png")
    plt.show()
