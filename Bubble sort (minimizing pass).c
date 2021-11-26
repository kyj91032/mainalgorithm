#include <stdio.h>
#include <stdlib.h>
#define swap(type, x, y) do { type t=x; x=y; y=t; } while(0)

void bubble(int a[], int n)
{
  int i, j;
  for(i=n-1; i>0; i--) {
    int swapnum = 0;
    for(j=0; j<i; j++) {
      if(a[j] > a[j+1]) {
        swap(int, a[j], a[j+1]);
        swapnum++;
      }
    }
    if(swapnum == 0) break;
  }
}
