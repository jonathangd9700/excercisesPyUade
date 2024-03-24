def alCuadrado(cantidad):
    i = 1
    lista = []
    while i <= cantidad:
        lista.append(i**2)
        i+=1
    return lista

def imprimirUltimosDiez(lista):
    print("Ultimos diez valores cargados:", end= " ")
    for i in range(len(lista)-10,len(lista)):
        print(lista[i],end = " ")
    
cantidad = int(input("Ingrese el numero hasta donde desee cargar la lista"))
listaCargada = alCuadrado(cantidad)
print(listaCargada)
imprimirUltimosDiez(listaCargada)