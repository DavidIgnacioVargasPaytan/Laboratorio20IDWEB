def generar_matriz_espiral():
    
    n = 0
    while n < 3:
        try:
            n_input = input("\nIngrese el número N (debe ser mayor o igual a 3): ")
            n = int(n_input)
            if n < 3:
                print("El número debe ser N >= 3. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")

    matriz = [[0] * n for _ in range(n)]

    numero_actual = 1
    limite_superior = 0
    limite_inferior = n - 1
    limite_izquierdo = 0
    limite_derecho = n - 1
    total_celdas = n * n

    while numero_actual <= total_celdas:
        
        for j in range(limite_izquierdo, limite_derecho + 1):
            if numero_actual > total_celdas: break
            matriz[limite_superior][j] = numero_actual
            numero_actual += 1
        limite_superior += 1
        
        for i in range(limite_superior, limite_inferior + 1):
            if numero_actual > total_celdas: break
            matriz[i][limite_derecho] = numero_actual
            numero_actual += 1
        limite_derecho -= 1
        
        if limite_superior <= limite_inferior:
            for j in range(limite_derecho, limite_izquierdo - 1, -1):
                if numero_actual > total_celdas: break
                matriz[limite_inferior][j] = numero_actual
                numero_actual += 1
            limite_inferior -= 1
        
        if limite_izquierdo <= limite_derecho:
            for i in range(limite_inferior, limite_superior - 1, -1):
                if numero_actual > total_celdas: break
                matriz[i][limite_izquierdo] = numero_actual
                numero_actual += 1
            limite_izquierdo += 1

    print(f"\nMatriz Espiral {n}x{n}")
    ancho_maximo = len(str(total_celdas))
    for fila in matriz:
        print(" ".join(str(val).rjust(ancho_maximo) for val in fila))

generar_matriz_espiral()