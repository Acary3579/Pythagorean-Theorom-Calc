# IMPORTS

import os
import math

# SELECTION

print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("~~~ PYTHAGOREAN THEOROM CALCULATOR ~~~")
print ("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print ("OPTIONS:")
print ("1 - SOLVE FOR HYPOTENUSE")
print ("2 - SOLVE FOR LEG")

user_choice = input("ENTER YOUR CHOICE: ")

# HYPOTENUSE MATHEMATICS

if user_choice == "1":
    firstnh = int(input("ENTER YOUR FIRST LEG'S DIMENSION: "))
    secondnh = int(input("ENTER YOUR SECOND LEG'S DIMENSION: "))

    secondsteph = (firstnh ** 2 + secondnh **2)

    hanswer = math.sqrt(secondsteph)

    print (hanswer , "IS YOUR ANSWER")

    input()
    os.system('cls')

# LEG 1 MATHEMATICS

elif user_choice == "2":
    firstnl = int(input("ENTER YOUR LEG: "))
    secondnl = int(input("ENTER YOUR HYPOTENUSE: "))

    secondstepl = (secondnl ** 2 - firstnl ** 2)

    lanswer = math.sqrt(secondstepl)

    print (lanswer, "IS YOUR ANSWER")

    input()
    os.system('cls')
