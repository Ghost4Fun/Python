import time

print("Find the Answer to Life, the Universe, and Everything\n")


def NumberOfLife(number): 
  if number >= 100 or number < 1:
    print("Acceptable range of numbers (1-99)")
    time.sleep(1.0)
    return NumberOfLife(int(input("Please provide a number for the answer: ")))
  else:
    while number != 42:
      print(number)
      print("Wrong number, try again")
      time.sleep(1.0)
      return NumberOfLife(int(input("Please provide a number for the answer: ")))
  return number

  
print(NumberOfLife(int(input("Please provide a number for the answer: "))))
print("You did it!")
time.sleep(2.0)

exit()