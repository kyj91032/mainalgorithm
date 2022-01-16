# 퀵 정렬: 기준 데이터를 설정하여 탐색, swap, 분할을 반복해(재귀) 정렬하는 알고리즘.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
  if start >= end: # 원소가 1개인 경우 종료 (재귀함수의 종료조건)
    return
  
  pivot = start # 피벗을 첫번째 원소로 설정하고, 나머지 배열에서 정렬한 후 피벗을 중앙에 삽입(right와 swap).
  left = start + 1 # left 커서 정의
  right = end # right 커서 정의
  
  while left <= right: # 커서가 엇갈릴 때 까지. **조건 반복문은 while 1: if로 분해해서 생각. 전치인지 후치인지까지도.
    while left <= end and array[left] <= array[pivot]: # left 탐색
      left += 1
    while right > start and array[right] >= array[pivot]: # right 탐색
      right -= 1
    if left > right: # 엇갈렸다면 right와 피벗을 swap. (엇갈렸을 때 구조적으로 피벗은 right쪽에 있기 때문에, right와 swap해야 분할이 됨. 차순과는 상관없음)
      array[right], array[pivot] = array[pivot], array[right]
    else: # 엇갈리지 않았다면 left와 right를 swap.
      array[left], array[right] = array[right], array[left]

  quick_sort(array, start, right - 1)
  quick_sort(array, left + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)


'''

//c언어에서 퀵 정렬

#include <stdio.h>
#include <stdlib.h>
#define swap(type, x, y) do {type t = x; x = y; y = t;} while(0)

void quick(int a[], int left, int right)
{
	int pl = left;
	int pr = right;
	int x = a[(pl + pr) / 2]; //피벗을 가운데 요소로 설정. 피벗은 값 설정만 하고 실질적으로 정렬은 배열 전체에서 실행하는 것.
  
	do {
		while(a[pl] < x) pl++;
		while(a[pr] > x) pr--;
		if(pl <= pr) {
			swap(int, a[pl], a[pr]);
			pl++;
			pr--; // 써도되고 안써도 됨. 쓰는 게 탐색 덜 하긴 함.
		}
	} while(pl <= pr);
  
	if(left < pr) quick(a, left, pr); // 그룹 개수가 1인 경우를 거르면서 재귀.
	if(pl < right) quick(a, pl, right);
}


// qsort 함수 (stdlib.h)

void qsort(void *base, size_t nmemb, size_t size, int(*compar)(const void *, const void *));
// 1. 정렬할 배열(동적 메모리)의 주소, 2. 배열 요소 개수, 3. 배열 요소 크기
// 4. 비교 함수 포인터. 가인수 compar은 비교함수의 주소를 받는다. 그 함수는 (const void *, const void *)를 입력받고 int를 반환하는 함수이어야 한다.


#include <stdio.h>
#include <stdlib.h>

int int_cmp(const int *a, const int *b)
{
	if(*a < *b)
		return -1;
	else if(*a > *b)
		return 1;
	else
		return 0;
}


qsort(x, nx, sizeof(int), (int(*)(const void *, const void *))int_cmp); /* qsort 함수의 호출. 배열 x를 정렬시킴.
									   캐스팅 연산자 (int(*)(const void *, const void *))로 함수 int_cmp의 자료형 변환 */

'''
