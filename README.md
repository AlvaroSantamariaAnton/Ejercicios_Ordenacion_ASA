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

## Algoritmo para Completar Especificaciones

Este algoritmo encuentra los segmentos en una lista donde cada segmento contiene un máximo local.

### Descripción

El algoritmo `max_segmentos` funciona de la siguiente manera:

1. Itera sobre la lista proporcionada.
2. Encuentra el final del segmento y el máximo valor en el segmento.
3. Guarda el segmento encontrado en una lista de segmentos.
4. Realiza una operación de exploración para reorganizar la lista original y encontrar el siguiente segmento.
5. Repite este proceso hasta que se hayan encontrado todos los segmentos.

### Ejemplo de Uso

```python
# Ejemplo de uso
tabla = [7, 14, 2, 10, 18, 9, 5, 4, 3, 8, 21, 1]
segmentos = max_segmentos(tabla)
print("Segmentos encontrados:")
for inicio, fin in segmentos:
    print(f"Segmento desde {inicio} hasta {fin} con máximo en t[{inicio}] = {tabla[inicio]}")
```

## Link al repositorio de GitHub

https://github.com/AlvaroSantamariaAnton/Ejercicios_Ordenacion_ASA.git