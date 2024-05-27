import json

with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\EjerciciosClase\\clase6-5.json","r",encoding="utf-8") as f:
    personaTxt = f.read()
    
personas = json.loads(personaTxt)

print(personas)

# for persona in personas:
#     if persona["id"] == 1:
#         print(f'Nombre: {persona["nombre"]}')
#     elif  "ruso" in persona["idioma"]:
#         print(f'Nombre: {persona["nombre"]} - Apellido: {persona["apellido"]}')
#AGREGAR USUARIO AL ARCHIVO
# usuId = input("Ingrese un id: ")
# usuNombre = input("Ingrese un nombre: ")
# usuApellido = input("Ingrese un apellido: ")
# usuEdad = input("Ingrese la edad: ")
# usuIdioma = ["Español","Ingles"]

# personas.append({"id":usuId, "Nombre":usuNombre,"Apellido": usuApellido,"Edad":usuEdad,"Idiomas":usuIdioma})
# 
# personas_Txt = json.dumps(personas, ensure_ascii = False, indent=4)
# 
# with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\EjerciciosClase\\clase6-5.json","w",encoding="utf-8") as f:
#     f.write(personas_Txt)
    
#Modificar JSON
usuId = input("Ingrese un id: ")
usuEdad = input("Ingrese la edad: ")
 for persona in personas:
     
with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\EjerciciosClase\\clase6-5.json","w",encoding="utf-8") as f:
    