from utility_clases import Proceso
from pandas import DataFrame

lista_de_procesos:list[Proceso] = []
cantidad_de_procesos:int = 0
q_asignado:int = 0
tabla_de_resultados:DataFrame = DataFrame(columns=["Proceso","Tiempo requerido" ,"Tiempo asignado", "Ciclos"])

while True:
	cantidad_de_procesos=int(input("Ingrese la cantidad de procesos: "))
	q_asignado=int(input("Ingrese el quantum asignado a todos los procesos: "))
	
	if cantidad_de_procesos > 0 and q_asignado > 0:
		break
	else:
		print("Ingrese valores mayores a 0")


for i in range(cantidad_de_procesos):
	q_requerido=int(input(f"Ingrese el quantum requerido para el proceso {i+1}: "))
	t_llegada=int(input(f"Ingrese el tiempo de llegada para el proceso {i+1}: "))

	lista_de_procesos.append(Proceso(f"Proceso {i+1}", q_requerido, q_asignado, t_llegada))

lista_de_procesos.sort(key=lambda proceso: proceso.llegada)


print(lista_de_procesos)

procesos_terminados:list[Proceso] = []

def round_robin(procesos:list[Proceso], quantum:int) -> None:
	# tiempo = 1
	# while len(procesos) > 0:
	# 	for i in procesos:
	# 		if i.requerido > quantum:
	# 			i.requerido -= quantum
	# 			i.ciclos += 1
	# 		else:
	# 			i.requerido = 0
	# 			procesos_terminados.append(i)
	# 			procesos.remove(i)

























	# while len(procesos) > 0:
	# 			for proceso in procesos:
	# 					if proceso.requerido > quantum:
	# 							proceso.requerido -= quantum
								
	# 							if proceso.requerido <= 0:
	# 								tabla_de_resultados.loc[len(tabla_de_resultados)] = [proceso.name, proceso.aux_requerido, proceso.asignado, proceso.ciclos]
	# 								procesos.remove(proceso)
	# 							else: 
	# 							# proceso.requerido > 0:
	# 								proceso.ciclos += 1 

	# 					else:
	# 							print(f"Proceso {proceso.name} terminado")
	# 							tabla_de_resultados.loc[len(tabla_de_resultados)] = [proceso.name, proceso.aux_requerido, proceso.asignado, proceso.ciclos]
	# 							procesos.remove(proceso)
# round_robin(lista_de_procesos, q_asignado)

# print(tabla_de_resultados)
