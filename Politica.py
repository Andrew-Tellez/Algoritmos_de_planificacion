from random import randint
from classes import Process2

time = 20
need = 3
time_position = 0
process = []
quantum = 1

# Nombre del proceso, Tiempo de quantums que necesita, Tiempo de llegada del proceso
for i in range(need):
    process.append(Process2(f"P{i + 1}", randint(1, 3), randint(1, 3), False))

process.sort(key=lambda x: x.deadline)

print("Procesos Creados")
print(f"Tiempo: {time_position} {process}")
print("\n")

"""
Dudas
- Que pasa si los procesos tiene la misma cantidad de requerido de quantum?
- 
"""
finish_process = []
cache = []

while(time != time_position):
    cache = list(filter(lambda x: not x.finish, process))
    cache[0].task += 1
    cache[0].check()

    for x in cache:
        if(time_position % x.deadline == 0):
            x.task = 0
            x.finish = False
    
    
    time_position += quantum


print("\nProcesos Terminados")
print(f"Tiempo: {time_position} {finish_process}")