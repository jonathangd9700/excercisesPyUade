import random

numero = random.randint(1,5)
print(numero)
numIngresado = int(input("Ingrese el numero a adivinar"))

while True:
    if numIngresado == numero:
        print("Usted adivinó")
        break;
    elif numIngresado < numero:
        print("El numero secreto es mayor")
    elif numIngresado> numero:
        print("El numero secreto es menor")
    numIngresado = int(input("Ingrese el numero a adivinar"))




