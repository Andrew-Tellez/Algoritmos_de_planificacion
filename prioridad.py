from utility_clases import Proceso
from random import shuffle, randint

lista_de_procesos:list[Proceso] = []

while True:
	cantidad_de_procesos=int(input("Ingrese la cantidad de procesos: "))
	if cantidad_de_procesos > 0:
		break
	else:
		print("Ingrese valores mayores a 0")


llegada = list(range(cantidad_de_procesos))
shuffle(llegada)

for i in range(cantidad_de_procesos):
	lista_de_procesos.append(Proceso(f"P{i + 1}", randint(1, cantidad_de_procesos), llegada[i], randint(1,20)))

lista_de_procesos.sort(reverse=True ,key=lambda proceso: proceso.prioridad)

#algoritmo de proioridad
for i in lista_de_procesos:
  print(f"Proceso: {i.name} Requiere:{i.requerido} llegada:{i.llegada} Prioridad: {i.prioridad}")

tiempo=0
procesos_en_cola:list[Proceso]=[]
proceso_prioritario:list[Proceso]=[]
for i in lista_de_procesos:
	if i.llegada == 0:
		print(f"\nProceso {i.name} de la llegada {i.llegada} y prioridad {i.prioridad} terminado\n")
		tiempo += i.requerido
		lista_de_procesos.remove(i)

while (len(lista_de_procesos)>0):
	procesos_en_cola=list(filter(lambda p: p.llegada <= tiempo , lista_de_procesos))
	if len(procesos_en_cola) > 1:
		max_prioridad = max([p.prioridad for p in procesos_en_cola])
		proceso_prioritario = list(filter( lambda p: p.prioridad == max_prioridad, procesos_en_cola))
		print(procesos_en_cola)
		print(f"\nProceso {proceso_prioritario[0].name} de la llegada {proceso_prioritario[0].llegada} y prioridad {proceso_prioritario[0].prioridad} terminado\n")
		tiempo += proceso_prioritario[0].requerido
		lista_de_procesos.remove(proceso_prioritario[0])
	else:
		print(procesos_en_cola)
		print(f"\nProceso {procesos_en_cola[0].name} de la llegada {procesos_en_cola[0].llegada} y prioridad {procesos_en_cola[0].prioridad} terminado\n")
		tiempo += procesos_en_cola[0].requerido
		lista_de_procesos.remove(procesos_en_cola[0])