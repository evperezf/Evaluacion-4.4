asientoNormal: 78900
asientoVip: 240000
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
        op = False
    except:
        print("Debe ingresar un numero")
        
