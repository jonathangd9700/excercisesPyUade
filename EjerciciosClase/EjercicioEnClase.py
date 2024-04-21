#Codifica un programa que nos permita guardar los nombres de los alumnos de una clase y la nota final que han obtenido.
#El programa pedirá el número de alumnos que vamos a introducir. Al final el programa nos mostrará la lista de alumnos,
#la nota obtenida por cada uno de ellos y una leyenda si aprobó o no. Se aprueba con una nota mayor e igual a 4.
 
#Ej:
#Juan Pérez obtuvo un 4 -> Aprobó
#Raúl González obtuvo un 9 -> Aprobó
#Ana Sanchez obtuvo un 2 -> Desaprobó
 
#Nota: Guarda la información en un diccionario cuyas claves serán los nombres de los alumnos y los valores las notas finales.
#Validar nota (1 al 10). Utilizar tres funciones, la primera para el programa principal, la segunda para la carga del diccionario,
#y la tercera para la impresión de las notas.

def cargarDiccionario(cantidadCargar):
    datosNotasAlumnos = []
    for i in range(cantidadCargar):
        alumno = {}
        nombre = input("Ingrese el nombre del alumno")
        alumno["Nombre"] = nombre
        nota = int(input("Ingrese la nota del alumno entre 1 y 10"))
        while nota < 1 or nota > 10:
            nota = int(input("Ingrese una nota válida entre 1 y 10"))
        alumno["Nota"] = nota
        datosNotasAlumnos.append(alumno)
    return datosNotasAlumnos
    
def aprobadoDesaprobado(lista):
    for alumno in lista:
        nombre = alumno.get("Nombre")
        nota = alumno.get("Nota")
        if nota >= 1 and nota < 4:
            print(f"El alumno/a {nombre}  desaprobó con {nota}")
        if nota >= 4 and nota <= 10:
            print(f"El alumno/a {nombre}  aprobó con {nota}")
            
def main():
    cantidad = int(input("Ingrese la cantidad de alumnos a cargar. Debe ser mayor a cero"))
    while cantidad <= 0:
        cantidad = int(input("Ingrese la cantidad de alumnos a cargar. Debe ser mayor a cero"))
    datosAlumnos = cargarDiccionario(cantidad)
    aprobadoDesaprobado(datosAlumnos)


    
main()
    