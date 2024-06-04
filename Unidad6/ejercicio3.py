def grabarRangoAlturas():
    while True:
        deporte = input("Ingrese deporte")
        with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\Unidad6\\alturas.txt","a") as f:
                f.write(deporte + "\n")
        while True:
            altura = input("Ingrese la altura en cm. Ingrese -1 para finalizar")
            if altura == "-1":
                with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\Unidad6\\alturas.txt","a") as f:
                    f.write("\n")
                break;
            with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\Unidad6\\alturas.txt","a") as f:
                f.write(altura + "\n")
        bandera = input("Ingrese 1 para ingresar otro deporte. Ingrese 2 para finalizar")
        if bandera == "2":
            break;

def grabarPromedios():
    with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\Unidad6\\alturas.txt","r") as f:
        datos = f.readlines()
        suma = 0
        contador = 0
        i = 0
        while i <= len(datos)-1:
            with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\Unidad6\\promedios.txt","a") as f:
                if i == 0:
                    f.write(datos[i])
                elif i > 0 and datos[i] != "\n":
                    suma += int(datos[i])
                    contador +=1
                else:
                    i +=1
                    promedio = suma/contador
                    f.write(str(promedio) + "\n")
                    f.write(datos[i])
                    contador = 0
                    suma = 0
                    promedio = 0
                if i == len(datos)-1:
                    promedio = suma/contador
                    f.write(str(promedio))
                    contador +=1
            i +=1

# def mostrarMasAltos():
    

# grabarRangoAlturas()
grabarPromedios()
# mostrarMasAltos()
