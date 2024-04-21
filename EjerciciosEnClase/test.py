def main():
    cadena = cargar_cadena()
    diccionario = contar_apariciones(cadena)
    imprimir_diccionario(diccionario)

def cargar_cadena():
    return input("Ingrese una cadena de caracteres: ")

def contar_apariciones(cadena):
    diccionario = {}
    for caracter in cadena:
        if caracter in diccionario:
            diccionario[caracter] += 1
        else:
            diccionario[caracter] = 1
    return diccionario

def imprimir_diccionario(diccionario):
    for caracter, cantidad in diccionario.items():
        print(f"'{caracter}': {cantidad}")

if __name__ == "__main__":
    main()
