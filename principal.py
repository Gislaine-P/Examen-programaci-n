import funciones as fn

trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","Miguel Sánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]

sueldo_trabajadores = {}

while True:
    print("MENU")
    print("1. inicializar sueldos")
    print("2. Asignar sueldos aleatorios")
    print("3. Clasificar sueldos")
    print("4. Ver estadísticas.")
    print("5. Reporte de sueldos")
    print("6. Salir del programa")

    try:
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            sueldo_trabajadores = {trabajador : 0 for trabajador in trabajadores}
            print("Sueldos inicializados correctamente")
        elif opcion == 2:
            if not sueldo_trabajadores:
                print("Debe inicializar los sueldos")
            else:
                sueldo_trabajadores = fn.asignar_sueldo_aleatorios(trabajadores)
        elif opcion == 3:
            if sueldo_trabajadores:
                fn.clasificar_sueldos(sueldo_trabajadores)
            else:
                print("Debe inicializar los sueldos")
        elif opcion == 4:
            if sueldo_trabajadores:
                sueldo,Sueldo_alto,Sueldo_bajo,Promedio_sueldos,Media_geometrica = fn.estadisticas_sueldos(sueldo_trabajadores)
                if sueldo is not None:
                    print("Sueldo más alto: $",Sueldo_alto)
                    print("Sueldo más bajo: $", Sueldo_bajo)
                    print("Promedio de sueldos: ",Promedio_sueldos)
                    print("Media geométrica:",Media_geometrica)
        elif opcion == 5:
            if sueldo_trabajadores:
                fn.generar_reporte(sueldo_trabajadores)
            else:
                print("Debe inicializar los sueldos")
        elif opcion == 6:
            print("Finalizando programa…")
            print("Desarrollado por Gislaine Paredes")
            print("RUT 21.452.683-2")
            break
        else:
            print("Opción no valida, intente nuevamente")
    except ValueError:
        print("Debe ingresar una opción numerica.")
