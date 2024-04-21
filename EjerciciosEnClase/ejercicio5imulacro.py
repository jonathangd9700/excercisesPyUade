#Ej5
#Realizar un programa que contenga una función que reciba una lista y un elemento.
#La función debe añadir el elemento al final de la lista con la condición de no repetir ningún elemento.
#Además si este elemento ya se encuentra en la lista se debe invocar un error de tipo ValueError
#que debes capturar y mostrar este mensaje en su lugar:

#Error: Imposible añadir elementos duplicados

#Nota: se deben utilizar al menos dos funciones y las excepciones que crea conveniente.
#Debe elevar excepciones entre funciones y utilizar las cláusulas else (si cree conveniente) y finally.

import random;

def listaElementos():
    lista = []
    i = 0
    while i < 20: 
        numeros = random.randint(0,5)
        lista.append(numeros)
        i+=1
    print(lista)
    return lista

def agregarElemento(lista,elemento):
    if elemento in lista:
        raise ValueError("Imposible agregar elementos duplicados")
    else:
        lista.append(elemento)
        return lista


def main():
    try:
        lista = listaElementos()
        elemento = int(input("Agregue un elemento"))
        listaFinal = agregarElemento(lista,elemento)
        print(listaFinal)
    except ValueError as e:
        print("Error: ",e)
    finally:
        print("Finalizó el programa")
    
        
        
main()