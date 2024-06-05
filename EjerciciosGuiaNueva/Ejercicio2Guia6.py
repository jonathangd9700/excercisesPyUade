import random
ruta = "C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\EjerciciosGuiaNueva\\lluvias.txt"

def cargarArchivo(cantidad):
    i = 0
    while i < cantidad:
        mes = random.randint(1,12)
        if mes == 2:
            dia = random.randint(1,28)
        elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
            dia = random.randint(1,31)
        else:
            dia = random.randint(1,30)
        lluvia = random.randint(150,2500)
        print(f"Cargo- Dia: {dia} ; Mes: {mes} ; Lluvia: {lluvia}")
        with open("C:\\Users\\HP\\Desktop\\UADE\\Progra1\\excersicesPyUade\\EjerciciosGuiaNueva\\lluvias.txt","a") as f:
            datos = f.write(str(dia)+";"+str(mes)+";"+str(lluvia) + "\n")
        i+=1

def imprimirTotalLluvia():
    with open (ruta, "r") as f:
        datos = f.readlines()
        suma = 0
        for i in datos:
            i = i.split(";")
            i = i[2].split("\n")
            suma += int(i[0])
            print(i)
        print(suma)
        return suma
            

def main():
    while True:
        try:
            resultado = imprimirTotalLluvia()
#             cantidad = int(input("Ingrese cuantos datos desea generar: "))
#             cargarArchivo(cantidad)
            print(f"El total de las lluvias es: {resultado}")
            
            break;
        except ValueError as e:
            print("Valor incorrecto")
    
main()