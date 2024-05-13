contador = 0
def imprimirNumeros(contador):
    try:
        for i in range(contador, 10000):
            print(i)
            contador = i+1
    except KeyboardInterrupt:
        cancelar = input("\nDesea cerrar la aplicación? S para Sí - N para No: ")
        if cancelar.upper() == "S":
            print("Fin del programa")
        else:
            print("Continuando...")
            imprimirNumeros(contador)

imprimirNumeros(contador)

