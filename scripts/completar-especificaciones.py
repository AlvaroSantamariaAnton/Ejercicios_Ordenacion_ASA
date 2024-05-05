"""
Pseudocódigo:

Función max_segmentos(t):
    segmentos = []  // Lista para almacenar los segmentos encontrados
    n = longitud(t)  // Longitud de la lista t
    i = 0            // Índice para recorrer la lista
    
    // Iterar sobre la lista hasta que alcancemos el final
    Mientras i sea menor que n hacer:
        max_valor = t[i]  // Valor máximo inicial del segmento
        fin = i           // Índice del final del segmento
        
        // Encontrar el final del segmento y el máximo valor en el segmento
        Para j desde i + 1 hasta n - 1 hacer:
            Si t[j] es mayor o igual que max_valor entonces:
                max_valor = t[j]
                fin = j
            Sino:
                Romper el ciclo
        
        // Guardar el segmento encontrado en la lista de segmentos
        Añadir (i, fin) a segmentos
        
        // Realizar la operación de explorar
        max_segmento = t[i]
        Para k desde i + 1 hasta fin hacer:
            max_segmento = máximo(max_segmento, t[k])
            t[k - 1] = t[k]
        t[fin] = max_segmento
        
        // Mover al siguiente elemento
        i = i + 1
    
    Devolver segmentos
"""

def max_segmentos(t):
    segmentos = []  # Lista para almacenar los segmentos encontrados
    n = len(t)      # Longitud de la lista t
    i = 0           # Índice para recorrer la lista
    
    # Iterar sobre la lista hasta que alcancemos el final
    while i < n:
        max_valor = t[i]  # Valor máximo inicial del segmento
        fin = i           # Índice del final del segmento
        
        # Encontrar el final del segmento y el máximo valor en el segmento
        for j in range(i + 1, n):
            if t[j] >= max_valor:
                max_valor = t[j]
                fin = j
            else:
                break
        
        # Guardar el segmento encontrado en la lista de segmentos
        segmentos.append((i, fin))
        
        # Realizar la operación de explorar
        max_segmento = t[i]
        for k in range(i + 1, fin + 1):
            max_segmento = max(max_segmento, t[k])
            t[k - 1] = t[k]
        t[fin] = max_segmento
        
        # Mover al siguiente elemento
        i += 1
    
    return segmentos

# Ejemplo de uso
tabla = [7, 14, 2, 10, 18, 9, 5, 4, 3, 8, 21, 1]
segmentos = max_segmentos(tabla)
print("Segmentos encontrados:")
for inicio, fin in segmentos:
    print(f"Segmento desde {inicio} hasta {fin} con máximo en t[{inicio}] = {tabla[inicio]}")