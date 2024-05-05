"""
Pseudocódigo:

PROCEDIMIENTO OrdenacionTopologica(n, restricciones)
    // Inicializar las estructuras de datos necesarias
    grados_entrada = lista de 0s de longitud n
    adyacencia = lista de listas vacías de longitud n
    
    // Construir el grafo dirigido y calcular los grados de entrada de cada nodo
    PARA CADA restriccion (i, j) EN restricciones HACER
        adyacencia[i].agregar(j)
        grados_entrada[j] += 1
    FIN PARA
    
    // Inicializar una lista para almacenar el orden topológico de las tareas
    ordenacion = lista vacía
    
    // Procesar los nodos en orden topológico
    PARA i DESDE 0 HASTA n - 1 HACER
        nodo = encontrar_nodo_sin_entrada(grados_entrada)
        SI nodo == -1 ENTONCES
            DEVOLVER "No se puede cumplir con todas las restricciones. No hay una ordenación de las tareas."
        FIN SI
        ordenacion.agregar(nodo)
        PARA CADA adyacente EN adyacencia[nodo] HACER
            grados_entrada[adyacente] -= 1
        FIN PARA
    FIN PARA
    
    DEVOLVER ordenacion
FIN PROCEDIMIENTO

FUNCION encontrar_nodo_sin_entrada(grados_entrada)
    PARA i DESDE 0 HASTA longitud(grados_entrada) - 1 HACER
        SI grados_entrada[i] == 0 ENTONCES
            grados_entrada[i] = -1  // Marcar el nodo como visitado
            DEVOLVER i
        FIN SI
    FIN PARA
    DEVOLVER -1  // No se encontró ningún nodo sin entrada
FIN FUNCION
"""

def ordenacion_topologica(n, restricciones):
    grados_entrada = [0] * n
    adyacencia = [[] for _ in range(n)]
    
    # Construir el grafo dirigido y calcular los grados de entrada de cada nodo
    for i, j in restricciones:
        adyacencia[i].append(j)
        grados_entrada[j] += 1
    
    ordenacion = []
    
    for _ in range(n):
        nodo = encontrar_nodo_sin_entrada(grados_entrada)
        if nodo == -1:
            return "No se puede cumplir con todas las restricciones. No hay una ordenación de las tareas."
        ordenacion.append(nodo)
        for adyacente in adyacencia[nodo]:
            grados_entrada[adyacente] -= 1
    
    return ordenacion

def encontrar_nodo_sin_entrada(grados_entrada):
    for i in range(len(grados_entrada)):
        if grados_entrada[i] == 0:
            grados_entrada[i] = -1  # Marcar el nodo como visitado para evitar duplicados
            return i
    return -1

# Ejemplo 1: Ordenación válida
n = 5
restricciones = [(0, 1), (1, 2), (1, 3), (2, 4), (3, 4)]
resultado = ordenacion_topologica(n, restricciones)
print("Ejemplo 1: Orden topológico de las tareas:", resultado)

# Ejemplo 2: No se pueden cumplir todas las restricciones
n = 5
restricciones = [(0, 1), (1, 2), (2, 0)]
resultado = ordenacion_topologica(n, restricciones)
print("Ejemplo 2:", resultado)

# Ejemplo 3: Ordenación válida con tareas adicionales
n = 7
restricciones = [(0, 1), (0, 2), (1, 3), (2, 3), (3, 4), (5, 6)]
resultado = ordenacion_topologica(n, restricciones)
print("Ejemplo 3: Orden topológico de las tareas:", resultado)

# Ejemplo 4: Tareas independientes (sin restricciones)
n = 4
restricciones = []
resultado = ordenacion_topologica(n, restricciones)
print("Ejemplo 4: Orden topológico de las tareas:", resultado)