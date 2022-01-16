# 계수 정렬: 데이터를 리스트에 담아서 차례로 나열해 정렬하는 알고리즘.

array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2] # 데이터의 크기 범위가 제한되고 정수 형태로 표현할 수 있을 때 사용가능한 정렬 방법.

count = [0] * (max(array) + 1) # 데이터의 크기 범위 만큼의 리스트 생성. 모든 요소(각 데이터의 개수로 사용)는 0으로 초기화

for i in range(len(array)):
  count[array[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가 (개수 세기)

for i in range(len(count)): # count에서 개수만큼 차례로 데이터 출력.
  for j in range(count[i]):
    print(i, end = ' ')
