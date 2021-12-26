# 나이트 움직이기

input_data = input() # a1을 입력받기
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 # 문자을 숫자로 대응. 아스키코드 이용

steps = [(-2, -1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] # 나이트 이동 경로 8가지 정의. **연산과 자료구조의 활용

cnt = 0
for step in steps: # 파이썬의 for은 횟수반복문이면서 in이라는 연산자를 이용해 자료구조적 이득을 볼 수 있음
    next_row = row + step[0] # 열 이동
    next_column = column + step[1] # 행 이동
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        cnt += 1
print(cnt)


# 유닛의 자동 이동

n, m = map(int, input().split()) # N, M을 공백을 기준으로 구분하여 입력받기

x, y, direction = map(int, input().split()) # 현재 캐릭터의 X 좌표, Y 좌표, 방향을 입력받기

d = [[0] * m for _ in range(n)] # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d[x][y] = 1 # 현재 좌표 방문 처리

array = []
for i in range(n):
    array.append(list(map(int, input().split()))) # 전체 맵 정보를 입력받기

dx = [-1, 0, 1, 0] # 북, 동, 남, 서 방향 정의
dy = [0, 1, 0, -1]

def turn_left(): # 왼쪽으로 회전 함수. 완전탐색(시뮬레이션)에서 함수의 이용. 반복되는 동작이므로 효율적임
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1 # 방문 횟수
turn_time = 0
while True: # 시뮬레이션 시작
    turn_left() # 왼쪽으로 회전
    nx = x + dx[direction] # 회전만 하기, 회전하고 이동하기 동작을 분리하는 과정에서 nx와 ny 변수 추가.
    ny = y + dy[direction]
    if d[nx][ny] == 0 and array[nx][ny] == 0: # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동.
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    else: # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
        turn_time += 1
    if turn_time == 4: # 네 방향 모두 갈 수 없는 경우
        nx = x - dx[direction]
        ny = y - dy[direction]
        if array[nx][ny] == 0: # 뒤로 갈 수 있다면 이동하기
            x = nx
            y = ny
        else: # 뒤가 바다로 막혀있는 경우
            break
        turn_time = 0

print(count) # 정답 출력
