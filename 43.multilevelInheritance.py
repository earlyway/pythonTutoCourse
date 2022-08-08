# multi-level inheritance = when a derived (child) class inherits another derived (child) class
# 파생 (하위)클래스가 다른 파생(하위) 클래스를 상속하는 경우

class Organism :
    alive = True
    
    
class Animal(Organism):
    def eat(self):
        print('This animal is eating')
        
class Dog(Animal):
    def bark(self):
        print('This dog is barking')
        
dog = Dog()     
print(dog.alive)    
dog.eat()     # Animal class을 가져오지않아도 def eat를 받네? 뭐지 
dog.bark()