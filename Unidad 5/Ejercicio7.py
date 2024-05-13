import random

def numRandom():
    num = random.randint(0,500)
    print(num)
    return num

def ingresarNum():
    try:
        numIngresado = int(input("Ingrese un número entre 0 y 500 para adivinar"))
        if numIngresado < 0 or numIngresado > 500:
            raise ValueError("El número ingresado esta fuera de los límites")
        return numIngresado
    except TypeError as e:
        print(e)
    

def main():
    intentos = 0
    resultado = numRandom()
    while True:
        try:
            numIngresado = ingresarNum()
            if resultado == numIngresado:
                print("Usted adivinó")
                intentos +=1
                print(f"Adivinaste el número luego de {intentos} intentos")
                break;
            elif resultado > numIngresado:
                print("El número ingresado es menor")
                intentos +=1
            else:
                print("El número ingresado es mayor")
                intentos +=1
        except ValueError as e:
            print(e)

main()