import heapq
import time

class Grafo:
    def __init__(self):
        self.grafo = {}

    def agregar_vertice(self, vertice):
        if vertice not in self.grafo:
            self.grafo[vertice] = {}

    def agregar_arista(self, desde_vertice, hacia_vertice, peso):
        if desde_vertice in self.grafo and hacia_vertice in self.grafo:
            self.grafo[desde_vertice][hacia_vertice] = peso

    def dijkstra(self, inicio):
        distancias = {nodo: float('inf') for nodo in self.grafo}
        distancias[inicio] = 0
        cola_prioridad = [(0, inicio)]

        while cola_prioridad:
            distancia_actual, nodo_actual = heapq.heappop(cola_prioridad)

            if distancia_actual > distancias[nodo_actual]:
                continue

            for vecino, peso in self.grafo[nodo_actual].items():
                distancia = distancia_actual + peso

                if distancia < distancias[vecino]:
                    distancias[vecino] = distancia
                    heapq.heappush(cola_prioridad, (distancia, vecino))

        return distancias

def imprimir_caminos_minimos_con_tiempo(grafo, vertice_inicio):
    start_time = time.time()
    caminos_minimos = grafo.dijkstra(vertice_inicio)
    end_time = time.time()

    print(f"Caminos mínimos desde {vertice_inicio}:")
    for vertice, distancia in caminos_minimos.items():
        print(f"{vertice}: {distancia}")

    execution_time = end_time - start_time
    print(f"Tiempo de ejecución: {execution_time} segundos")

# Crear el grafo de ejemplo y realizar pruebas con medición de tiempo
grafo = Grafo()
grafo.agregar_vertice("A")
grafo.agregar_vertice("B")
grafo.agregar_vertice("C")
grafo.agregar_arista("A", "B", 3)
grafo.agregar_arista("A", "C", 5)
grafo.agregar_arista("B", "C", 2)

# Vértice de inicio para encontrar los caminos mínimos con medición de tiempo
vertice_inicio = "A"
imprimir_caminos_minimos_con_tiempo(grafo, vertice_inicio)