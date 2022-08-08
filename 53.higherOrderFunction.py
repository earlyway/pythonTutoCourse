# Higher Order Functions = a function that either:
#    1. accepts a function as an argument
#   or
#   2.returns a function
#   (In python, functions are also treated as objects)
# 함수를 인수로 허락하거나 함수를 반환함
def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func):
    text = func('HElluuuu')
    print(text)

hello(loud)
hello(quiet)

############################

def divisor(x):
    def dividend(y):
        return y /  x
    return dividend

divide = divisor(2)
print(divide(10))