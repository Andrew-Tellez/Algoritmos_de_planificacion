from utility_clases import Proceso
from random import shuffle, randint

lista_de_procesos:list[Proceso] = []

while True:
	cantidad_de_procesos=int(input("Ingrese la cantidad de procesos: "))
	q_asignado=int(input("Ingrese el quantum asignado a todos los procesos: "))
	
	if cantidad_de_procesos > 0 and q_asignado > 0:
		break
	else:
		print("Ingrese valores mayores a 0")

llegada = list(range(cantidad_de_procesos))
shuffle(llegada)

for i in range(cantidad_de_procesos):
	lista_de_procesos.append(Proceso(f"P{i + 1}", randint(1, 10), llegada[i] + 1))

lista_de_procesos.sort(key=lambda proceso:proceso.requerido)

suma=0
for i in lista_de_procesos:
  suma+=i.requerido

print(f"{lista_de_procesos}\n")

print(f"suma total: {suma}\n")
print(f"Tiempo promedio: {suma/cantidad_de_procesos}\n")


