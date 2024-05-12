def ingresarMes(lista):
    mes = int(input("Ingrese un valor entre 1 y 12 para saber el mes"))
    if mes >= 1 and mes <=12:
        return mes
    else:
        raise ValueError("El valor ingresado no es un número")
        raise IndexError("El valor ingresado no está dentro de los valores correctos")

def main():
    while True:
        try:
            meses = ["Enero", "Febrero", "Marzo","Abril", "Mayo", "Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
            resultado = ingresarMes(meses)
            if resultado >0 and resultado <len(meses):
                print(f"El mes elegido es {meses[resultado-1]}")
                break;            
        except ValueError as e:
            print("Error: ",e)
        except IndexError as e:
            print("Error: ",e)

main()

