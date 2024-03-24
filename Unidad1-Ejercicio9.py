"""Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando que la ocupación del camión no debe ser
inferior al 80%; en caso contrario el camión no serán despachado por su alto costo. """

#Camion transporta hasta 500kg
#1 cajon = 100 naranjas c/u entre 200 y 300g
#Si el peso es <200 o >300, se clasifica para jugo
#Si quedan naranjas sobrantes que no ingrese al cajon, se considera para el siguiente reparto.
#Generar numero entero entre 150 y 350g
#Ocupación del camión, no inferior al 80%
import random
cargaMaxCamion = 500000
cargaCamion = 0
cargaMaxCajon = 100
camiones = 0
cajones = 0
cantidadNaranjas = int(input("Ingrese la cantidad de naranjas"))
sumaNaranjas = 0
cantidadJugo = 0
naranjasSobras = 0
camionCargado = False
Pesototal = 0
i= 0
while i < cantidadNaranjas:
    naranjas = random.randint(150,350)
    Pesototal += naranjas
    cargaCamion += naranjas
    if camionCargado == False:
        if cargaCamion >=cargaMaxCamion*0.8:
            camiones +=1
            camionCargado = True
    if cargaCamion >=cargaMaxCamion:
        cargaCamion = 0
        camionCargado = False

    if(naranjas<200 or naranjas>300):
        cantidadJugo +=1
    else:
        sumaNaranjas +=1
    if(sumaNaranjas == cargaMaxCajon):
        cajones +=1
        sumaNaranjas = 0
    i+=1
naranjasSobras = cantidadNaranjas-cantidadJugo-(cajones*100)

print(f"Cajones = {cajones}")
print(f"Cantidad naranjas para jugo = {cantidadJugo}")
print(f"Sobraron {naranjasSobras} naranjas para el próximo transporte")
print(f"Se necesitan {camiones} camiones para transportar")
print(Pesototal)