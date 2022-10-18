#Autoescuela la rapida Horas de clase de manejo de todos sus clientes

def print_welcome():
    print ("***Welcome***")

def get_user_option(dict):
    for key, value in dict.items():
        for key_interno , value_interno in value.items():
            print (f"{key} - {value_interno}", end = "")
        print ("")
    return (input("Please enter a option: "))

def get_client_data(client):
    client = { "id": (input ("Introduce tu numero de cedula: ")), 
    "hora": (input("Introduce el numero de horas de clase que vas a tomar: ")) }
    return client

def print_invoice(client):
    print ("***Receipt***")
    print ("Cédula: ", client.get("id"))
    print ("Horas de clase: ", client.get("hora"))
    print ("Tipo de Vehiculo: ", )

def main():
    vehiculo = {"A":{"Automatico":2500,}, "S":{"Sincronico":3500}}

    clients = []
    print_welcome()
    while True: 
        option = get_user_option(vehiculo)
        client = get_client_data(option)
        get_netamount= ()
        print_invoice (client)
        clients.append(client)

main()