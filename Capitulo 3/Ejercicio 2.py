while True:
    try:
        horas_input = input("Introduzca las Horas: ")
        if horas_input.lower() == "salir":
            print("¡Hasta luego!")
            break
        
        horas_trabajadas = float(horas_input)

        tarifa_input = input("Introduzca la Tarifa por hora: ")
        tarifa_por_hora = float(tarifa_input)

        if horas_trabajadas > 40:
            horas_normales = 40
            horas_extra = horas_trabajadas - 40
        else:
            horas_normales = horas_trabajadas
            horas_extra = 0

        salario_bruto = (horas_normales * tarifa_por_hora) + (horas_extra * tarifa_por_hora * 1.5)

        print(f"El salario bruto es: {salario_bruto}")
    
    except ValueError:
        print("Error, por favor introduzca un número")