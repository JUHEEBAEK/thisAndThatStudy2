# 아침코테 #코드업 #파이썬 #기초100제 #종합 #16진수구구단출력

# 타이틀: 6081 [기초-종합] 16진수 구구단 출력하기
# 문제:  A, B, C, D, E, F 중 하나가 입력될 때, 1부터 F까지 곱한 16진수 구구단의 내용을 출력해보자. (단, A ~ F 까지만 입력된다.)
'''
예시 :  print('%X'%n, '*%X'%i, '=%X'%(n*i), sep='')

16진수(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)를 배운
영일이는 16진수끼리 곱하는 16진수 구구단?에 대해서 궁금해졌다.

참고
print('%X'%n)  #n에 저장되어있는 값을 16진수(hexadecimal) 형태로 출력
작은 따옴표 2개를 사용해서 print(..., sep='') 으로 출력하면, 공백없이 모두 붙여 출력된다.
작은 따옴표 2개 '' 또는 큰 따옴표 2개 "" 는 아무 문자도 없는 빈문자열(empty string)을 의미한다.

입력
16진수로 한 자리 수가 입력된다.
단, A ~ F 까지만 입력된다.

출력
입력된 16진수에 1~F까지 순서대로 곱한, 16진수 구구단을 줄을 바꿔 출력한다.
계산 결과도 16진수로 출력해야 한다.
'''

# 입력 예시
# B

# 출력 예시
# B*1=B
# B*2=16
# B*3=21c
# B*4=2C
# B*5=37
# B*6=42
# B*7=4D
# B*8=58
# B*9=63
# B*A=6E
# B*B=79
# B*C=84
# B*D=8F
# B*E=9A
# B*F=A5

n = input()

for i in range(1, 16):
    changeInt = int(n, 16)
    res = changeInt * i
    print(n, '*', '%X' % i, '=', '%X' % res, sep='')
