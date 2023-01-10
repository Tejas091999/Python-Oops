import time
print("Welcome to the notice board")
task1=input("What is your task1: ")
task2=input("What is your task2: ")
task3=input("What is your task3: ")
task4=input("What is your task4: ")
task5=input("What is your task5: ")
mytask=[]
mytask.append(task1)
mytask.append(task2)
mytask.append(task3)
mytask.append(task4)
mytask.append(task5)
print(mytask)
for items in mytask:
    print(items)
    if items==task1:
        user=input("Is this work done: ").lower()
        if user=="yes":
            mytask.remove(task1)
    if items==task2:
        user=input("Is this work done: ").lower()
        if user=="yes":
            mytask.remove(task2)
    if items==task3:
        user=input("Is this work done: ").lower()
        if user=="yes":
            mytask.remove(task3)
    if items==task4:
        user=input("Is this work done: ").lower()
        if user=="yes":
            mytask.remove(task4)
    if items==task5:
        user=input("Is this work done: ").lower()
        if user=="yes":
            mytask.remove(task5)
print("ALL THINGS DONE FOR TODAY")