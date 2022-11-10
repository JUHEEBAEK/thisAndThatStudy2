# 아침코테 #코드업 #파이썬 #기초100제 #종합 #함께문제푸는날

# 타이틀: 6091 : [기초-종합] 함께 문제 푸는 날
# 문제: 같은 날 동시에 가입한 3명의 사람들이 온라인 채점시스템에 들어와 문제를 푸는 날짜가
#      매우 규칙적이라고 할 때, 다시 모두 함께 문제를 풀게 되는 그날은 언제일까?


'''

온라인 채점시스템에는 초등학생, 중고등학생, 대학생, 대학원생,
일반인, 군인, 프로그래머, 탑코더 등 아주 많은 사람들이 들어와 문제를 풀고 있는데,

실시간 채점 정보는 메뉴의 채점기록(Judge Status)을 통해 살펴볼 수 있다.

예를 들어 3명이 같은 날 가입/등업하고, 각각 3일마다, 7일마다, 9일마다
한 번씩 들어온다면, 처음 가입하고 63일 만에 다시 3명이 함께 문제를 풀게 된다.

갑자기 힌트?
왠지 어려워 보이지 않는가?
수학에서 배운 최소공배수를 생각한 사람들도 있을 것이다. 하지만, 정보에서 배우고 경험하는
정보과학의 세상은 때때로 컴퓨터의 힘을 빌려 간단한 방법으로 해결할 수 있게 한다.

아래의 코드를 읽고 이해한 후 도전해 보자.
day는 날 수, a/b/c는 방문 주기이다.
...
d = 1
while d%a!=0 or d%b!=0 or d%c!=0 :
  d += 1
print(d)
...

입력
같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는,
방문 주기가 공백을 두고 입력된다. (단, 입력값은 100이하의 자연수이다.)

출력
3명이 다시 모두 함께 방문해 문제를 풀어보는 날(동시 가입/등업 후 며칠 후?)을 출력한다.

'''

# 입력 예시
# 3 7 9

# 출력 예시
# 63

a, b, c = input().split()

a = int(a)
b = int(b)
c = int(c)

d = 1
while d % a != 0 or d % b != 0 or d % c != 0:
    d += 1

print(d)
