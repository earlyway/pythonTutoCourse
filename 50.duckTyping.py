# Duck typing = concept where the class of an object is less important than the methods / attributes.
# class type is not checked if minimum methods / attributes are present.
# "If it walks like a duck, and it quacks like a duck, then it must be a duck."
#   메소드, 속성들보다 오브젝트의 클래스가 덜 중요하다는 개념입니다.
# 만약 최소한의 메소드, 속성이 있다면 클래스 타입을 체크하지않는다.
# "만약 오리처럼 걷고 오리처럼 꽥꽥거린다면 그것은 오리일 것이다."


class Duck :
    def walk(self):
        print('This duck is walking')
        
    def talk(self):
        print('This duck is quacking')
        
class Chicken:
    def walk(self):
        print('This chicken is walking')
        
    def talk(self):
        print('This chicken is clucking')
        
        
class Person():
    def catch(self, duck):
        duck.walk()
        duck.talk()
        print('You caught the critter!')
        
duck = Duck()
chicken = Chicken()
person = Person()

person.catch(chicken)