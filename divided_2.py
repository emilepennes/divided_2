# coding:utf-8
"""The exercice is to define how many times a number can be divided by two"""

X = 0
Y = 0
print("The exercice is to define how many times a number can be divided by two")
while True:
    try:
        X = int(input("Let's have X = "))
        break
    except ValueError:
        print("X must be an integer ;) Try again...")

while X % 2 == 0:
    X = X/2
    Y += 1
print("X is " + str(Y) + " times divided by two.")
