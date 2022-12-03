from utility_clases import Proceso
from pandas import DataFrame
from random  import randint, shuffle

lista_de_procesos:list[Proceso] = []
cantidad_de_procesos:int = 0
q_asignado:int = 0
# tabla_de_resultados:DataFrame = DataFrame(columns=["Proceso","Tiempo requerido" ,"Tiempo asignado", "Ciclos"])

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

lista_de_procesos.sort(reverse=True, key=lambda Proceso:Proceso.llegada)
procesos_terminados:list[Proceso] = []

def check_zero(i):
    if i.requerido != 0:
          return True  

    return False

def round_robin(lista: list[Proceso], quantum: int, tiempo: int, index: int) -> None:
	while(tiempo != 0):
		print(lista)
		for i in lista:
			i.requerido -= quantum
			if(i.requerido < 1):
				i.requerido = 0
				procesos_terminados.append(i)

		lista = list(filter(lambda i:i.requerido != 0, lista))
		random = randint(0, 1)
		
		if(random == 1):
			lista.insert(0, Proceso(f"P{index + 1}", randint(1, 10), index))
			index += 1

		tiempo -= quantum
		

			
round_robin(lista_de_procesos, 2, 20, cantidad_de_procesos)
print("Nodos terminados")
print(procesos_terminados)