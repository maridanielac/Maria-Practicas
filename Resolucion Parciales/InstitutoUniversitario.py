#Instituto Universitario

while True: 
    cedula = (input("Introduce tu cedula"))
    promedio_notas_primaria = int(input("Introduce tu promedio de  educación primaria:"))
    promedio_notas_media = int(input("Introduce tu promedio de educación media:"))

    promedio = (promedio_notas_primaria+promedio_notas_media)/2

    aspirantes = 0
    alumnos_uno =0
    alumnos_dos =0
    promedio_total=0
    prom_aspirantes=0
    trimestre=0

    print ("Cedula: ", cedula)
    print ("Promedio de Notas: ", promedio)
    if promedio >= 18:
        print ("Estas ubicado en el trimestre Dos")
        promedio += promedio_total
        aspirantes +=1
        alumnos_dos +=1
        trimestre +=1
    elif promedio >= 12 and promedio <18:
        print ("Estas ubicado en el trimestre Uno ")
        promedio += promedio_total
        aspirantes+=1
        alumnos_uno +=1
        trimestre +=1
    elif promedio < 12:
        print ("Rechazado")
        aspirantes +=1
    total_day= aspirantes + alumnos_uno + alumnos_dos
    trimestre_1= alumnos_uno + alumnos_dos
    if (input ("Do you want to continue Y-yes or N-No")) == "V":
        break 
    
    print ("***Datos Instituto Universitario***")
    print ("Cantidad alumnos aspirantes", aspirantes)
    print ("Cantidad de alumnos por trimestre uno: ", alumnos_uno)
    print ("Cantidad de alumnos por trimestre uno: ", alumnos_dos)
    if(aspirantes > 0):
        print("Promedio de aspirantes por trimestre:",total_day/aspirantes)
    if trimestre > 0:
        print ("Promedio General del trimestre:",trimestre_1/aspirantes)
    
    
    
    