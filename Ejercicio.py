import numpy as np
from sqlalchemy import desc
bancoduoc = 0
descuento = 0.15
def comprarAsientos():
    print("comprar asientos")
    print("favor ingresar datos")
    print("*"*30)
    nombrePasajero=(input("Nombre: "))
    rutPasajero=""
    while len(rutPasajero) != 10:
        rutPasajero=str(input("Rut (con guion y digito verificador): "))    
    telefonoPasajero= ""
    while len(str(telefonoPasajero)) !=8:    
        telefonoPasajero=int(input("Telefono: (9) "))   
asientosList_Norm = [str(x) for x in range(1,31)]
asientoVend = 0  
arrayNorm =np.array(asientosList_Norm).reshape(5,6)
for fila in range(5):
    for asiento in range(6):
        if asientoVend == arrayNorm[fila][asiento]:
            arrayNorm[fila][asiento] = "X"
asientosList_Vip = [str(x) for x in range(31,43)]
asientoVend = 0  
arrayVip =np.array(asientosList_Vip).reshape(2,6)
for fila in range(2):
    for asiento in range(6):
        if asientoVend == arrayVip[fila][asiento]:
            arrayVip[fila][asiento] = "X"
valorAVp = 240000
valorAsn = 78900
normal = 30
vip = 12
asComp = 0
op = 4
while op !=5:
    print("Bienvenido a Vuelos-Duoc en que lo podemos ayudar.")
    print("*"*50)
    print("1.- Ver asientos disponibles.")
    print("2.- Comprar asientos.")
    print("3.- Anular vuelo.")
    print("4.- Modificar datos de pasajero.")
    print("5.- Salir")
    print("*"*50)
    try:
        op = int(input("Ingresar una opcion (1-5): "))
        if op == 1:
            print(arrayNorm)
            print(arrayVip)
            print("asientos disponibles: \n",normal, " Asientos Normales\n", vip, " Asientos Vip")
        if op == 2:
            comprarAsientos()
            bancoPasajero = input("Banco: ")
            if bancoPasajero == "bancoDuoc":
                valorAVipdesc = valorAVp*descuento
                valorAsndesc=valorAsn*descuento
                valorAsn = valorAsn - valorAsndesc
                valorAVp = valorAVp - valorAVipdesc
                print("*"*30)
            asComp = int(input("¿que asiento desea comprar? (1. normal y 2. es vip):  "))
            if asComp == 1:
                asNorm = int(input("indicar cantidad de asientos que comprara: "))
                print(arrayNorm)                
                cantAsn = asNorm*valorAsn
                for i in range(asNorm):
                    asientoVend = input("eliga asientos: ")
                    for fila in range(5):
                         for asiento in range(6):
                            if asientoVend == arrayNorm[fila][asiento]:
                                arrayNorm[fila][asiento] = "X"
                                print(arrayNorm)
                                print(arrayVip)                        
                print(" Total asientos comprados: ",asNorm,"\n","Monto total a pagar: ""$",cantAsn)
            if asComp == 2:
                asVip = int(input("indicar cantidad de asientos que comprara: "))
                print(arrayVip)
                cantAsv = asVip*valorAVp
                for i in range(asVip):
                    asientoVend = input("eliga asientos: ")
                    for fila in range(2):
                         for asiento in range(6):
                             if asientoVend == arrayVip[fila][asiento]:
                                arrayVip[fila][asiento] = "X"
                                print(arrayNorm)
                                print(arrayVip)
            print(" Total asientos comprados: ",asVip,"\n","Monto total a pagar: ""$",cantAsv)
        if op == 3:
            asNorm = int(input("indicar cantidad de asientos a devolver: "))
            for i in range(asNorm):
                eliminar = input("eliga asientos: ")
                count = 0 
                if int(eliminar) <= 30:
                    for fila in range(5):
                        for asiento in range(6):
                            count = count + 1
                            if str(arrayNorm[fila][asiento]) == "X" and count == int(eliminar):
                                arrayNorm[fila][asiento] = count                           
                                print(arrayNorm)
                                print(arrayVip)
                else:
                    for i in range(asVip):
                        count = count + 30
                        for fila in range(2):
                            for asiento in range(6):
                                count = count + 1
                                if str(arrayVip[fila][asiento]) == "X" and count == int(eliminar):
                                    arrayVip[fila][asiento] = count 
                                    print(arrayNorm)
                                    print(arrayVip)      
        if op == 4:
            print("*"*30) 
            comprarAsientos()
            bancoPasajero = input("Banco: ")
            print("*"*30)    
    except:
        print("Debe ingresar un numero")
print("adios")