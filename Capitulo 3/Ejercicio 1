horas_trabajadas = float(input("Ingresa el número de horas trabajadas: "))
tarifa_por_hora = float(input("Ingresa la tarifa por hora: "))

if horas_trabajadas > 40:
    horas_normales = 40
    horas_extra = horas_trabajadas - 40
else:
    horas_normales = horas_trabajadas
    horas_extra = 0

salario_bruto = (horas_normales * tarifa_por_hora) + (horas_extra * tarifa_por_hora * 1.5)


print(f"El salario bruto es: {salario_bruto}")
