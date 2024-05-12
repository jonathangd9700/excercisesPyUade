import random

def cargarCadenas():
    cadenaA = input("Ingrese numeros reales para la suma")
    cadenaB = input("Ingrese nuevamente números reales para la suma")
    return cadenaA, cadenaB

def sumarCadenas(cadenaA, cadenaB):
    try:
        sumaA = 0
        sumaB = 0
        listaA = cadenaA.split()
        for i in listaA:
            sumaA += int(i)
        listaB = cadenaB.split()
        for i in listaB:
            sumaB += int(i)
        return sumaA, sumaB
    except ValueError as e:
        raise ValueError("El valor ingresado no es correcto")
    except TypeError as e:
        raise TypeError("El valor ingresado no es correcto")

def main():
    while True:
        try:
            cadenaA, cadenaB = cargarCadenas()
            sumaA, sumaB = sumarCadenas(cadenaA, cadenaB)
            print(sumaA)
            print(sumaB)
            break;
        except ValueError as e:
            print(e)
        except TypeError as e:
            print(e)
        
main()
