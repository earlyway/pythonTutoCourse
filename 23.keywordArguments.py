#keyword arguments = arguments preceded by an identifier when we pass them to a function
#The order of the arguments doesn't matter, unlike positional arguments.
#Python knows the names of the arguments that our function receives.
#키워드 arguments = argument는 함수에 그것들을 전달할때 식별자의 앞에 오는 argument이다.
#위치된 argument와는 달리 argument의 순서는 상관없다.
#python은 우리의 함수가 받는 그 argument들의 이름을 알고 있다.

def hello(first, mid, last) :
    print("Hello" +first+ "  "+mid+"  "+last)
    
hello("Code", "Dude", "Bro")

#만약에 호출을
#hello(last = "Code",first = "Dude",mid = "Bro")
#이렇게 호출한다해도 정상적으로 Hello Dude Bro Code 로 출력됨. 에러 XXX