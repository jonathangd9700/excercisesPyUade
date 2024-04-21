#Ej3
#Escribe un programa que lea una cadena de caracteres y devuelva un diccionario con la cantidad
#de apariciones de cada carácter en la cadena. Nota: Utilizar al menos cuatro funciones,
#se recomienda la primera para el programa principal, la segunda para la carga de la cadena,
#la tercera para calcular la cantidad de apariciones de cada carácter y la última para la impresión del diccionario.


def frase():
    frase = input("Ingrese una frase")
    return frase

def calculo(cadena):
    diccionario = {}
    for caracter in cadena:
        if caracter not in diccionario:
            diccionario[caracter] = 1
        else:
            diccionario[caracter]+=1
    return diccionario

def imprimirDiccionario(resultadoDiccionario):
    for clave, valor in resultadoDiccionario.items():
        print(f"El caracter \'{clave}\' tiene {valor} apariciones en la cadena")

def main():
    cadena = frase()
    resultadoDiccionario = calculo(cadena)
    imprimirDiccionario(resultadoDiccionario)
    
main()

