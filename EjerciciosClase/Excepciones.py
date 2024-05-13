#Excepciones
try:
    dividendo = int(input("Ingrese el dividendo: "))
    divisor = int(input("Ingrese el divisor: "))

    resultado = dividendo / divisor

    print(resultado)

except BaseException as e:
    print(e)
except ValueError:
    print("Ingresaste un caracter")