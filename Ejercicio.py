<<<<<<< HEAD
asiento = 30
asComp = 0
=======
asientoNormal: 78900
asientoVip: 240000
>>>>>>> 8aa527c8a96850e1513bbf53a6365b67ec0ad416
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
            asiento = asiento - asComp
    except:
        print("Debe ingresar un numero")

    

