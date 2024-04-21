# Realizar un algoritmo en el cual el usuario/a ingrese dos cadenas de caracteres conteniendo números reales,
# sume ambos valores y devuelva el resultado como un número real. Informar con el booleano False si alguna de
# las cadenas no contiene un número válido, utilizando manejo de excepciones para detectar el error. 
# 
# Ej.
# Si numero1= 3.1 y numero2= 1.4
# La suma es 4.5
# 
# Si numero1= 3.1 y numero2= “sd”
# False
# 
# Nota: Utilizar al menos dos funciones, la primera para el programa principal y la segunda para la suma de los valores.
# Debe elevar excepciones entre funciones y utilizar la cláusula else (si cree conveniente) y finally.

#Necesito convertir dos cadenas de caracteres en numeros reales y sumarlos. Si, alguno de los dos o los dos no es un numero válido, debo devolver False.

def suma(numero1,numero2):
    try:
        n1Float = float(numero1)
        n2Float = float(numero2)
        suma = n1Float+n2Float
        return suma
    except ValueError:
        raise ValueError("Valor no válido ingresado")
        return False
def main():
    while True:
        try:
           numero1 = input("Ingrese un primer numero")
           numero2 = input("Ingrese un segundo numero")
           resultado = suma(numero1,numero2)
           if resultado is not None:
               print("La suma es: ",resultado)
               break;
        except ValueError as e:
            print("Error ", e)
main()
