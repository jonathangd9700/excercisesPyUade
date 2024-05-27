def cargarArchivo():
    with open (r"C:\Users\HP\Desktop\UADE\Progra1\excersicesPyUade\Unidad6\texto.txt", "w") as f:
        i = 0
        while i < 4:
            nombre = input("Ingrese el nombre")
            apellido = input("Ingrese el apellido")
            registro = apellido + ";" + nombre+ "\n"
            f.write(registro)
            i += 1

def filtrarApellidos():
    with open(r"C:\Users\HP\Desktop\UADE\Progra1\excersicesPyUade\Unidad6\texto.txt", "r") as f:
        datos = f.readlines()
        
    with open(r"C:\Users\HP\Desktop\UADE\Progra1\excersicesPyUade\Unidad6\texto.txt", "w") as f:
        for linea in datos:
            

def main():
    cargar = False
    preguntar = int(input("Desea cargar el archivo? 1 - Si / 2 - No"))
    if preguntar == 1:
        cargarArchivo()
    
    
main()
# def cargarArchivo():
#     identificador = int(input("Ingrese el ID"))
#     nombre = input("Ingrese el nombre")
#     edad = int(input("Ingrese la edad"))
#     return identificador, nombre, edad
# 
# with open(r"C:\Users\HP\Desktop\UADE\Progra1\excersicesPyUade\Unidad6\texto.txt", "a") as f:
#     identificador, nombre, edad = cargarArchivo()
#     linea = str(identificador) + ";" + nombre +";"+ str(edad) + "\n" 
#     print(linea)
#     f.write(linea)
# 
# id = int(input("Ingrese id"))
# nombreUsu = input("Ingrese el nombre a cambiar")
# 
# with open(r"C:\Users\HP\Desktop\UADE\Progra1\excersicesPyUade\Unidad6\texto.txt", "r") as f:
#     datos = f.readlines()
# 
# with open(r"C:\Users\HP\Desktop\UADE\Progra1\excersicesPyUade\Unidad6\texto.txt", "w") as f:
#     for linea in datos:
#         identificador, nombre, edad = linea.strip().split(";")
#         if identificador == str(id):
#             registro = str(identificador) + ";" + nombreUsu+ ";" + str(edad) + "\n"
#             f.write(registro)
#         else:
#             f.write(linea)