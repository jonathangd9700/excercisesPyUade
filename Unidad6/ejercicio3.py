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

def pruebaLeer():
    i = 0
    with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\Unidad6\\alturas.txt","r") as f:
        datos = f.readlines()
        suma = 0
        i = 0
#         while i < len(datos) -1 and i<=3 :
#             suma += int(datos[i])
#             i+=1
#         print(suma)
#         suma = 0
        while i < len(datos)-1:
            with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\Unidad6\\promedios.txt","a") as f:
                if i == 0:
                    f.write(datos[i])
#                     suma += int(datos[i])
                elif i > 0:
                    suma += int(datos[i])
                if datos[i] == "\n":
                    i +=1
                    f.write(datos[i])
                    f.write(str(suma))
                    i+=1
                    suma = 0

            i +=1
#             for i in datos:
#                 if i == "\n":
#                     print("ACA ESTOOOYYY")

# grabarRangoAlturas()
# grabarPromedios(deportes)
pruebaLeer()
