# 아침코테 #코드업 #파이썬 #기초100제 #비트단위논리연산

# 비트단위 연산자 정리

# 비트단위(bitwise) 연산자 종류
# ~(bitwise not),
# &(bitwise and),
# |(bitwise or) : | 은 파이프(pipe)연산자라고도 불리는 경우가 있다.,
# ^(bitwise xor),
# <<(bitwise left shift),
# >>(bitwise right shift)

# 타이틀: 6059 [기초-비트단위논리연산] 비트단위로 NOT 하여 출력하기
# 문제: 입력 된 정수를 비트단위로 참/거짓을 바꾼 후 정수로 출력해보자.
#      비트단위(bitwise)연산자 ~ 를 붙이면 된다.(~ : tilde, 틸드라고 읽는다.)

'''
예를 들어 1이 입력되었을 때 저장되는 1을 32비트 2진수로 표현하면
      00000000 00000000 00000000 00000001 이고,
~1은   11111111 11111111 11111111 11111110 가 되는데 이는 -2를 의미한다.

참고
컴퓨터에 저장되는 모든 데이터들은 2진수 형태로 바뀌어 저장된다.
0과 1로만 구성되는 비트단위들로 변환되어 저장되는데,
양의 정수는 2진수 형태로 바뀌어 저장되고, 음의 정수는 "2의 보수 표현"방법으로 저장된다.

양의 정수 5를 32비트로 저장하면, 

5의 2진수 형태인 101이 32비트로 만들어져
00000000 00000000 00000000 00000101
로 저장된다.(공백은 보기 편하도록 임의로 분리)

32비트 형의 정수 0은
00000000 00000000 00000000 00000000

그리고 -1은 0에서 1을 더 빼고 32비트만 표시하는 형태로
11111111 11111111 11111111 11111111 로 저장된다.

-2는 -1에서 1을 더 빼면 된다.
11111111 11111111 11111111 11111110 로 저장된다.

이러한 내용을 간단히 표현하면, 정수 n이라고 할 때,

~n = -n - 1
-n = ~n + 1 과 같은 관계로 표현할 수 있다.

이 관계를 그림으로 그려보면 마치 원형으로 수들이 상대적으로 배치된 것과 같다.

입력
정수 1개가 입력된다.
-2147483648 ~ +2147483647

출력
비트 단위로 1 -> 0, 0 -> 1로 바꾼 후 그 값을 10진수로 출력한다.
'''

# 입력 예시
# 2

# 출력 예시
# -3


# 타이틀: 6060 [기초-비트단위논리연산] 비트단위로 AND 하여 출력하기
# 문제: 입력된 정수 두 개를 비트단위로 and 연산한 후 그 결과를 정수로 출력해보자.
#      비트단위(bitwise)연산자 &를 사용하면 된다.(and, ampersand, 앰퍼센드라고 읽는다.)

'''
예를 들어 3과 5가 입력되었을 때를 살펴보면
3       : 00000000 00000000 00000000 00000011
5       : 00000000 00000000 00000000 00000101
3 & 5   : 00000000 00000000 00000000 00000001
이 된다.

비트단위 and 연산은 두 비트열이 주어졌을 때,
둘 다 1인 부분의 자리만 1로 만들어주는 것과 같다.

이 연산을 이용하면 어떤 비트열의 특정 부분만 모두 0으로도 만들 수 있는데
192.168.0.31   : 11000000.10101000.00000000.00011111
255.255.255.0 : 11111111.11111111.11111111.00000000

두 개의 ip 주소를 & 연산하면
192.168.0.0 :     110000000.10101000.0000000.00000000 을 계산할 수 있다.

실제로 이 계산은 네트워크에 연결되어 있는 두 개의 컴퓨터가 데이터를 주고받기 위해
같은 네트워크에 있는지 아닌지를 판단하는데 사용된다.

이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서
마스크연산(특정 부분을 가리고 출력하는)을 수행하는 데에도 효과적으로 사용된다.

입력
2개의 정수가 공백을 두고 입력된다.
-2147483648 ~ +2147483647

출력
두 정수를 비트단위(bitwise)로 and 계산을 수행한 결과를 10진수로 출력한다.
'''

# 입력 예시
# 3 5

# 출력 예시
# 1

a, b = input().split()
print(int(a) & int(b))

# 타이틀: 6061 [기초-비트단위논리연산] 비트단위로 OR 하여 출력하기
# 문제: 입력된 정수 두 개를 비트단위로 or 연산한 후 그 결과를 정수로 출력해보자.
#      비트단위(bitwise)연산자 |(or, vertical bar, 버티컬바)를 사용하면 된다.

'''

예를 들어 3과 5가 입력되었을 때를 살펴보면
3      : 00000000 00000000 00000000 00000011
5      : 00000000 00000000 00000000 00000101
3 | 5  : 00000000 00000000 00000000 00000111
이 된다.

비트단위 or 연산은 둘 중 하나라도 1인 자리를 1로 만들어주는 것과 같다.

이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서도 효과적으로 사용된다

입력
2개의 정수가 공백을 두고 입력된다.
-2147483648 ~ +2147483647

출력
두 정수를 비트단위(bitwise)로 or 계산을 수행한 결과를 10진수로 출력한다.
'''

# 입력 예시
# 3 5

# 출력 예시
# 7

a, b = input().split()
print(int(a) | int(b))

# 타이틀: 6062 [기초-비트단위논리연산] 비트단위로 XOR 하여 출력하기
# 문제: 입력된 정수 두 개를 비트단위로 xor 연산한 후 그 결과를 정수로 출력해보자.
#      비트단위(bitwise) 연산자 ^(xor, circumflex/caret, 서컴플렉스/카릿)를 사용하면 된다.


'''
** 주의 ^은 수학식에서 거듭제곱(power)을 나타내는 기호와 모양은 같지만,
C언어에서는 전혀 다른 배타적 논리합(xor, 서로 다를 때 1)의 의미를 가진다.

예를 들어 3과 5가 입력되었을 때를 살펴보면
3       : 00000000 00000000 00000000 00000011
5       : 00000000 00000000 00000000 00000101
3 ^ 5   : 00000000 00000000 00000000 00000110

이러한 비트단위 연산은 빠른 계산이 필요한 그래픽처리에서도 효과적으로 사용된다.

구체적으로 설명하자면,
두 장의 이미지가 겹쳐졌을 때 색이 서로 다른 부분만 처리할 수 있다.
배경이 되는 그림과 배경 위에서 움직이는 그림이 있을 때,
두 그림에서 차이만 골라내 배경 위에서 움직이는 그림의 색으로 바꿔주면
전체 그림을 구성하는 모든 점들의 색을 다시 계산해 입히지 않고
보다 효과적으로 그림을 처리할 수 있게 되는 것이다.
비행기 슈팅게임 등을 상상해보면 된다.

입력
2개의 정수가 공백을 두고 입력된다.
-2147483648 ~ +2147483647

출력
두 정수를 비트단위(bitwise)로 xor 계산을 수행한 결과를 10진수로 출력한다.
'''

# 입력 예시
# 3 5

# 출력 예시
# 6

a, b = input().split()
print(int(a) ^ int(b))
