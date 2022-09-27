# 아침코테 #코드업 #파이썬 #기초100제 #리스트 #바둑알십자뒤집기

# 타이틀: 6097 : [기초-리스트] 설탕과자 뽑기
# 문제 : 격자판의 세로(h), 가로(w), 막대의 개수(n), 각 막대의 길이(l), 막대를 놓는 방향(d:가로는 0, 세로는 1)과 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치(x, y)가 주어질 때, 격자판을 채운 막대의 모양을 출력하는 프로그램을 만들어보자.

# 부모님과 함께 놀러간 영일이는
# 설탕과자(설탕을 녹여 물고기 등의 모양을 만든 것) 뽑기를 보게 되었다.

# 길이가 다른 몇 개의 막대를 바둑판과 같은 격자판에 놓는데,

# 막대에 있는 설탕과자 이름 아래에 있는 번호를 뽑으면 설탕과자를 가져가는 게임이었다.
# (잉어, 붕어, 용 등 여러 가지가 적혀있다.)

'''
참고
리스트가 들어있는 리스트를 만들면?
가로번호, 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다.
리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있다.


입력
첫 줄에 격자판의 세로(h), 가로(w) 가 공백을 두고 입력되고,
두 번째 줄에 놓을 수 있는 막대의 개수(n)
세 번째 줄부터 각 막대의 길이(l), 방향(d), 좌표(x, y)가 입력된다.
1 <= w, h <= 100
1 <= n <= 10
d = 0 or 1
1 <= x <= 100-h
1 <= y <= 100-w

출력
모든 막대를 놓은 격자판의 상태를 출력한다.
막대에 의해 가려진 경우 1, 아닌 경우 0으로 출력한다.
단, 각 숫자는 공백으로 구분하여 출력한다.


'''

# 입력 예시
# 5 5
# 3
# 2 0 1 1
# 3 1 2 3
# 4 1 2 5

# 출력 예시
# 1 1 0 0 0
# 0 0 1 0 1
# 0 0 1 0 1
# 0 0 1 0 1
# 0 0 0 0 1

w, h = input().split()
w = int(w)
h = int(h)
n = int(input())

data = [];
for i in range(w) :
  data.append([]);
  for j in range(h) :
      data[i].append(0);

for i in range(n) :
  l,d,x,y = input().split()
  l = int(l)
  d = int(d)
  x = int(x)
  y = int(y)
  for i in range(int(l)) : 
    if d == 0:
      data[x-1][y-1+i] = 1
    else :
      data[x-1+i][y-1] = 1

for i in range(w) :
  for j in range(h) : 
    print(data[i][j], end=" ")
  print()