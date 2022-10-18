#Empresa Saman Internacional
def is_primo(rif):
    number = int (rif[-1])
    aux = number -1 
    while aux > 1:
        if number %aux == 0:
            return False 
        aux -=1
    return True


products = {"Q":{
    "name":"Químicos",
    "price": 1000},
    "F":{
    "name":"Farmaceutico",
    "price": 2500},
    "B":{
    "name":"Biológicos",
    "price": 4000
}}

client_f = 0
client_q = 0
client_b = 0
discount_f = 0
discount_q = 0
discount_b = 0
max_purchase = 0
rif_max_purchase = 0
total_day = 0
while True: 
    rif = (input("Introduzca su rif"))
    line_product = (input("Introduzca la linea del producto a comprar \nQ- Quimico \nF- Farmaceutico \nB- Biologico \n->  "))
    code_pago = (input("Introduzca el metodo de pago \nC- Contado \nF- Crédito \n-> "))
    gross_amount = products.get(line_product).get("price") #Interesante (lo que estabas buscando ayer)
    discount = 0
    recharge = 0
    tax = 0

    #Discounts 
    if code_pago == "C":
        discount += gross_amount *0.03
    if gross_amount %2 == 0:
        discount += gross_amount *0.02
    if is_primo(rif):
        discount += gross_amount *0.05
    
    #Taxes
    if line_product != "F":
        tax += gross_amount *0.12

    #Total
    total = gross_amount + recharge - discount + tax

    #End of the day 
    total_day += total
    if line_product == "F":
        client_f +=1
        discount_f += discount 
    elif line_product == "Q":
        client_q +=1
        discount_f += discount 
    elif line_product == "B":
        client_f +=1
        discount_b += discount 

    if total > max_purchase: 
        rif_max_purchase = rif 
        max_purchase = total
    
        #Factura
        print ("***RECEIPT***")
        print ("Rif", rif)
        print ("Product", products.get(line_product).get("description"))
        print ("Payment method", code_pago)
        print ("Discount", discount)
        print ("Tax", tax)
        print ("Total", total)
        if (input ("Do you want to continue Y-yes or N-No")) == "V":
            break 
    print ("**End of the day***")
    print ("Client F", client_f)
    print ("Client Q", client_q)
    print ("Client B", client_b)
    print ("Discount F", discount_f)
    print ("Discount Q", discount_q)
    print ("Discount B", discount_b)
    print ("Rif Maximun Purchase", rif_max_purchase)
    print ("Total", total_day)
