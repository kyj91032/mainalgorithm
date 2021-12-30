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

