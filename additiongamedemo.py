#Ryan Jones
#1/22/18
#additiongamedemo.py - how to use random numbers

from random import randint

num1 = randint(-10,10)
num2 = randint(-10,10)
print(num1, '+', num2)
ans = int(input('= '))
print(ans == num1 + num2)