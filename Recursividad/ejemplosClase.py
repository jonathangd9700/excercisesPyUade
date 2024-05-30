# def imprimir(x):
#     if x > 0:
#         imprimir(x-1)
#         print(x)
# 
# numero = int(input("Ingrese un numero"))
# 
# def calcularFactorial(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero * calcularFactorial(numero - 1)
#     
# resultado = calcularFactorial(numero)
# print(resultado)

# numero = int(input("Ingrese un numero"))

# def sumarNumeros(numero):
#     if numero == 1:
#         return 1
#     else:
#         return numero + sumarNumeros(numero-1)
#     
# resultado = sumarNumeros(numero)
# print(resultado)

lista = [1,2,10]
# 
# def sumarLista(indice,lista):
#     if indice == 0:
#         return lista[indice]
#     else:
#         return lista[indice] + sumarLista(indice-1, lista)
#     
# resultado = sumarLista(len(lista)-1,lista)
# 
# print(resultado)

# def sumarLista(lista):
#     if len(lista) == 1:
#         return lista[0]
#     return lista[len(lista)-1] + sumarLista(lista[:-1])
# 
# resultado = sumarLista(lista)
# print(resultado)

def sumar(numA,numB):
    if numA == 1:
        return numB
    else:
        return numB + sumar(numA-1, numB)
    
resultado = sumar(3,2)

print(resultado)