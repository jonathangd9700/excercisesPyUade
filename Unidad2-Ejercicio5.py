#Ejercicio 5

import random;

def cargarLista():
    lista = []

    for i in range(0,10):
        numero = random.randint(0,50)
        lista.append(numero)
    return lista

def ordenarListaAsc(lista):
    for i in range(len(lista)):
        for a in range(i+1, len(lista)):
            if lista[a] < lista[i]:
                aux = lista [a]
                lista[a] = lista[i]
                lista[i] = aux
    return lista

def ordenarListaDesc(lista):
    for i in range(len(lista)):
        for a in range(i+1, len(lista)):
            if lista[a] > lista[i]:
                aux = lista [a]
                lista[a] = lista[i]
                lista[i] = aux
    return lista

def ascendente(lista):
    largoLista = len(lista)
    ascendente = True
    if(lista[0] < lista[largoLista-1]):
        return ascendente
    else:
        ascendente = False
        return ascendente
        
        
def main():
    listaCargada = cargarLista()
    print(f"Lista desordenada {listaCargada}")
    numero = random.randint(0,1)
    if(numero == 1):
        ordenarListaAsc(listaCargada)
    else: 
        ordenarListaDesc(listaCargada)
    print(f"Lista ordenada: {listaCargada}")
    ordenLista = ascendente(listaCargada)
    if(ordenLista == True):
        print("La lista está ordenada de forma ascendente")
    else:
        print("La lista está ordenada de forma descendente")
main()
