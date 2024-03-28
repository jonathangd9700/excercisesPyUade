def centrarCadena(cadena):
    ancho = 100
    espacioIzq= (ancho - len(cadena)) // 2
    print(" " * espacioIzq + cadena)

cadena = input("Ingrese una frase: ")
centrarCadena(cadena)


