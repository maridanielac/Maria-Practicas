def welcome():
    print ("***Welcome***")

def get_user_option(dict):
    for key, value in dict.items():
        for key, value_interno in value.items():
            print (f"{key} - {value_interno}", end = "")
        print ("")
    return input ("Please enter a option: ")

def get_client_data(study):
    client = {
        "id": input ("Please enter the client id"),
        "age": input("Please enter the client age:"),
        "gender": input("Please enter the client M or F"),
        "study": study
    }
    return client

def print_invoice(client):
    print ("***Receipt***")
    print ("ID: ", client.get("id"))
    print ("Age: ", client.get("age"))
    print ("Gender: ", client.get("gender"))
    print ("Total: ", client.get("total"))

def get_amount (cliente,estudios):
    return estudios.get(cliente.get("study")).get("price")

def get_discount(client,net_amount,cont):
    discount = 0
    