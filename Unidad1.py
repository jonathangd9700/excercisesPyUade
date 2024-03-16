def  cargarNum():
    lista = []
    i = 0
    while (i<3):
        print("Ingrese un numero")
        numero = int(input())
        lista.append(numero)
        i+=1
    return lista

def buscarMayor(lista):
    mayor = lista[0]
    encontrado = 0
    estricto = False
    for i in range(len(lista)):
        if(lista[i]>mayor):
            mayor= lista[i]
    for i in range(len(lista)):
        if(mayor == lista[i]):
            encontrado+=1
    if(encontrado >1):
        estricto = True
    if (estricto == False):
        return -1
    else:
        return mayor
    

result = cargarNum()
print(result)

buscarMayor(result)