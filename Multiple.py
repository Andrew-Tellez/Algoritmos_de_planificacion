from utility_clases import Proceso
from random import randint

need = 6

process = []
process_finish = []

quantum = [2, 3, 5, 7]

for i in range(need):
    process.append(Proceso(f"P{i + 1}", randint(1, 20), randint(1, 6), 0))

process.sort(key=lambda x: x.llegada)
index = 0

while(need != len(process_finish)):
    print(process)
    for x in process:
        x.requerido -= quantum[index]
        if(x.requerido < quantum[index]):
            x.requerido = 0

    process_finish += list(filter(lambda x: x.requerido < 1, process))
    process = list(filter(lambda x: x.requerido >= 1, process))

    
    if(len(quantum) - 1 > index):
        index += 1

    for x in process:
        x.prioridad = index
        


print(process_finish)
