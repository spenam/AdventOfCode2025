import numpy as np


f = np.genfromtxt("input_03.txt", dtype='|U100',delimiter=",").transpose()

## Part One

voltage = 0

for battery in f:
    battery = list(map(int,battery))
    max_number = sorted(battery)[-1]
    second_max_number = sorted(battery)[-2]
    index_max = battery.index(max_number)
    if index_max == len(battery)-1:
        index_max = battery.index(second_max_number)
    first = battery[index_max]
    second = max(battery[index_max+1:])
    jolt = int(str(first)+str(second))
    voltage += jolt

print("Solution Part One:")
print(voltage)
print("#"*30)


## Part Two

voltage = 0

for battery in f:
    battery = list(map(int,battery))
    jolt = 0
    for i in range(12):
        i=int(-1*(11-i))
        if i>-1:
            temp=battery[:]
        else:
            temp=battery[:i]
        nmax=max(temp)
        nindex=temp.index(nmax)
        battery=battery[nindex+1:]
        jolt=jolt*10+nmax
    voltage+=jolt

print("Solution Part Two:")
print(voltage)
