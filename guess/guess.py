#random number guess code in python 

import random
from random import randint

random_number = randint(0,100)

x = -1

while x != random_number:
    if x != -1:
        print("wrong number try again \n")
    
    x=input("Enter the number : ")
    x= int(x)

if x== random_number:
    print("You guessed correctly")
