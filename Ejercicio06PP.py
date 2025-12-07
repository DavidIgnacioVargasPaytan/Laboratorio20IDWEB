#Version Python Puro

import math 

def normalizar_puro(lista: list, modo: str) -> list:
    """Normaliza una lista de números reales según el modo especificado."""
    
    modos_validos = ["minmax", "zscore", "unit"]
    if modo not in modos_validos:
        raise ValueError(f"Modo de normalización '{modo}' no válido. Use: {', '.join(modos_validos)}")
    
    n = len(lista)
    if n == 0:
        return []

    nueva_lista = [] 
    
    if modo == "minmax":
        min_val = min(lista)
        max_val = max(lista)
        rango = max_val - min_val
        
        if rango == 0:
            return [0.0] * n
        
        for x in lista:
            x_prima = (x - min_val) / rango
            nueva_lista.append(x_prima)
            
    elif modo == "zscore":
        media = sum(lista) / n
        
        suma_diferencias_cuadrado = sum([(x - media) ** 2 for x in lista])
        if n > 1:
            desviacion_estandar = math.sqrt(suma_diferencias_cuadrado / (n - 1))
        else: 
            desviacion_estandar = 0.0

        if desviacion_estandar == 0:
            return [0.0] * n
            
        for x in lista:
            x_prima = (x - media) / desviacion_estandar
            nueva_lista.append(x_prima)

    elif modo == "unit":
        norma_cuadrado = sum([(x ** 2) for x in lista])
        norma = math.sqrt(norma_cuadrado)
        
        if norma == 0:
            return [0.0] * n 
        
        for x in lista:
            x_prima = x / norma
            nueva_lista.append(x_prima)
            
    return nueva_lista

valores = [10, 20, 30]

print(f"\nPruebas con Python Puro")
print(f"Original: {valores}")
print(f"MinMax: {normalizar_puro(valores, 'minmax')}")
print(f"ZScore: {normalizar_puro(valores, 'zscore')}")
print(f"Unit: {normalizar_puro(valores, 'unit')}")