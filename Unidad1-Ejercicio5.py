"""Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3."""
naturales = [1,2,3,4,5,6,7,8,9]
def oblongo(numero,lista):
    esOblongo = False
    for i in range(len(lista)-1):
        if(numero== naturales[i]*naturales[i+1]):
            esOblongo = True
    return esOblongo
numero = int(input("Ingrese el numero para saber si es oblongo"))
verificar = oblongo(numero,naturales)
if(verificar == True):
    print("El numero es oblongo")
else:
    print("El numero no es oblongo")
    
"""5 - B ---------------------------"""

def triangular(numero,combinaciones):
    esTriangular = False
    for i in range(len(combinaciones)):
        if numero == combinaciones[i]:
            esTriangular = True
    if esTriangular == True:
        print("Es triangular")
    else:
        print("No es triangular")

combinaciones = []
acumulador = 0
lista = [1,2,3,4,5,6,7,8,9]
vueltas = 0
for i in range(len(lista)):
    if vueltas == 0:
        acumulador = 1
    else:
        acumulador = 0
    for a in range(i+1,len(lista)):
        acumulador +=  lista[a]
        combinaciones.append(acumulador)
    vueltas = 1
numero = int(input("Ingrese un numero para saber si es triangular"))
triangular(numero,combinaciones)