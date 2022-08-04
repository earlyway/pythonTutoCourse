# **kwargs = parameter that will pack all arguments into a dictionary
# useful so that a function can accept a varying amount of keyword argument.
# 모든 인수를 dictionary에 대입하는 매개변수이다.
# 많은 키워드 인수를 함수에 쓸수있기에 유용하다.

def hello(**kwargs):
    #print('hello ' + kwargs['first'] + ' ' + kwargs['last'])
    print('Hello',end=' ')
    for key,value in kwargs.items():
        print(value, end = ' ')
    
hello(title = 'Mr.', first="Bro",middle="Dude",last="Code")