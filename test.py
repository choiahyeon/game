import mod1

num1 = 10
num2 = 5

#더하기를 해보자 num1+num2
result1 = mod1.add(num1, num2)
#결과값 출력을 해보자
print(result1)

#빼기를 해보자 num1-num2
result2 = mod1.sub(num1, num2)
#결과값 출력을 해보자
print(result1)

#두 수를 입력 받게 만들고
#메뉴 1.더하기 2.빼기
#1를 누르면 두 수의 더한 결과값
#2를 누르면 두 수의 뺸 결과값
#출력되도록 해보자

###스스로 해본 것####
munustep = '''
1. 더하기
2. 뺴기 
'''

#print("메뉴를 선택하세요")
#print(munustep)
#num = input("당신의 선택:")
#만약 1를 누르면
#if num == '1':
    #print(f"당신은 {num}를 누르셨습니다")
    #print(result1)
#elif num == '2':
    #print(f"당신은 {num}를 누르셨습니다")
    #print(result2)

###스스로 해본 것####



#두 수를 입력 받게 만들고
num1 = int(input("첫번째 수 입력:")) #문자로 입력 되기 때문에 숫자로 변경
num2 = int(input("첫번째 수 입력:")) #문자로 입력 되기 때문에 숫자로 변경

#메뉴 1.더하기 2.빼기
print("1.더하기 2.빼기")
num = int(input("선택: "))

#만약에 1를 누르면 두 수의 뺸 결과값
if num == 1:
    result = mod1.add(num1, num2)
#만약에 2를 누르면 두 수의 뺸 결과값
elif num == 2:
    result = mod1.sub(num1, num2)
#출력되도록 해보자
print("결과값:", result)