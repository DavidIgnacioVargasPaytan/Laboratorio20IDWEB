#Version NumPy

import numpy as np

def normalizar_numpy(lista: list, modo: str) -> list:
    """Normaliza una lista de números usando NumPy."""
    
    modos_validos = ["minmax", "zscore", "unit"]
    if modo not in modos_validos:
        raise ValueError(f"Modo de normalización '{modo}' no válido. Use: {', '.join(modos_validos)}")
    
    if not lista:
        return []

    vector = np.array(lista, dtype=float)
    
    if modo == "minmax":
        min_val = vector.min()
        max_val = vector.max()
        rango = max_val - min_val
        
        if rango == 0:
            return [0.0] * len(lista)
            
        return ((vector - min_val) / rango).tolist()
            
    elif modo == "zscore":
        media = vector.mean()
        desviacion_estandar = vector.std(ddof=1) 

        if desviacion_estandar == 0:
            return [0.0] * len(lista)
            
        return ((vector - media) / desviacion_estandar).tolist()

    elif modo == "unit":
        norma = np.linalg.norm(vector)
        
        if norma == 0:
            return [0.0] * len(lista)
            
        return (vector / norma).tolist()

valores = [10, 20, 30]

print(f"\nPruebas con NumPy")
print(f"Original: {valores}")
print(f"MinMax (NumPy): {normalizar_numpy(valores, 'minmax')}")
print(f"ZScore (NumPy): {normalizar_numpy(valores, 'zscore')}")
print(f"Unit (NumPy): {normalizar_numpy(valores, 'unit')}")