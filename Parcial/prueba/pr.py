type_vehicle = {"A":{"Automatico":2500}, "S":{"Sincronico":3500}}
horas = (int(input("Introduzca las horas de clase que va a tomar")))
valor = type_vehicle["A"]["Automatico"]
monto = horas * valor
descuento = (monto * 15)/100
mtotal = monto - descuento
print (mtotal)

