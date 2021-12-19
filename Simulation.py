// 나이트 움직이기

input_data = input()
row = int(input_data[1])
column = int(ord(input_data[0])) - int(ord('a')) + 1 #문자을 숫자로 대응. 아스키코드 이용

steps = [(-2, -1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)] #나이트 이동 경로 8가지 정의. **연산과 자료구조의 활용

cnt = 0
for step in steps: #파이썬의 for은 횟수반복문이면서 in이라는 연산자를 이용해 자료구조적 이득을 볼 수 있음
    next_row = row + step[0]
    next_column = column + step[1]
    if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <=8:
        cnt += 1
print(cnt)
