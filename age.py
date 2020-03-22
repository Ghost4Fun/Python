import time
import datetime

print("When you will be 100 years old?")

def calculation():
    name = input("What is your name?: ")
    time.sleep(1.0)
    age = int(input("How old are you?: "))
    time.sleep(1.0)
    number = int(input("How much of the copies?: "))
    if number <= 0:
        print("Number must be greater than 0")
        time.sleep(1.0)
        return calculation()

    time.sleep(1.0)    

    date = datetime.datetime.now()
    calc = date.year + 100 - age

    result = name + " at " + str(calc) + " you will be 100 years old.\n"
    
    print(result * number)
    time.sleep(2.0)
    exit()

calculation()


