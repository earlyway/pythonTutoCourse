# Object Oriented Programming

from pyexpat import model
from turtle import color
from car import Car

car_1 = Car('Chevy',"Corvette",2021,'blue')
car_2 = Car('Ford', "mustang", 2022,'red')

print(car_2.make)
print(car_2.model)
print(car_2.year)
print(car_2.color)

car_1.drive()
car_2.stop()