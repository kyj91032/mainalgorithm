# 큰 수의 법칙. 일단 큰 수 먼저 3개 박고 두번째로 큰 수 1개 박기. 그리디 알고리즘

n, m, k = map(int, input().split()) # N, M, K를 공백을 기준으로 구분하여 입력 받기
data = list(map(int, input().split())) # N개의 수를 공백을 기준으로 구분하여 입력 받기

data.sort() # 입력 받은 수들 정렬하기. **정렬을 활용한 최대최소 구하기.
first = data[n - 1] # 가장 큰 수
second = data[n - 2] # 두 번째로 큰 수

count = int(m / (k + 1)) * k # 가장 큰 수가 더해지는 횟수 계산
count += m % (k + 1)

result = 0
result += (count) * first # 가장 큰 수 더하기
result += (m - count) * second # 두 번째로 큰 수 더하기

print(result) # 최종 답안 출력
