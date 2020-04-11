import time

print("Odd Or Even?\n")
time.sleep(1.0)

number = int(input("Please provide a number to check: "))
time.sleep(1.0)


def calc():
    if number != 0:
        return number % 2         
    else:
        print("The number can't be 0!")
        time.sleep(2.0)
        

if calc() == 0:
    if (number % 4) == 0:
        print("It's a multipler of 4\n")
        time.sleep(2.0)
    else:
        print("It's an Even\n")
        time.sleep(2.0)
else:
    print("It's an Odd\n")
    time.sleep(2.0)


print("Program - part 2\n")
num = int(input("Please provide a number to check: "))
check = int(input("\nPlease provide a number to check by: "))


if (num % check) == 0:
    print(num, "divides evenly by", check)
else:
    print(num, "does not divide evenly by", check)

