import numpy as np

asientosList = [str(x) for x in range(1,43)]
asientoVend = input("Que numero de asiento desea: ") #debe ser un opcion string? para que genere el cambio ya que todo debe ser extring ya que sino es imposible generar cuadraturas
# asientoVend = input("Que asiento desea ocupar")//pero si es string habria que poner un lowercase para que tome todas las combinaciones posibles para generar un pago o no?, no necestariamente, se deberia generara un arametro del 1-30 para que el monto sea asiento normal y otro del 31-42 asinto vip para cobrar monto mayor
array =np.array(asientosList).reshape(7,6)
for fila in range(7):
    for asiento in range(6):
        if asientoVend == array[fila][asiento]:
            array[fila][asiento] = "X"
           
            #for array in asientosList: # se debe pasar la array a string, pero como??
print(array)