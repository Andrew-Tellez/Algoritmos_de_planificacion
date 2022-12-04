from random import randint
from classes.Process import Process

def condition(x):
    if(x.required < 1):
        return False

time = 20
need = 6
time_position = 0
process = []
quantum = 1

# Nombre del proceso, Tiempo de quantums que necesita, Tiempo de llegada del proceso
for i in range(need):
    process.append(Process(f"P{i + 1}", randint(1, 6), randint(0, time)))

process.sort(key=lambda x: x.arrival)

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
    
    cache = list(filter(lambda x: x.required > 0, process))
    cache = list(filter(lambda x: x.arrival <= time_position, cache))
    cache.sort(key=lambda x: (x.required, x.arrival))

    print(f"Tiempo: {time_position} {cache}")

    if(len(cache) != 0):
        cache[0].required -= 1

    for i in cache:
        if(i.required == 0):
            finish_process.append(i)
    time_position += quantum


print("\nProcesos Terminados")
print(f"Tiempo: {time_position} {finish_process}")