#include <stdio.h>

int search(const int a[], int n, int key)
{
	int i = 0;
	while(1){
		if(i == n)	// i가 배열의 끝에 갔을 때, 일치하는지 검사하기 전 종료시키기 위해 이 if문이 먼저 등장한다.
			return -1;
		if(a[i] == key) // key와 일치하는가 확인. 일치하면 인덱스 리턴
			return i;
		i++;
	}
}
