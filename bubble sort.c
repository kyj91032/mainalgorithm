// 버블 정렬: 계속해서 swap하여 차례로 정렬하는 알고리즘

#include <stdio.h>
#include <stdlib.h>
#define swap(type, x, y) do { type t=x; x=y; y=t; } while(0)

void bubble(int a[], int n)
{
  int i, j;
  for(i = 0; i < n - 1; i++) { // i는 start 부터 end - 1 까지.
    for(j = n - 1; j > i; j--) // j는 i + 1 까지만 반복해서 swap 하면 됨. j와 j - 1을 swap 하기 때문에 마지막에 i + 1 과 i를 swap하면 끝이기 때문.
      if(a[j - 1] > a[j])
        swap(int, a[j - 1], a[j]);
  }
}


// 알고리즘 개선 1: swap이 없을 때 정렬을 마치도록

#include <stdio.h>
#include <stdlib.h>
#define swap(type, x, y) do { type t=x; x=y; y=t; } while(0)

void bubble(int a[], int n)
{
  int i, j;
  for(i = 0; i < n - 1; i++) { // i는 start 부터 end - 1 까지.
    int exchg = 0; // 하나의 요소를 결정할 때 까지 swap한 횟수.
    for(j = n - 1; j > i; j--) // j는 i + 1 까지만 반복해서 swap 하면 됨. j와 j - 1을 swap 하기 때문에 마지막에 i + 1 과 i를 swap하면 끝이기 때문.
      if(a[j - 1] > a[j]) {
        swap(int, a[j - 1], a[j]);
        exchg++;
      }
    if(exchg == 0) break; // swap한 횟수가 0이라면 정렬 끝.
  }
}


// 알고리즘 개선 2: 마지막 swap까지 건너뛰면서 정렬하기

#include <stdio.h>
#include <stdlib.h>
#define swap(type, x, y) do { type t=x; x=y; y=t; } while(0)

void bubble(int a[], int n)
{
  int k = 0;
  while(k < n - 1) {
    int j;
    int last = n - 1; // if문이 실행되지 않으면 정렬되어 있다는 것이므로 last를 n - 1로 두어 while문을 탈출한다.
    for(j = n - 1; j > k; j--) // 3. 다음 시행 시 k(=last)까지만 정렬하게 함.
      if(a[j - 1] > a[j]) {
        swap(int, a[j - 1], a[j])
          last = j; // 1. 기억해둔 last를
      }
    k = last; // 2. k에 넣어서
  }
}
