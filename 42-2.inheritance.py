# inherit 상속받다. 물려받다
# https://youtu.be/XKHEtdqhLK8?list=RDCMUC4SVo0Ue36XCfOyb5Lh1viQ&t=13972
class Animal :
    alive = True
    def eat(self):
        print('This animal is eating')
        
    def slumber(self):
        print('This animal is sleeping')
        
class Rabbit(Animal):
    def run(self):
        print('This rabbit is running')
    
class Fish(Animal):
    def swim(self):
        print('This fish is swimming')
class Hawk(Animal):
    def fly(self):
        print('This hawk is flying')

rabbit = Rabbit()
fish = Fish()
hawk = Hawk()

#print(rabbit.alive) # Animal 클래스
# fish.eat() # 

rabbit.run()
hawk.fly()
