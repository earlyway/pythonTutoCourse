# Prevents a user from creating an object of that class
# + compels a user to override abstract methods in a child class

#abstract class =  a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but doesn't have an implementation.

# 유저를 막는다. 그 클래스의 오브젝트를 생성하는
# 자식 클래스에서 추상 메소드를 오버라이드(재정의)하도록 유저를 강요하게 한다.

# 추상 클래스 = 하나 또는 여러 추상 메소드를 포함한 클래스
# 추상 메소드 = 선언이 있지만 실행(구현)이 없는 메소드.

from abc import ABC, abstractmethod

class Vehicle(ABC) :
    
    @abstractmethod
    def go(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    
    def go(self):
        print('You drive the car')
        
    def stop(self):
        print('This car is stopped')
        
class Motorcycle(Vehicle):
    
    def go(self):
        print('You drive the motorcycle')
        
    def stop(self):
        print('This motorcycle is stopped')
        
#vehicle = Vehicle()
car = Car()
motorcycle=Motorcycle()

#vehicle.go()      ## Vehicle 클래스의 go함수가 pass.
car.go()
motorcycle.go()


car.stop()