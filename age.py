import sys
from time import sleep
import datetime

print("When you will be 100 years old?\n")

def calculation(name, age, number):
    if number <= 0:
        print("Number must be greater than 0")
        sleep(1.0)  
        return calculation(name, age, number=int(input("How much of the copies do you want to print?: ")))
        
    date = datetime.datetime.now()
    calc = date.year + 100 - age

    result = name + " at " + str(calc) + " you will be 100 years old.\n\n"
    
    return result * number



print(calculation(input("What is your name?: "), int(input("How old are you?: ")), int(input("How much of the copies do you want to print?: "))))
sleep(2.0)

sys.exit()