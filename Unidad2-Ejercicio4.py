import random;

def cargarLista(cantidad):
    i = 0
    lista = []
    while i < cantidad:
        numero = random.randint(0,5)
        lista.append(numero)
        i+=1
    return lista

def eliminarValores(lista1,lista2):
    i = 0
    a = 0
    largo = len(lista1)
    eliminar = []
    while i < largo-1:
        for a in range(len(lista2)):
            if (lista1[i] == lista2[a]):
                del lista1[i]
                eliminar.append(lista2[a])
                largo = len(lista1)
            else:
                i+=1
    print(eliminar)
    print(lista1)

cantidad = int(input("Ingrese la cantidad a agregar a la lista"))

listaCargada = cargarLista(cantidad)

cantidad = int(input("Ingrese la cantidad a agregar a la lista"))

listaCargada2 = cargarLista(cantidad)

print(listaCargada)

print(listaCargada2)

eliminados = eliminarValores(listaCargada,listaCargada2)
