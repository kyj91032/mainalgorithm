#include <stdio.h>
#include <stdlib.h>

int binary_search(const int a[], int n, int key) //전제는 "정렬된 데이터". key와의 "크기 판단"으로 검색 범위를 좁히는 것이기 때문.
{
	int pl = 0;
	int pr = n - 1;
	int pc;
	do {
		pc = (pl + pr) / 2;
		if(a[pc] == key)
			return pc;
		else if(a[pc] < key)
			pl = pc + 1;
		else
			pr = pc - 1;
	} while (pl <= pr); // 조건 반복문. 조건 사후 판단. 첫 시행은 조건에 관계없이 시행하고 시작해야 할 때.
	return -1;
}


//bsearch 함수

void *bsearch(const void *key, const void *base, size_t nmemb, size_t size, //1. 키 값을 가진 변수의 포인터, 2. 검색할 배열(동적 메모리)의 주소, 3. 배열 요소 개수, 4. 배열 요소 크기
	      int(*compar)(const void *, const void *)); /* 5. 비교 함수 포인터. 가인수 compar은 비교함수의 주소를 받는다. 그 함수는 (const void *, const void *)를 입력받고
							       int를 반환하는 함수이어야 한다.
							 */

int int_cmp(const int *a, const int *b) /* (const int *, const int *)를 입력받고 int를 반환하는 비교함수. 함수 포인터 compar과 함수 int_cmp의 자료형이 다르다.
					   따라서 bsearch 함수를 호출할 때 비교함수의 자료형을 캐스팅 해야한다. */
{
	if(*a < *b)
		return -1;
	else if(*a > *b)
		return 1;
	else
		return 0;
}

p = bsearch(&key, a, na, sizeof(int), (int(*)(const void *, const void *)) int_cmp); /* bsearch 함수의 호출. 검색 성공 시 그 인덱스의 포인터를 반환함. 실패 시 -1 반환.
											캐스팅 연산자 (int(*)(const void *, const void *))로 함수 int_cmp의 자료형 변환 */

