import math 

def calcular_impuesto_progresivo():
    
    tramos = [
        (20000, 0),    
        (50000, 10),   
        (100000, 20),  
        (float('inf'), 30) 
    ]
    
    try:
        ingreso_mensual = float(input("Ingrese su sueldo mensual: "))
    except ValueError:
        print("Error: Ingrese un número válido para el sueldo mensual.")
        return

    ingreso_anual = (12 * ingreso_mensual) + (2 * ingreso_mensual)
    
    impuesto_total = 0.0
    ingreso_tramo_anterior = 0.0
    impuestos_por_tramo = []

    print(f"\nCálculo de Impuestos")
    print(f"Ingreso Mensual: ${ingreso_mensual:,.2f}")
    print(f"Ingreso Anual (Incluyendo Aguinaldos): ${ingreso_anual:,.2f}")
    print("-" * 30)

    for limite_superior, tasa in tramos:
        
        limite_imponible = min(limite_superior, ingreso_anual)
        monto_en_tramo = limite_imponible - ingreso_tramo_anterior
        
        if monto_en_tramo <= 0:
            break
            
        impuesto_tramo = monto_en_tramo * (tasa / 100)
        impuesto_total += impuesto_tramo
        
        impuestos_por_tramo.append({
            "rango": f"({ingreso_tramo_anterior:,.2f} - {limite_imponible:,.2f}]",
            "monto": monto_en_tramo,
            "tasa": tasa,
            "impuesto": impuesto_tramo
        })
        
        ingreso_tramo_anterior = limite_superior
        
        if limite_imponible == ingreso_anual:
            break

    print("Impuesto por Tramo:")
    for tramo in impuestos_por_tramo:
        print(f"  Rango {tramo['rango']} -> ${tramo['monto']:,.2f} x {tramo['tasa']}% = ${tramo['impuesto']:,.2f}")

    print("-" * 30)
    print(f"Total de Impuestos: ${impuesto_total:,.2f}")

    if ingreso_anual > 0:
        tasa_efectiva = (impuesto_total / ingreso_anual) * 100
        print(f"Tasa Efectiva Real: {tasa_efectiva:,.2f}%")
    else:
        print("Tasa Efectiva Real: 0.00%")

calcular_impuesto_progresivo()