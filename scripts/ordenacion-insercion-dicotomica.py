"""
Pseudocódigo:

PROCEDIMIENTO OrdenacionInsercionDicotomica(t)
    PARA CADA elemento EN t DESDE i = 1 HASTA longitud(t) - 1 HACER
        clave = elemento
        INICIO = 0
        FIN = i - 1
        
        // Búsqueda binaria para encontrar la posición de inserción
        MIENTRAS INICIO <= FIN
            MITAD = (INICIO + FIN) / 2
            SI t[MITAD] < clave ENTONCES
                INICIO = MITAD + 1
            SINO
                FIN = MITAD - 1
            FIN SI
        FIN MIENTRAS
        
        // Desplazar los elementos para hacer espacio para la inserción
        PARA j = i HASTA INICIO + 1 CON PASO -1 HACER
            t[j] = t[j - 1]
        FIN PARA
        
        // Insertar el elemento en su posición correcta
        t[INICIO] = clave
    FIN PARA
FIN PROCEDIMIENTO
"""

def ordenacion_insercion_dicotomica(t):
    # Recorremos la lista desde el segundo elemento hasta el último
    for i in range(1, len(t)):
        clave = t[i]  # Clave a insertar en su posición correcta
        inicio = 0    # Inicializamos el índice de inicio de la búsqueda
        fin = i - 1   # Inicializamos el índice de fin de la búsqueda en la sublista ordenada
        
        # Búsqueda binaria para encontrar la posición de inserción de la clave
        while inicio <= fin:
            # Calculamos el índice medio de la sublista
            mitad = (inicio + fin) // 2
            # Si la clave es mayor que el elemento en el índice medio, ajustamos los límites
            if t[mitad] < clave:
                inicio = mitad + 1
            # Si la clave es menor o igual que el elemento en el índice medio, ajustamos los límites
            else:
                fin = mitad - 1
        
        # Desplazamos los elementos para hacer espacio para la inserción
        for j in range(i, inicio, -1):
            t[j] = t[j - 1]
        
        # Insertamos la clave en su posición correcta
        t[inicio] = clave

# Ejemplo de uso
t = [5, 2, 7, 1, 9, 3]
ordenacion_insercion_dicotomica(t)
print("Tabla ordenada por inserción dicotómica:", t)