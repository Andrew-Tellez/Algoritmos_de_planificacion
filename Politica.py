from random import randint
from classes.Process2 import Process2

time = 20
need = 3
time_position = 0
process = []
quantum = 1

# Nombre del proceso, Tiempo de quantums que necesita, Tiempo de llegada del proceso
"""
for i in range(need):
    process.append(Process2(f"P{i + 1}", randint(1, 3), randint(1, 3), False))
"""
process.append(Process2(f"P3", 2, 7))
process.append(Process2(f"P1", 1, 4))
process.append(Process2(f"P2", 2, 5))

process.sort(key=lambda x: (x.deadline))
process[0].start = True
process[0].available = False
process[0].print = '1'

def lowNumber(values: list, time: int) -> int:
    number = 0
    value = 10000000
    for x in range(len(values)):
        if(values[x].start):
            continue

        if(not values[x].available):
            continue
        
        res = (values[x].deadline * values[x].cicle) - time
        #print(f"number {x}, res {res}")
        if(value > res):
            value = res
            number = x


    #print(f"result {number}")
    return number  

index = 0

while(time > time_position):
    x = process[index]
    
    for y in process:
        if(time_position == 0):
            break
        
        if((time_position + 1) % (y.deadline) == 0):
            y.available = True
    
    print(f"Tiempo: { time_position + 1 } {process}")

    if(x.start):
        x.check += 1

    if(x.required == x.check):
        index = lowNumber(process, time_position)
        x.cicle += 1
        process[index].start = True
        process[index].available = False
        process[index].print = '1'
        x.start = False
        x.available = False
        x.print = '0'
        x.check = 0

    time_position += quantum
          