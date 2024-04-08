
#Ejercicio 8

def devolverSubcadena(cadena,N):
    inicio = len(cadena)-N
    subcadena = cadena[inicio:]
    return subcadena

def main():
    cadena = input("Ingrese una frase: ")
    nCaracteres = int(input(f"Escoja la cantidad de caracteres menor o igual a {len(cadena)}: "))
    while nCaracteres > len(cadena):
        nCaracteres = int(input(f"Escoja la cantidad de caracteres menor o igual a {len(cadena)}"))
    subcadena = devolverSubcadena(cadena,nCaracteres)
    print(subcadena)
    
main()