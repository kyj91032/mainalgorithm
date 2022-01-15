# 퀵 정렬: 기준 데이터를 설정하여, 교체를 반복해 분할하고 분할을 반복해(재귀) 정렬하는 알고리즘.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1개인 경우 종료 (재귀함수의 종료조건)
    return
  pivot = start # 피벗은 첫 번째 원소
  left = start + 1 # left 커서 정의
  right = end # right 커서 정의
  while left <= right: # 커서가 엇갈린다면 종료
    while left <= end and array[left] <= array[pivot]: # left가 end 넘어가면 혹은 left가 피벗보다 큰 값(내림차순이라서)을 찾았다면 종료
      left += 1
    while right > start and array[right] >= array[pivot]: # right가 start에 가면 혹은 right가 피벗보다 작은 값을 찾았다면 종료
      right -= 1
    if left > right: # 엇갈렸다면 right와 피벗을 교체. (right가 피벗 위치(맨 앞)으로 가야 
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[left], array[right] = array[right], array[left]
  quick_sort(array, start, right - 1)
  quick_sort(array, left + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)
