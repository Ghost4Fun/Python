import datetime

date =  datetime.datetime.now()

name =input("Jak sie nazywasz?: ")
age = int(input("Ile masz lat?: "))

year = int(100 - age)
year2 = str(date.year + year)

print(name + " w roku " + year2 + " bedziesz w wieku 100 lat")
