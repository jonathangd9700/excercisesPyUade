# Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
# utilizar cadenas de caracteres.

def cantidadDigitos(numero):
    if numero >=-9 and numero<= 9:
        return 1
    else:
        return 1 + cantidadDigitos(numero//10)

numero = int(input("Ingrese un numero"))

resultado = cantidadDigitos(numero)

print(f"El numero ingresado tiene {resultado} digitos")

