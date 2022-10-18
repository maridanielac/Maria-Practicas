#Autoescuela La Rapida

print ("***Bienvenido a la Autoescuela La Rapida***")
type_vehicle = {"A":{
    "name": "Automatico",
    "precio":2500}, 
    "S":{
    "name": "Sincronico",
    "precio": 3500
}}

client = 0
client_a =0
client_s=0
discount = 0

while True: 
    cedula = input ("Introduzca su cedula: ")
    tipo_vehiculo = input ("Introduzca el tipo de vehiculo: \nA - Automatico  \nS - Sincronico \n->")
    horas = int(input("Introduzca el numero de horas de clase: "))
    price = type_vehicle.get(tipo_vehiculo).get("precio")
    if horas > 3:
        if tipo_vehiculo == "A":
            monto_total_a= price * horas
            discount_a = (monto_total_a*0.15)/100
            monto_total_aa = monto_total_a -discount_a
        if tipo_vehiculo == "S":
            monto_total_b= price * horas
            discount_b = (monto_total_b*0.15)/100
            monto_total_bb = monto_total_b -discount_b
    elif horas <= 3 or horas >= 1:
        if tipo_vehiculo == "A":
            monto_total_a= price * horas
        if tipo_vehiculo == "S":
            monto_total_b= price * horas

    option = type_vehicle.get(tipo_vehiculo).get("name")
    
    #End oF day
    if tipo_vehiculo == "A":
        client +=1
        client_a +=1
        discount_a += discount
    elif tipo_vehiculo == "S":
        client +=1
        client_s +=1
        discount_b += discount
    
    print ("***RECEIPT***")
    print ("Cedula:", cedula)
    print ("Tipo de vehiculo:", option)
    
    if (input ("Do you want to continue Y-yes or N-No")) == "V":
        break 
    
    print ("***End of the Day")
    print ("Cantidad total de clientes: ", client)
    print ("Cantidad total por vehiculos automaticos: ", client_a)
    print ("Cantidad total por vehiculos automaticos: ", client_s)
    print ("Cantidad de clientes con descuento: ", discount)
    #Falta promedio de faturación por tipo de vehiculo

