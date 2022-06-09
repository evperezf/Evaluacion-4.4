import numpy as np
from sqlalchemy import desc
bancoduoc = 0
descuento = 0.15
#def asientosDisp(asiento):
    #asiento = asiento - asComp
    #return asiento
#def vueloAnulado(asiento):
    #asiento = asiento + asComp
    #return asiento
def comprarAsientos():
    print("comprar asientos")
    print("favor ingresar datos")
    print("*"*30)
    nombrePasajero=(input("Nombre: "))
    rutPasajero=str(input("Rut: "))
    telefonoPasajero=int(input("Telefono: "))
    bancoPasajero=str(input("Banco: "))
    print("*"*30)

#def asientosDisp():   
asientosList_Norm = [str(x) for x in range(1,31)]
asientoVend = 0 #debe ser un opcion string? para que genere el cambio ya que todo debe ser extring ya que sino es imposible generar cuadraturas
# asientoVend = input("Que asiento desea ocupar")//pero si es string habria que poner un lowercase para que tome todas las combinaciones posibles para generar un pago o no?, no necestariamente, se deberia generara un arametro del 1-30 para que el monto sea asiento normal y otro del 31-42 asinto vip para cobrar monto mayor   
arrayNorm =np.array(asientosList_Norm).reshape(5,6)
for fila in range(5):
    for asiento in range(6):
        if asientoVend == arrayNorm[fila][asiento]:
            arrayNorm[fila][asiento] = "X"
asientosList_Vip = [str(x) for x in range(31,43)]
asientoVend = 0 #debe ser un opcion string? para que genere el cambio ya que todo debe ser extring ya que sino es imposible generar cuadraturas
# asientoVend = input("Que asiento desea ocupar")//pero si es string habria que poner un lowercase para que tome todas las combinaciones posibles para generar un pago o no?, no necestariamente, se deberia generara un arametro del 1-30 para que el monto sea asiento normal y otro del 31-42 asinto vip para cobrar monto mayor   
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
                          #asNorm = int(input("favor elegir asientos entre el 1 y el 30?: "))   
                          #asiento = asientosDisp(asiento)
                print("total: ",asNorm,"  $",cantAsn)
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
        if op == 3:

            for fila in range(5):
                for asiento in range(6):
                    if arrayNorm[fila][asiento] == "X":
                        arrayNorm[fila][asiento] = asientoVend
                        
                        print(arrayNorm)
                        print(arrayVip)
            
        if op == 4:
            print("*"*30) 
            comprarAsientos()
            print("*"*30)    
    except:
        print("Debe ingresar un numero")
print("adios")