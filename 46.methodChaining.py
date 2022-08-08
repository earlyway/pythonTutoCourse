# method chaining = calling multiple methods sequentially
# each call performs an action on the same object and returns self
# 여러 메소드들을 순차적으로 호출함.
# 각 호출은 같은 오브젝트에 대해 그 액션을 실행하고 자신을 반환한다.

class Car:
    def turn_on(self):
        print('You start the engine')
        return self
        
    def drive(self):
        print('You drive the car')
        return self
        
    def brake(self):
        print('You step on the brakes')
        return self
        
    def turn_off(self):
        print('You turn off the engine')
        return self
        
        
    
car = Car()
#car.turn_on().drive()
car.brake().turn_off()