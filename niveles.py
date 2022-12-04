from utility_clases import Proceso
from random import randint

memoria_principal:list[Proceso] = []
disco_duro:list[Proceso] = []
quantum=2
while True:
	cantidad_de_procesos=int(input("Ingrese la cantidad de procesos: "))
	if cantidad_de_procesos > 0:
		break
	else:
		print("Ingrese valores mayores a 0")

for i in range(cantidad_de_procesos):
  if i % 2 ==0:
    disco_duro.append(Proceso(name=f"P{i + 1}", requerido=randint(1, cantidad_de_procesos), llegada=randint(1,20)))
  else:
    memoria_principal.append(Proceso(name=f"P{i + 1}", requerido=randint(1, cantidad_de_procesos), llegada=randint(1,20)))

memoria_principal.sort(key=lambda proceso: proceso.requerido)
disco_duro.sort(key=lambda proceso: proceso.requerido)


print("Memoria principal")
for i in memoria_principal:
  print(f"Proceso: {i.name} Requiere:{i.requerido}")

print("\nDisco duro")
for i in disco_duro:
  print(f"Proceso: {i.name} Requiere:{i.requerido}")

while(len(memoria_principal)>0):
  for i in memoria_principal:
    i.requerido -= quantum
    if i.requerido <= 0:
      print(f"\nProceso {i.name} terminado\n")
      memoria_principal.remove(i)
      if len(disco_duro)==0 and len(memoria_principal) == 1:
        continue
      elif len(disco_duro)==0 and len(memoria_principal) == 0:
        break
      memoria_principal.append(disco_duro[0])
      disco_duro.remove(disco_duro[0])

    else:
      if len(disco_duro) == 0:
        disco_duro.append(i)
        memoria_principal.remove(i)
      else:
        disco_duro.append(i)
        memoria_principal.remove(i)
        memoria_principal.append(disco_duro[0])
        disco_duro.remove(disco_duro[0])
    

