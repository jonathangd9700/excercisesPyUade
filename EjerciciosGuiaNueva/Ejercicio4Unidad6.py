ruta = "C:\\Users\\joniy\\Desktop\\UADE\\1AÑO\\SegundoCuatri\\Progra1\\Ejercicios\\EjerciciosGuiaNueva\\comentarios.txt"
def traerDatos(ruta):
    with open(ruta,"r") as f:
        datos = f.readlines()
        indice = 0
        while indice <= len(datos)-1:
            if datos[indice][0] == "#":
                datos.remove(datos[indice])
                indice -=1
            indice +=1
        return datos
def cargarDatos(datos,ruta):
    with open(ruta,"w") as f:
        for linea in datos:
            f.write(linea)
def main():
    try:
        datos = traerDatos(ruta)
        cargarDatos(datos,ruta)
    except FileNotFoundError as e:
        print("No se encontró el archivo o directorio: ", e)

main()

