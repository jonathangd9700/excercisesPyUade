import random;

def cargarLista1():
    lista = []
    cargar = random.randint(10,99)
    i = 0
    while i < 5:
        numeroRandom = random.randint(0,1)
        lista.append(numeroRandom)
        i += 1
    print(f"Lista generada aleatoriamente: {lista}")
    return lista

def sumarLista(listaCompleta):
    sumaLista = 0
    for i in range(len(listaCompleta)):
        sumaLista += listaCompleta[i]
    print("La suma de los elementos de la lista es: ",end="")
    print(sumaLista)
    return sumaLista

def eliminarValor(valor,lista):
    i=0
    largoLista = len(lista)
    while i < largoLista:
        if valor == lista[i]:
            del lista[i]
            i -=1
            largoLista = len(lista)
        i +=1
    print(lista)

def esCapicua(lista):
    for i in range (len(lista)-1,-1,-1):
        print(lista[i], end= " ")
    print()
    for a in range(len(lista)):

        print(lista[a], end = " ")
    
def esCapicua(lista):
    inicio = 0
    fin = len(lista)-1

    while inicio < fin:
        if lista[inicio] != lista[fin]:
            return print("La lista no es capicúa")
        else:
            inicio += 1
            fin -= 1
    if inicio == fin:
        print("Es capicúa")

         

listaAleatoria = cargarLista1()
sumarLista(listaAleatoria)
eliminarValor(5,listaAleatoria)
esCapicua(listaAleatoria)

