import random
import statistics
import csv

def asignar_sueldo_aleatorios(trabajadores):
    sueldo_trabajadores = {}

    for trabajador in trabajadores:
        sueldo = random.randint(300000,2500000)
        sueldo_trabajadores[trabajador] = sueldo

    print("Sueldo asignados con exito")
    print(sueldo_trabajadores)

    return sueldo_trabajadores

def clasificar_sueldos(sueldo_trabajadores):

    menor_800 = {}
    entre_800_y_2000000 = {}
    superior_2000000 = {}

    for trabajador, sueldo in sueldo_trabajadores.items():
        if sueldo < 800000:
            menor_800[trabajador] = sueldo

        elif sueldo <= 2000000:
            entre_800_y_2000000[trabajador] = sueldo

        else:
            superior_2000000[trabajador] = sueldo

    print("Menor $800.000 Total", len(menor_800))
    for trabajador,sueldo in menor_800.items():
        print(trabajador, ": $",sueldo)

    print("Entre $800.000 y $2.000.000 Total", len(entre_800_y_2000000))
    for trabajador,sueldo in entre_800_y_2000000.items():
        print(trabajador, ": $",sueldo)
        
    print("Superior $2.000.000 Total", len(superior_2000000))
    for trabajador,sueldo in superior_2000000.items():
        print(trabajador, ": $",sueldo)

    sueldo = (sueldo_trabajadores.values())
    sueldos = sum(sueldo)
    

    print("TOTAL: $",sueldos)
    
def estadisticas_sueldos(sueldo_trabajadores):

    sueldo = (sueldo_trabajadores.values())

    if sueldo is None:
        print("No hay sueldos asignados")
        return None, None, None

    Sueldo_alto = max(sueldo)
    Sueldo_bajo = min(sueldo)
    Promedio_sueldos = sum(sueldo) / len(sueldo)
    Media_geometrica = statistics.geometric_mean(sueldo)

    return sueldo,Sueldo_alto,Sueldo_bajo,Promedio_sueldos,Media_geometrica

def generar_reporte(sueldo_trabajadores):

    for sueldo in sueldo_trabajadores.values():
        descuento_salud = sueldo * 0.07
        descuento_afp = sueldo * 0.12
        sueldo_liquido = sueldo - descuento_salud - descuento_afp

    with open("Reporte_sueldos.csv", "w", newline="") as archivo:
        escritor = csv.writer(archivo, delimiter=",")
        escritor.writerow(["Nombre empleado", "Sueldo base", "Descuento Salud", "Descuento AFP", "Sueldo liquido"])

        for trabajador,sueldo in sueldo_trabajadores.items():
            escritor.writerow([trabajador, sueldo, descuento_salud, descuento_afp, sueldo_liquido])
    
    print("Reporte generado con exito")