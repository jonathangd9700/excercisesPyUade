def  cargarNum():
    lista = []
    i = 0
    while (i<3):
        print("Ingrese un numero ", end="")
        numero = int(input())
        if(numero < 0):
            print("Ingrese un numero positivo")
        else:
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
        return mayor
    else:
        return -1
    

result = cargarNum()

result2 = buscarMayor(result)
if (result2 != -1):
    print("El mayor estricto es ",end ="")
    print(result2)
else:
    print("No se ingresò un nùmero mayor estricto")
