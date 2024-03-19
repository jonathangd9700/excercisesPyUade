"""Informar si un número es oblongo. Se dice que un número es oblongo cuando
se puede obtener multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de multiplicar 2 * 3."""
naturales = [1,2,3,4,5,6,7,8,9]
def oblongo(numero,lista):
    esOblongo = False
    for i in range(len(lista)):
        if(numero== naturales[i]*naturales[i+1]):
            esOblongo = True
        return esOblongo
numero = int(input("Ingrese el numero para saber si es oblongo"))
verificar = oblongo(numero,naturales)
if(verificar == True):
    print("El numero es oblongo")
else:
    print("El numero no es oblongo")