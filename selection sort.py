# 선택 정렬: 매번 가장 작은 것을 선택하여 정렬하는 알고리즘.

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)): # 정렬하기 위한 맨 앞부터의 인덱스
  min_index = i # 최솟값의 인덱스 초깃값 0.
  for j in range(i + 1, len(array)): # 나머지 데이터의 search_min(or max)_index. **search_min의 경우 데이터를 끝까지 진행시키면서 최소 갱신 시 m에 최솟값을 저장해놓는 방식이다.
                                     # 하지만 최솟값의 인덱스를 구하는 경우, 데이터를 끝까지 진행시키면서 최소 갱신 시 min_index에 최솟값의 인덱스를 저장해놓는다.
    if array[min_index] > array[j]: # 최소 갱신.
      min_index = j # 최솟값의 인덱스 저장.
  array[i], array[min_index] = array[min_index], array[i] # min_index와 i의 요소를 swap **파이썬 swap : 특정한 리스트가 주어졌을 때 두 변수의 위치를 변경하는 작업. 

print(array)


'''
// c언어에서 선택정렬

#include <stdio.h>
#include <stdlib.h>
#define swap(type,x,y) do{type t=x; x=y; y=t;} while(0) // 매크로 정의 함수. swap정의

int selection(int a[], int n)
{
  int i, j;
  for(i=0; i < n-1; i++) {
    int min = j;
    for(j = i+1; j < n; j++){
      if(a[j] < a[min])
        min = j;
    }
    swap(int, a[i], a[min]);
  }
}

'''
