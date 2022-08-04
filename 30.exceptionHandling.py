# exception = events detected during execution that interrupt the flow of a program
# 실행하는 동안 프로그램 흐름을 중단하는 이벤트가 탐지된다.


try :
    numerator = int(input("Enter a number to divide :")) #분자
    denominator = int(input("Enter a number to divide by : ")) #분모
    result = numerator / denominator
    
except ZeroDivisionError as e: # 0 인풋을 인식하고 에러 내용을 프린트로 바꿈
    print(e)
    print("You cant divide by zero! ")
except ValueError as e: # 문자열 인풋을 인식함
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong : (")
else:
    print(result)
finally:
    print("This will always execute")