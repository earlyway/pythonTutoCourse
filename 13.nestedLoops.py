# nested loops = The "inner loop" will finish all of it's iterations before finishing one iteration of the "outer loop"
# inner loop는 outer loop가 한번의 반복을 끝내기 전에 모든 반복을 끝낼 것이다. 중첩문


rows = int(input('How many rows? : '))
columns = int(input('How many columns? : '))
symbol = input('Enter a symbol to use: ')

for i in range(rows):
    for j in range(columns):
        print(symbol, end = "")
    print()