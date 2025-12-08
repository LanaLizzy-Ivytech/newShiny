#get a random shiny hunt for gen 1
import numpy as np
target = 0
targetList = []
rng = np.random.default_rng()
checkEnd = 0

check = input("Do you want a target or list: T/L: ")
while check != "X":
    if check == "T":
        target = rng.integers(low=1, high=143)
        print(target)
        targetList.append(target)
    elif check == "L":
        print(targetList)
    else:
        print("Not a vaild input")
    check = input("Do you want a target or list: T/L or end with X: ")
print("Have a good day")