import json
from pilas import *


def extraerJson():
    pila = crearPila()
    with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\simulacroDos\\personas.json","r", encoding= "utf-8") as f:
        personas = f.read()
        personaTexto = json.loads(personas)
        for persona in personaTexto:
            apilar(pila,persona)
        return pila

# def actualizarJson(pila):
#     with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\simulacroDos\\personas.json","w", encoding= "utf-8") as f:
#         datos = json.dumps(pila)
#         f.write(datos)                
def menu():
    print("Ingrese 1 para agregar una nueva tarea")
    print("Ingrese 2 para completar una tarea")
    print("Ingrese 3 para completar una tarea")
    print("Ingrese 4 finalizar")
    opcionElegida = int(input("Ingrese la opción aquí: "))
    while opcionElegida != 1 and opcionElegida != 2 and opcionElegida != 3 and opcionElegida != 4:
        opcionElegida = int(input("Ingrese una opción válida: "))
    return opcionElegida

def opcionUno(pila):
    try:
        persona = { }
        persona["id"] =  input("Ingrese el id")
        persona["descripcion"] = input("Ingrese la descripcion")
        persona["prioridad"] = input("Ingrese la prioridad")
        apilar(pila,persona)
        return pila
    except ValueError as e:
        raise ValueError(e)
        
#     actualizarJson(pila)


def opcionDos(pila):
    if esVacia(pila) != True:
        desapilar(pila)
    else:
        print("La pila está vacia")
    return pila

def main():
    while True:
        try:
            pilaCargada = extraerJson()
            print(pilaCargada)
            opcion = menu()
            print(opcion)
            while opcion != 4:
                if opcion == 1:
                    resultado = opcionUno(pilaCargada)
                    print(resultado)
                elif opcion == 2:
                    resultado = opcionDos(pilaCargada)
                    print(resultado)
                elif opcion == 3:
                    pilaAux = crearPila()
                   
            else:
                print("Finalizó el programa")
                break;
        except ValueError as e:
            print("Valor incorrecto")
#             opcion = menu()
main()
