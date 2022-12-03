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

process.sort(key=lambda x: x.arrival, reverse=True)

print("Procesos Creados")
print(process)
print("\n")

while(time != time_position):
    cache = []
    cache = list(filter(lambda x: x.required > 0, process))
    cache = list(filter(lambda x: x.arrival <= time_position, cache))
    
    print(cache)
    
    for x in cache:
        x.required -= quantum

    time_position += quantum

print("\nProcesos Terminados")
print(process)