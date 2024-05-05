# Ejercicios de Ordenación

## Algoritmo de Ordenación por Inserción Dicotómica

Este es un algoritmo de ordenación que utiliza una estrategia de inserción dicotómica para ordenar una lista de elementos.

### Descripción

El algoritmo `ordenacion_insercion_dicotomica` funciona de la siguiente manera:

1. Recorre la lista desde el segundo elemento hasta el último.
2. En cada iteración, toma el elemento actual como clave a insertar en su posición correcta.
3. Realiza una búsqueda binaria en la sublista ordenada para encontrar la posición de inserción de la clave.
4. Desplaza los elementos necesarios para hacer espacio para la inserción.
5. Inserta la clave en su posición correcta.

### Ejemplo de Uso

```python
# Ejemplo de uso
t = [5, 2, 7, 1, 9, 3]
ordenacion_insercion_dicotomica(t)
print("Tabla ordenada por inserción dicotómica:", t)
```

## Algoritmo de Ordenación Topológica

Este algoritmo realiza una ordenación topológica de un grafo dirigido dado un número de nodos y un conjunto de restricciones entre ellos.

### Descripción

El algoritmo `ordenacion_topologica` funciona de la siguiente manera:

1. Construye un grafo dirigido basado en las restricciones proporcionadas y calcula los grados de entrada de cada nodo.
2. Encuentra un nodo sin restricciones de entrada en cada iteración.
3. Añade el nodo a la ordenación resultante y decrementa los grados de entrada de sus nodos adyacentes.
4. Repite este proceso hasta que todos los nodos hayan sido añadidos a la ordenación o no se pueda cumplir con todas las restricciones.

### Ejemplo de Uso

```python
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
```

## Link al repositorio de GitHub

https://github.com/AlvaroSantamariaAnton/Ejercicios_Ordenacion_ASA.git