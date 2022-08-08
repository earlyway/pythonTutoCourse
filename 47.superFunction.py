# super() = Function used to give access to the methods of a parent class.
# Returns a temporary object of a parent class when used

# 부모클래스의 메소드에 접근할 수 있게 권한을 주는데 사용되는 함수이다.
# 사용될때 부모클래스의 임시 오브젝트를 반환한다.

class Rectangle:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width

class Square(Rectangle):
    
    def __init__(self, length, width):
        super().__init__(length, width)
        
    def area(self):
        return self.length * self.width
        
class Cube(Rectangle):
    
    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height
        
    def volume(self):
        return self.length * self.width * self.height
        
square = Square(3,3)
cube = Cube(3,3,2)

print(square.area())
print(cube.volume())