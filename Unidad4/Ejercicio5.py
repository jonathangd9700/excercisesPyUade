cadena = "¡Únete a nosotros para una noche llena de música, diversión y sorpresas! ¡No te lo pierdas!"

lista = cadena.split()
print(lista)
N = 7

for i in range(len(lista)):
    if len(lista[i]) >= N:
        print(lista[i],end=" ")
  