def grabarRangoAlturas():
    deportes = []
    alturas = []
    while True:
        deporte = input("Ingrese deporte")
        deportes.append(deporte)
        with open("C:\\Users\\joniy\\Desktop\\UADE\\1AÑO\\SegundoCuatri\\Progra1\\Ejercicios\\Unidad6\\archivoEj3.txt","a") as f:
                f.write(deporte + "\n")
        while True:
            altura = input("Ingrese la altura en cm. Ingrese -1 para finalizar")
            if altura == "-1":
                break;
            with open("C:\\Users\\joniy\\Desktop\\UADE\\1AÑO\\SegundoCuatri\\Progra1\\Ejercicios\\Unidad6\\archivoEj3.txt","a") as f:
                f.write(altura + "\n")
        bandera = input("Ingrese 1 para ingresar otro deporte. Ingrese 2 para finalizar")
        if bandera == "2":
            break;
    return deportes

def grabarPromedios(lista):
    with open("C:\\Users\\joniy\\Desktop\\UADE\\1AÑO\\SegundoCuatri\\Progra1\\Ejercicios\\Unidad6\\archivoEj3.txt","r") as f:
        datos = f.readlines()
        print(datos)
        i = 0
        suma = 0
        for linea in datos:
            print(linea)
            if lista[i] == linea:
                print(linea)
            else:
                suma += int(linea)
            i+=1
    print(suma)

deportes = grabarRangoAlturas()
grabarPromedios(deportes)
print(deportes)