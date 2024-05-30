from pilas import *

def main():
    pila = crearPila()
    pilaAux = crearPila()
    print(pila)
    for i in range(3):
        numero = int(input("Ingrese un numero"))
        apilar(pila,numero)
    print(pila)
    suma = 0
    while esVacia(pila) == False:
        suma += desapilar(pila)
    print(suma)

    
main()