import math

def raizCuadrada(numero):
        if numero < 0:
            raise ValueError("Numero negativo")
        return math.sqrt(numero)
        
    

def main():
    while True:
        try:
            numero = float(input("Ingrese un número para sacar su raíz cuadrada"))
            resultado = raizCuadrada(numero)
            if resultado is not None:
                print(f"La raíz cuadrada es: {resultado}")
                break;
        except ValueError as e:
            print(f"Error: {e}")

main()



