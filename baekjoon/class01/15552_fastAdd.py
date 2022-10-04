# 아침코테 #백준 #파이썬 #새싹클래스 #빠른 A + B

# 타이틀: 15552 빠른 A + B
# 문제: 빠르게 입출력 하기

# 본격적으로 for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.

''' 
입력
첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

출력
각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력한다.

'''


# 입력 예시
# 5
# 1 1
# 12 34
# 5 500
# 40 60
# 1000 1000

# 출력 예시
# 2
# 46
# 505
# 100
# 2000

import sys;

t = int(input());
for i in range(t):
  a, b = map(int, sys.stdin.readline().split())
  print(a + b)
