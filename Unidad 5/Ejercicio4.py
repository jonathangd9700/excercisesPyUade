def imprimirNumeros():
    try:
        for i in range(0,10000):
            print(i)
    except KeyboardInterrupt:
        cancelar = input("Desea cerrar la aplicación? S para Sí - N para No")
        if cancelar.upper() == "S":
            raise KeyboardInterrupt("Fin del programa")
        else:
            print("Continuando...")
try:
    resultado = imprimirNumeros()
except KeyboardInterrupt as e:
    print(e)
