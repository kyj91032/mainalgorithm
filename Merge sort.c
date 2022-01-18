// 병합 정렬: 정렬을 마친 배열의 병합을 응용하여 분할 정복법(ex 퀵 정렬)에 따라 정렬하는 알고리즘.

#include <stdio.h>
#include <stdlib.h>

static int *buff; // buff에 앞 부분 빼놓고 buff의 앞부분과 a의 뒷부분을 a로 병합. 작업용 배열(버퍼 buffer)

static void __mergesort(int a[], int left, int right) // 맨 앞 인덱스와 맨 마지막 인덱스를 나타내는 고정 변수 left, right (퀵 정렬에서도 씀. start와 end는 고정, left와 right는 커서)
{
	if(left < right) {
		int center = (left + right) / 2;
		int p = 0;
		int i;
		int j = 0;
		int k = left;
		__mergesort(a, left, center);
		__mergesort(a, center+1, right);
		for(i = left; i <= center; i++) // buff(p)에 a의 앞 부분(i <= center) 빼놓기.
			buff[p++] = a[i];
		while(i <= right && j < p) // a의 뒷 부분을 (i <= right)가 이어서 진행하며 buff(j < p)와 함께 a에 새로 병합 정렬(k).
			a[k++] = (buff[j] <= a[i]) ? buff[j++] : a[i++];
		while(j < p)
			a[k++] = buff[j++]; // buff에 남은 요소를 배열 a로 마저 복사. 만약 a에 남은 요소가 있는 경우는 a에 병합 정렬하기 때문에 그대로 냅두면 따로 코드 필요 없음.
	}
}

int mergesort(int a[], int n)
{
	if((buff = calloc(n, sizeof(int))) == NULL)
		return -1;
	__mergesort(a, 0, n - 1);
	free(buff);
	return 0;
}
