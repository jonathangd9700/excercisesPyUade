def calculoVuelto(total,montoRecibido):
    billeteCincoMil = 5000
    billeteMil = 1000
    billeteQuinientos = 500
    billeteDoscientos = 200
    billeteCien = 100
    billeteCincuenta = 50
    billeteVeinte = 20
    billeteDiez = 10
    print("El total de su compra es $",end="")
    print(total)
    print("Usted pagò con $",end="")
    print(montoRecibido)
    print("Su vuelto es $",end="")
    vuelto = montoRecibido - total
    print(vuelto)
    cambioCincoMil = vuelto%5000 
    return vuelto
montoRecibido = -1
print("Ingrese el total de la compra",end="")
total = int(input())
print("Ingrese el monto con el que se realizò el pago",end="")
montoRecibido = int(input())
while(montoRecibido < total):
    print("No puede pagar con un valor menor al total de la compra")
    print("Ingrese el monto con el que se realizò el pago",end="")
    montoRecibido = int(input())


calculo = calculoVuelto(total,montoRecibido)
print(calculo)