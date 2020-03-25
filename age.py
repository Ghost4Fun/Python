import time
import datetime

print("When you will be 100 years old?")

def calculation(name, age, number):
    if number <= 0:
        print("Number must be greater than 0")
        return calculation(name, age, number = int(input("How much of the copies?: ")))
    time.sleep(1.0)    

    date = datetime.datetime.now()
    calc = date.year + 100 - age

    result = name + " at " + str(calc) + " you will be 100 years old.\n"
    
    return result * number


calculation(input("What is your name?: "), int(input("How old are you?: ")), int(input("How much of the copies?: ")))

print(calculation)
time.sleep(2.0)

exit()