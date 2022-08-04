# inherit 상속받다. 물려받다
# https://youtu.be/XKHEtdqhLK8?list=RDCMUC4SVo0Ue36XCfOyb5Lh1viQ&t=13972
class Animal :
    alive = True
    def eat(self):
        print('This animal is eating') 
    def sleeping(self):
        print('This animal is sleeping')
        
class Rabbit(Animal):
    pass
class Fish(Animal):
    pass
class Hawk(Animal):
    pass

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

print(rabbit.alive) # True가 출력됨. 왜냐하면 Rabbit 함수의 Animal클래스의 alive변수를 상속받았기때문.
fish.eat() # This animal is eating이 출력됨. 왜냐하면 Fish클래스의 Animal클래스의 eat함수의 print를 받기때문.

