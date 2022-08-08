# multi-level inheritance = when a child class is derived from more than one parent class
#중첩 상속 = 자식 클래스는 하나 이상의 부모 클래스에서 파생되었다.
class Prey :
    def flee(self):
        print('This animal flees')
        
class Predator :
    def hunt(self):
        print('This animal is hunting')
        
class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey, Predator):
    pass

rabbit = Rabbit()
hawk = Hawk()
fish = Fish()

#rabbit.flee()
hawk.hunt()
fish.flee()
fish.hunt()