# dictionary comprehension == create dictionaries using an expression.
#   can replace for loops and certain lambda functions.
#   dictionary = {key : expression for (key,value) in iterable}
#   dictionary = {key : expression for (key,value) in iterable if conditional}
#   dictionary = {key : (if/else) for (key,value) in iterable}
#   dictionary = {key : function(value) for (key,value) in iterable}
#    딕셔너리를 이용한 식을 만든다.
#       루프와 특정 lambda 함수를 대체할 수 있다.
cities_in_F = {'NewYork':32, 'Boston':75, 'LosAngeles':100, 'Chicago':50}
cities_in_C = {key : round((value-32)*(5/9)) for (key,value) in cities_in_F.items()}
print(cities_in_C)

#########################
weather = {'NewYork':'snowing', 'Boston':'sunny', 'LosAngeles':'sunny', 'Chicago':'cloudy'}
sunny_weather = {key : value for (key,value) in weather.items() if value == 'sunny'}
print(sunny_weather)
############################
cities = {'NewYork':32, 'Boston':75, 'LosAngeles':100, 'Chicago':50}
desc_cities = {key : ('WARM' if value >= 40 else 'COLD') for (key,value) in cities.items()}
print(desc_cities)
##############################
def check_temp(value):
    if value >= 70:
        return 'hhoott'
    elif 69>=value >=40:
        return 'wwarm'
    else:
        return "cold"

cities = {'NewYork':32, 'Boston':75, 'LosAngeles':100, 'Chicago':50}
desc = {key :check_temp(value) for (key,value) in cities.items()}
print(desc)