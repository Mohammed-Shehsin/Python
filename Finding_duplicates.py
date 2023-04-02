               #finding the Duplicates
number=[1,3,3,3,2]
unique=[]
for i in number:
    if i not in unique:
        unique.append(i)
print(unique)
          Converting number to word
numbers={
    "1":"one",
    "2":"two",
    "3":"three",
    "4":"four",
    "5":"five",
    "6":"six",
    "7":"seven",
    "8":"eight",
    "9":"nine",
    "0":"zero"
}
phone=input ("Phone Number : ")
output=""
for num in phone:
    output+=numbers.get(num,"!")+" "
print(output)#
def greet_user (name):
    print(f' Hi {name}')
    print("Welcome !")
name=input("What is your name :")
greet_user(name)
def factorial(number):
    if number<=1:
        return 1
    return number*factorial(number-1)

number=int(input("Enter the the number : "))
print(f' Factorial of {number} is {factorial(number)}')
class Mammal:
    def talk(self):
        print("talk")

import random

class Dice :
    def roll (self):
        first=random.randint(1,6)
        second=random.randint(1,6)
        return first,second


dice=Dice()
print(dice.roll())

#                 PATHLIB
# import pathlib
# path=pathlib.Path()
# for file in path.glob('*.*'):
#     print(file)

#           PYPI and PIP
 

