def calcularGastos(cantidadViajes):
    if(cantidadViajes <=20):
        print("Averiguar en internet el valor actualizado")
    elif(cantidadViajes>20 and cantidadViajes <= 30):
        print("20% descuento sobre la tarifa maxima")
    elif(cantidadViajes>30 and cantidadViajes < 40):
        print("30% descuento sobre la tarifa maxima")
    elif(cantidadViajes>40):
        print("40% descuento sobre la tarifa maxima")

def ingresarViajes():
    i = 0
    while (i == 0):
         print("Ingrese la cantidad de viajes a realizar en el mes ", end="")
         cantidadViajes = int(input())
         if cantidadViajes > 0:
             i = 1
    return cantidadViajes

cantidad = ingresarViajes()
calcularGastos(cantidad)