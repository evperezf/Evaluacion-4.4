def asientosDisp(asiento):
    asiento = asiento - asComp
    return asiento
def vueloAnulado(asiento):
    asiento = asiento + asComp
    return asiento
asiento = 30
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
            print("asientos disponibles",asiento)
        if op == 2:
            asComp = int(input("¿Cuantos asientos desea comprar?: "))
            asiento = asientosDisp(asiento)
            print("asientos disponibles: ",asiento)
        if op == 3:
            anular = int(input("¿desea anular vuelo? (1=si, 2=no): "))
            if anular == 1:
                asiento = vueloAnulado(asiento)
                print("asientos disponibles: ",asiento)
    except:
        print("Debe ingresar un numero")

    

