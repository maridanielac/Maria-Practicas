#Autoescuela La Rapida

type_vehicle = {"A":{"Automatico":int(2500)}, "S":{"Sincronico":int(3500)}}

while True: 
    cedula =(input("Ingrese su cedula: "))
    vehiculo =(input("Ingrese el tipo de vehiculo \n1-Automatico \n2- Sincronico \n -> "))
    #Falta como hacer para usar el typevehicle y tomar a info
    horas = (int(input("Introduzca las horas de clase que va a tomar")))
    #Falta saber como tomar el valor del tipo de carro, ya sea automatico o sincronico
    if vehiculo == "A":
        if horas > 3:
            valor = type_vehicle["A"]["Automatico"]
            monto = horas * valor
            descuento = (monto * 15)/100
            mtotal = monto - descuento
            print (f"El monto total a ser facturado es de: {mtotal}")
        elif horas <=3 or horas >= 1:
            val = type_vehicle["A"]["Automatico"]
            mtotal = horas * val
            print (f"El monto total a ser facturado es de: {monto}")  
    elif vehiculo == "S":
        if horas > 3:
            valor = type_vehicle["S"]["Sincronico"]
            monto = horas * valor
            descuento = (monto * 15)/100
            mtotal = monto - descuento
            print (f"El monto total a ser facturado es de: {mtotal}")
        elif horas <=3 or horas >= 1:
            val = type_vehicle["S"]["Sincronico"]
            mtotal = horas * val
            print (f"El monto total a ser facturado es de: {monto}")       

    client = {
        "id": cedula,
        "tipovehiculo": vehiculo, #Arreglar porque falta que aparezca el tipo de vehiculo
        "horas": horas,
        "monto total": mtotal
    }
    

    print (client)