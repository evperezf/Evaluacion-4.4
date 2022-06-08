import numpy as np
def asientosDisp(asiento):
    asiento = asiento - asComp
    return asiento
def vueloAnulado(asiento):
    asiento = asiento + asComp
    return asiento
asiento = 30
vip = 12
asComp = 0
op = 4

asientosList = [str(x) for x in range(1,43)]
asientoVend ="14" #debe ser un opcion string? para que genere el cambio ya que todo debe ser extring ya que sino es imposible generar cuadraturas
# asientoVend = input("Que asiento desea ocupar")//pero si es string habria que poner un lowercase para que tome todas las combinaciones posibles para generar un pago o no?, no necestariamente, se deberia generara un arametro del 1-30 para que el monto sea asiento normal y otro del 31-42 asinto vip para cobrar monto mayor
array =np.array(asientosList).reshape(7,6)
for fila in range(7):
    for asiento in range(6):
        if asientoVend == array[fila][asiento]:
            array[fila][asiento] = "X"
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
            print("asientos disponibles: \n",asiento, " Asientos Normales\n", vip, " Asientos Vip")
        if op == 2:
            asComp = int(input("¿Cuantos asientos desea comprar?: "))
            asiento = asientosDisp(asiento)
            print("asientos disponibles: ",asiento)
        if op == 3:
            anular = int(input("¿desea anular vuelo? (1=si, 2=no): "))
            if anular == 1:
                asiento = vueloAnulado(asiento)
                print("asientos disponibles: ",asiento)
            if anular == 2:
                print("gracias por no anular")
        if op == 4:
            print("continuara...")
        
    except:
        print("Debe ingresar un numero")
print("adios")