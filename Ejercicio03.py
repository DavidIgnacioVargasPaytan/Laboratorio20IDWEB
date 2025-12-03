salario_base = 5000.00          # Salario base mensual
horas_extras = 10               # Horas extras trabajadas
pago_hora_extra = 25.00         # Pago por hora extra
bono = 500.00                   # Bonificación
afp = 10.0                      # Tasa de descuento AFP en porcentaje
salud = 5.0                     # Tasa de descuento Salud en porcentaje

salario_bruto = salario_base + (horas_extras * pago_hora_extra) + bono

descuento_afp = salario_base * (afp / 100)
descuento_salud = salario_base * (salud / 100)
descuentos_totales = descuento_afp + descuento_salud

salario_neto = salario_bruto - descuentos_totales

print(f"--- Cálculo de Salario ---")
print(f"Salario Base: ${salario_base:.2f}")
print(f"Horas Extras (Ingreso): ${(horas_extras * pago_hora_extra):.2f}")
print(f"Bono: ${bono:.2f}")
print("-" * 30)
print(f"Salario Bruto (Ingresos Totales): ${salario_bruto:.2f}")
print(f"Descuento AFP ({afp}%): -${descuento_afp:.2f}")
print(f"Descuento Salud ({salud}%): -${descuento_salud:.2f}")
print(f"Descuentos Totales: -${descuentos_totales:.2f}")
print("-" * 30)
print(f"Salario Neto: ${salario_neto:.2f}")