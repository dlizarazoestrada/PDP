import numpy as np
import itertools

# Función para generar todas las rutas, sus productos y las sumas de restricción
def generar_rutas_y_productos_con_restriccion(matriz, matriz_restriccion, limite, maximo=True):
    n, m = matriz.shape
    resultados = []

    # Generar todas las posibles combinaciones de índices para las rutas
    combinaciones = itertools.product(range(n), repeat=m)

    for combinacion in combinaciones:
        suma_restriccion = 0
        producto = 1
        for etapa, nodo in enumerate(combinacion):
            producto *= matriz[nodo, etapa]
            suma_restriccion += matriz_restriccion[nodo, etapa]
        
        if suma_restriccion <= limite:
            # Incrementar cada posición en la ruta en 1 para ser más comprensible
            ruta_ajustada = [pos + 1 for pos in combinacion]
            resultados.append((ruta_ajustada, producto, suma_restriccion))

    # Filtrar para obtener el máximo o mínimo producto
    if resultados:
        if maximo:
            resultado_final = max(resultados, key=lambda x: x[1])
        else:
            resultado_final = min(resultados, key=lambda x: x[1])
        return resultado_final
    else:
        return None

# Ejemplo de uso
matriz = np.array([[0.5, 0.6, 0.7, 0.5],
          [0.6, 0.7, 0.8, 0.7],
          [0.8, 0.8, 0.9, 0.9]])

matriz_restriccion = np.array([[1, 2, 1, 2], 
                      [2, 4, 3, 3], 
                      [3, 5, 4, 4]])

limite = 10
maximo = True # Cambiar a True para obtener el máximo

resultado = generar_rutas_y_productos_con_restriccion(matriz, matriz_restriccion, limite, maximo)

# Imprimir el resultado
if resultado:
    ruta, probabilidad, costo = resultado
    print(f"Elementos asignados: {ruta} -> Probabilidad: {probabilidad} -> Costo: {costo}")
else:
    print("No se encontraron rutas válidas que cumplan con la restricción.")
