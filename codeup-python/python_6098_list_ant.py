# 아침코테 #코드업 #파이썬 #기초100제 #리스트 #성실한 개미

# 타이틀: 6098 : [기초-리스트] 성실한 개미
# 문제 : 미로 상자의 구조가 0(갈 수 있는 곳), 1(벽 또는 장애물)로 주어지고, 먹이가 2로 주어질 때, 성실한 개미의 이동 경로를 예상해보자.
#       단, 맨 아래의 가장 오른쪽에 도착한 경우, 더 이상 움직일 수 없는 경우, 먹이를 찾은 경우에는 더 이상 이동하지 않고 그 곳에 머무른다고 가정한다.

# 영일이는 생명과학에 관심이 생겨 왕개미를 연구하고 있었다.
# 왕개미를 유심히 살펴보던 중 특별히 성실해 보이는 개미가 있었는데, 그 개미는 개미굴에서 나와 먹이까지 가장 빠른 길로 이동하는 것이었다.

# 개미는 오른쪽으로 움직이다가 벽을 만나면 아래쪽으로 움직여 가장 빠른 길로 움직였다. (오른쪽에 길이 나타나면 다시 오른쪽으로 움직인다.)

# 이에 호기심이 생긴 영일이는 그 개미를 미로 상자에 넣고 살펴보기 시작하였다.
# 미로 상자에 넣은 개미는 먹이를 찾았거나, 더 이상 움직일 수 없을 때까지 오른쪽 또는 아래쪽으로만 움직였다. 
# 미로 상자의 테두리는 모두 벽으로 되어 있으며, 개미집은 반드시 (2, 2)에 존재하기 때문에 개미는 (2, 2)에서 출발한다.

'''
참고
리스트가 들어있는 리스트를 만들면?
가로번호, 세로번호를 사용해 2차원 형태의 데이터처럼 쉽게 기록하고 사용할 수 있다.
리스트이름[번호][번호] 형식으로 저장되어있는 값을 읽고 쓸 수 있다.

입력
10*10 크기의 미로 상자의 구조와 먹이의 위치가 입력된다.

출력
성실한 개미가 이동한 경로를 9로 표시해 출력한다.

'''

# 입력 예시
# 1 1 1 1 1 1 1 1 1 1
# 1 0 0 1 0 0 0 0 0 1
# 1 0 0 1 1 1 0 0 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 0 0 1 0 1
# 1 0 0 0 0 1 0 1 0 1
# 1 0 0 0 0 1 2 1 0 1
# 1 0 0 0 0 1 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1

# 출력 예시
# 1 1 1 1 1 1 1 1 1 1
# 1 9 9 1 0 0 0 0 0 1
# 1 0 9 1 1 1 0 0 0 1
# 1 0 9 9 9 9 9 1 0 1
# 1 0 0 0 0 0 9 1 0 1
# 1 0 0 0 0 1 9 1 0 1
# 1 0 0 0 0 1 9 1 0 1
# 1 0 0 0 0 1 0 0 0 1
# 1 0 0 0 0 0 0 0 0 1
# 1 1 1 1 1 1 1 1 1 1

# 배열입력
data = [];
for i in range(10) :
  data.append([]);
  for j in range(10) :
      data[i].append(0);

for i in range(10) :
  a = input().split()
  for j in range(10) :
    data[i][j] = int(a[j]);

start = 1;
isEnd = False;

for i in range(1, 10) :
  for j in range(start, 10) :
    print(start)
    value = data[i][j];
    if value == 1 :
      start = j-1;
      break;
    elif value == 2 :
      data[i][j] = 9;
      isEnd = True;
      break;
    else :
      data[i][j] = 9;

  if(isEnd) :
    break;

for i in range(10) :
  for j in range(10) : 
    print(data[i][j], end=" ");
  print();