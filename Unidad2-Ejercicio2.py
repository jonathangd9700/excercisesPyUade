import random;

def cargarLista(cantidad):
    i = 0
    lista = []
    while i< cantidad:
        numero = random.randint(0,100)
        lista.append(numero)
        i+=1
    return lista

def hayRepetidos(lista):
    repetido = False
    for i in range(len(lista)):
        for a in range(i+1, len(lista)):
            if(lista[i]==lista[a]):
                repetido = True
                return repetido
    return repetido
            
def sacarRepetidos(lista):
    i=0
    a= i+1
    largoLista = len(lista)
    while i < largoLista:
        while a < largoLista:
            if (lista[i]==lista[a]):
                del lista[a]
                largoLista = len(lista)
                a-=1
            a+=1
        i+=1
        a = i+1
    return lista
                

def main():
    cantidad = int(input("Ingrese la cantidad de numeros que desea cargar a la lista"))
    listaCargada = cargarLista(cantidad)
    print(listaCargada)
    repetidos = hayRepetidos(listaCargada)
    if(repetidos == True):
        print("Hay elementos repetidos en la lista")
    else:
        print("La lista no repite elementos")
    listaSinRepetidos = sacarRepetidos(listaCargada)
    print(f"Se eliminaron los elementos repetidos de la lista: {listaSinRepetidos}")

main()