import time

print("Find the Answer to Life, the Universe, and Everything")


def NumberOfLife():
  number = int(input("Please provide a number for the answer: "))
  if number >= 100 or number < 1:
    print("Acceptable range of numbers (1-99)")
    time.sleep(1.0)
    return NumberOfLife()
  else:
    while number != 42:
      print(number)
      print("Wrong number, try again")
      time.sleep(1.0)
      return NumberOfLife()
  print(number)
  print("You did it!")
  time.sleep(1.0)
  exit()


NumberOfLife()
