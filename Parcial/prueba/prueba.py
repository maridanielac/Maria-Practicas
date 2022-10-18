type_vehicle = {"A":{"Automatico":2500}, "S":{"Sincronico":3500}}

print (type_vehicle["A"]["Automatico"])


#Prueba

#Autoescuela La Rapida

from multiprocessing import Value


type_vehicle = {"A":{"Automatico":2500}, "S":{"Sincronico":3500}}
valor = type_vehicle.values["A"]


horas = (int(input("Introduzca las horas de clase que va a tomar")))
#Falta saber como tomar el valor del tipo de carro, ya sea automatico o sincronico
monto = horas * type_vehicle.values["A"]

print (monto)