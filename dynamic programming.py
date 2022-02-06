# 다이나믹(!= 동적, 런타임) 프로그래밍의 사용 조건 - 큰 문제와 작은 문제가 (as recurrence relation) 영향을 주며 존재하고, 똑같은 작은 문제를 반복적으로 해결해야 할 때.
# (=> 점화식이 존재(recurrence relation) and 기억공간 필요 -> 다이나믹 프로그래밍 != 분할정복)
# 초기값부터 i까지 모두 recurrence relation으로서 영향을 주고 있어 한번에 필드가 정복됨.

# 점화식이 존재한다면, 일단 재귀 함수를 사용하여 문제를 해결할 수 있다. 여기서 작은 문제를 반복적으로 해결해야한다면 dp 테이블 혹은 메모이제이션을 사용하여 다이나믹 프로그래밍을 할 수 있다.

# 탑 다운(하향식) 방식. 재귀 f 함수 기반 점화식

d = [0] * 100 # 메모이제이션을 위한 리스트

def fibo(x):
  print('f(' + str(x) + ')', end = ' ')
  if x == 1 or x == 2: # 종료조건
    return 1
  if d[x] != 0: # 메모이제이션
    return d[x]
  d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
  
# 바텀 업(상향식) 방식. 반복 a 수열 기반 점화식

d = [0] * 100 # dp 테이블

d[1] = 1 # 초기값
d[2] = 1

for i in range(3, 100) # 반복조건
  d[i] = d[i - 1] + d[i - 2]
  

# 1로 만들기 예제

x = int(input())
d = [0] * 30001 # dp 테이블. 인덱스가 주어진 정수, 그에 대한 값이 1까지 연산하는 최소 횟수.
                # d[0]과 d[1]은 어차피 0. 여기서 초깃값은 설정됨.
# f(i) = ai = i번째 수 까지의 최적의 해(연산 횟수)
# 점화식: ai = max(ai-1, ai/2, ai/3, ai/5) + 1 or f(i) = max(f(i-1), f(i/2), f(i/3), f(i/5)) + 1 

for i in range(2, x + 1):
  d[i] = d[i - 1] + 1  # d[i]의 최소를 구하기 위한 초깃값.
  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)
  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)
  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1) # 모든 경우 확인하며 최신화해서 d[i]의 최솟값 구하기.

print(d[x])


# 개미 전사 예제

n = int(input())
array = list(map(int, input().split())
# f(i) = ai = i번째 식량창고까지의 최적의 해(식량 값)
# 점화식: ai = max(ai-1, ai-2 + ki)

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])
for i in range(2, n):
  d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])             


#





 
