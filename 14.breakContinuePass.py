# Loop control statements = change a loops execution from its normal sequence
# 기본 시퀀스에서 loop 실행을 변경한다.

# break : used to terminate the loop entirely 루프 전체를 파괴, 끝내기
# continue : skips to the next iteration of the loop. 루프의 다음 반복을 스킵.
# pass : does nothing, acts as a placeholder 아무것도 하지않고 자리를 차지함.


#14-1
# while True:
#     name = input('Enter your name: ')
#     if name != "":
#         break

#14-2
# phone_number = "123-456-7890"
# for i in phone_number:
#     if i == "-":
#         continue      # i = "-"가 나오면 해당 반복문만 스킵.
#     print(i, end="")
    

#14-3
for i in range(1,21):
    if i == 13 :
        pass  #아무것도 하지않음.
    else :
        print(i)
