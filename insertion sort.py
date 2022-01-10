# 삽입 정렬: 데이터를 차례로 적절한 위치에 삽입하며 정렬하는 알고리즘.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)): # 두번째 데이터부터 차례로
  for j in range(i, 0, -1): # 적절한 위치에 삽입하기 위해 j는 i부터 1까지 -1씩 감소하며 진행.
    if array[j] < array[j - 1]:
      array[j], array[j - 1] = array[j - 1], array[j] # 작으면 swap.
    else: # 삽입 완료.
      break # 다음 데이터로.

print(array)


'''
// c언어에서 삽입 정렬

#include <stdio.h>
#include <stdlib.h>

void insertion(int a[], int n)
{
  int i, j;
  for(i = 1; i < n; i++){ // 두번째 데이터부터 차례로
    int tmp = a[i]; // 삽입할 데이터 tmp에 저장해두기. (swap 함수 안쓴다면)
    for(j = i; j > 0 && a[j - 1] > tmp; j--) // 적절한 위치에 삽입하기 위해 j는 i부터 1까지 -1씩 감소하며 진행.
      a[j] = a[j - 1]; // 작으면 데이터 오른쪽으로 계속 밀기.
    a[j] = tmp; // 삽입 완료. 저장해둔 tmp를 적절한 위치에 도달했을때 a[j]에 대입.
  }
}

'''
